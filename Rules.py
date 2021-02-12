from Facts import *


class TouristRules:
    @Rule(Tourist(type=MATCH.type))
    def found_tourist(self, type):
        print("============================")
        print(f"Possible Answer: Tourist is {type}")
        print("============================")
        self.declare(Action("Done"))
        return

    @Rule(
        OR(Equipment(type="oxygen mask", isPresent=True),
           AND(Hair(type="hair", isPresent=True),
               BodyType(type="humanoid", isPresent=True))))
    def is_earthing(self):
        self.declare(Tourist(type="earthing"))

    @Rule(
        OR(Language(type="loony", isPresent=True),
           AND(Equipment(type="missing", isPresent=True),
               BodyType(type="humanoid", isPresent=True))))
    def is_loony(self):
        self.declare(Tourist(type="loony"))

    @Rule(
        OR(Language(type="martian", isPresent=True),
           AND(BodyType(type="humanoid", isPresent=True),
               Skin(type="brown", isPresent=True))))
    def is_martian(self):
        self.declare(Tourist(type="martian"))

    @Rule(BodyType(type="mammalian", isPresent=True),
          Hair(type="hair", isPresent=True))
    def is_abednedo(self):
        self.declare(Tourist(type="abednedo"))

    @Rule(
        OR(AND(BodyType(type="reptiloid", isPresent=True),
               BodyType(type="humanoid", isPresent=False)),
           Language(type='mandalorian', isPresent=True)))
    def is_mandalorian(self):
        self.declare(Tourist(type="mandalorian"))

    @Rule(BodyType(type="porcine", isPresent=True),
          BodyType(type="humanoid", isPresent=False))
    def is_gamorrean(self):
        self.declare(Tourist(type="gamorrean"))


class EquipmentRules:

    @Rule(AS.f2 << Equipment(type='jetpack', isPresent=True))
    def has_jetpack(self, f1=None, f2=None):
        print("-> Has Jetpack")
        self.declare(BodyType(type="humanoid", isPresent=False))
        check_last_fact(self, f1, f2)

    @Rule(AS.f1 << Equipment(type="missing", isPresent=True))
    def equipment_is_missing(self, f1):
        print("-> Equipment is missing")
        self.declare(Language(type="english", isPreset=True))
        check_last_fact(self, f1)

    @Rule(AS.f1 << Equipment(type=~L("missing") & ~L("jetpack")))
    def no_equipment_match(self,f1):
        check_last_fact(self, f1)

class HairRules:

    @Rule(AS.f1 << Hair(type=~L('no hair'), isPresent=True))
    def has_hair(self, f1):
        print("-> Has Hair")
        self.declare(Hair(type="hair", isPresent=True))
        self.declare(Skin(type="white", isPresent=True))
        check_last_fact(self, f1)

    @Rule(AS.f1 << Hair(type='no hair', isPresent=True))
    def has_no_hair(self, f1=None):
        print("-> Does not have Hair")
        self.declare(Skin(type="white", isPresent=False))
        check_last_fact(self, f1)


class EyesRules:

    @Rule(AS.f1 << Eyes(type=L("round") | L("black"), isPresent=True))
    def eyes_are_round(self, f1):
        print("-> He has round eyes")
        self.declare(BodyType(type="humanoid", isPresent=True))
        self.declare(Language(type="english", isPresent=True))
        check_last_fact(self, f1)

    @Rule(AS.f1 << Eyes(type=MATCH.type, isPresent=True))
    def eyes_are_not_round(self, type, f1):
        print(f"-> He has {type} eyes")
        self.declare(BodyType(type="humanoid", isPresent=False))
        self.declare(Eyes(type="elongated", isPresent=True))
        check_last_fact(self, f1)


class BodyTypeRules:

    @Rule(OR(AS.f1 << Hair(type="above eyes", isPresent=True),
             AS.f2 << Equipment(type="sun glasses", isPresent=True)))
    def is_mammalian(self, f1=None, f2=None):
        print("-> He is not humanoid")
        self.declare(BodyType(type="mammalian", isPresent=True))
        check_last_fact(self, f1, f2)

    @Rule(AND(AS.f1 << Skin(type="white", isPresent=False),
              AS.f2 << Language(type="english", isPreset=False)))
    def is_reptiloid(self, f1=None, f2=None):
        print("-> He is not humanoid")
        self.declare(BodyType(type="mammalian", isPresent=True))
        check_last_fact(self, f1, f2)

    @Rule(AS.f1 << BodyType(type="humanoid", isPresent=True))
    def is_humanoid(self, f1):
        print("-> He is humanoid")
        self.declare(Eyes(type="round", isPresent=True))
        check_last_fact(self, f1)


class LanguageRules:
    pass


class SkinRules:
    @Rule(OR(AS.f1 << Skin(type="green", isPresent=True),
             AS.f2 << Skin(type="pigmented", isPresent=True)))
    def is_green_or_pigmented(self, f1=None, f2=None):
        self.declare(Hair(type='no hair', isPresent=True))
        self.declare(BodyType(type="porcine", isPresent=True))
        check_last_fact(self, f1, f2)

    @Rule(AS.f1 << Skin(type="white", isPresent=False))
    def is_not_white(self, f1):
        print("-> Skin is not white")
        self.declare(Hair(type='no hair', isPresent=True))
        check_last_fact(self, f1)

    @Rule(AS.f1 << Skin(type="white", isPresent=True))
    def is_white(self, f1):
        print("-> Skin is white")
        self.declare(Hair(type="hair", isPresent=True))
        check_last_fact(self, f1)

    @Rule(AS.f1 << Skin(type=~L("white") & ~L("green") & ~L("pigmented"), isPresent=True))
    def no_skin_match(self, f1):
        check_last_fact(self, f1)

