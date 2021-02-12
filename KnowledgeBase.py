from Rules import *


class Answer(Fact):
    pass


class KB(TouristRules,
         EquipmentRules,
         HairRules,
         BodyTypeRules,
         EyesRules,
         SkinRules,
         LanguageRules,
         KnowledgeEngine):

    def remove_facts(self, *facts):
        for fact in facts:
            self.retract(fact)

    def display_questions(self, category, value):

        print(f"\nWhich of {category} characteristic are applied: \n")
        question = ", ".join(
            "{name} ({key})".format(
                name=a, key=i)
            for a, i in enumerate(value, start=1)) + '? \n'
        responses = input(question).split(",")
        output = list()
        for r in responses:
            output.append(value[int(r.strip()) - 1])
            self.declare(characteristics_class_list[category](type=value[int(r.strip()) - 1], isPresent=True))
        return output

    def process_responses(self):
        for fact in list(self.facts.values()):
            for ch in characteristics_class_list.values():
                if isinstance(fact, ch) and fact.get("isPresent") == True:
                    name = ch.__name__.lower()
                    if name == "bodytype":
                        name = "type"
                    if fact.get("type") in compresed_info[name]:
                        compresed_info[name].remove(fact.get("type"))

    @Rule()
    def start_interogation(self):
        print("There are 5 types of tourists and one Loony")
        print("Answer question to know whom you saw")
        print("INFO: For handling multiple responses, please enumerate them using comma."
              "\nFor example: Variant1 , Variant2")
        print("------------------------------------------")
        self.declare(Action(max_category))

    @Rule(AS.f1 << Action(max_category))
    def get_answer(self, f1):
        self.remove_facts(f1)
        self.display_questions(max_category, max_values)

    @Rule(AS.f1 << Action(L("last")))
    def get_next(self, f1):
        self.remove_facts(f1)
        self.process_responses()
        for ch in characteristics_class_list.values():
            if not any(isinstance(x, ch) for x in list(self.facts.values())):
                name = ch.__name__.lower()
                if name == "bodytype":
                    name = "type"
                self.display_questions(name, compresed_info[name])
                break

    def checked_all(self):
        result = list()
        for ch in characteristics_class_list.values():
            if any(isinstance(x, ch) for x in list(self.facts.values())):
                result.append(ch.__name__.lower())

        if len(characteristics_class_list.keys()) == len(result):
            return True
        else:
            return False

    @Rule(Action(L("Done")))
    def exit(self):
        pass
