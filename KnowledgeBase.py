from Rules import *


class Action(Fact):
    pass


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
        print(f"Which of {category} characteristic are applied: \n")
        question = ", ".join(
            "{name} ({key})".format(
                name=a, key=i)
            for a, i in enumerate(value, start=1)) + '? \n'
        response = input(question).split(",")
        return response

    @Rule()
    def start_interogation(self):
        print("There are 5 types of tourists and one Loony")
        print("Answer question to know whom you saw")
        print("INFO: For handling multiple responses, please enumerate them using comma."
              "\nFor example: Variant1 , Variant2")
        print("------------------------------------------")
        self.declare(Action(max_category))

    @Rule(AS.f1 << Action('skin'))
    def get_skin_answer(self, f1):
        self.retract(f1)
        res = self.display_questions(max_category, max_values)
        print(res)
        for r in res:
            self.declare(Skin(type=max_values[int(r.strip()) - 1]))

            # "hair"
            # "equipment"
            # "type"
            # "language"
            # "skin"
            # "eyes"

    @Rule(AS.f1 << Action('hair'))
    def get_hair_answer(self, f1):
        self.retract(f1)
        res = self.display_questions(max_category, max_values)
        for r in res:
            self.declare(Skin(color=max_values[int(r.strip()) - 1]))


    # @Rule(AS.f1 << Action('hair'))
    # def get_hair_answer(self, f1):
    #     self.retract(f1)
    #     res = self.display_questions(max_category, max_values)
    #     for r in res:
    #         self.declare(Skin(color=max_values[int(r.strip()) - 1]))