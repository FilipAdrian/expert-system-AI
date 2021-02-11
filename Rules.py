import schema
from experta import *

from DataSet import *


class FactStructure(Fact):
    type = Field(str)
    isPresent = Field(bool, default=True)


class Equipment(Fact):
    wearType = Field(str, mandatory=True)
    isPresent = Field(bool, default=True)


class Eyes(Fact):
    type = Field(str, mandatory=True)
    isPresent = Field(bool, default=True)


class BodyType(Fact):
    type = Field(str, mandatory=True)
    isPresent = Field(bool, default=True)


class Hair(Fact):
    isPresent = Field(bool, default=True)


class Language(Fact):
    type = Field(schema.Or(*compresed_info["language"]))


# class Skin(Fact):
#     color = Field(str, mandatory=True)
#     isPresent = Field(bool, default=True)

class Skin(FactStructure):
    pass


class Tourist(Fact):
    type = Field(schema.Or(*list(dataset.keys())))


class TouristRules:
    @Rule(Tourist(type=MATCH.type))
    def found_tourist(self, type):
        print(f"Tourist is {type}")


class EquipmentRules:

    @Rule(OR(Equipment(wearType='spacesuit', isPresent=True),
             Equipment(wearType='jetpack', isPresent=False)))
    def has_spacesuit(self):
        print("-> Has SpaceSuit")
        self.declare(Eyes(type="round"))

    @Rule(OR(Equipment(wearType='spacesuit', isPresent=False),
             Equipment(wearType='jetpack', isPresent=True)))
    def has_no_spacesuit(self):
        print("-> Has Jetpack")
        print("-> Eyes are elongated")
        self.declare(Eyes(type='elongated'))

    @Rule(Equipment(wearType="missing"))
    def equipment_is_missing(self):
        self.declare(Tourist(type="loony"))


class HairRules:

    @Rule(Hair(isPresent=True))
    def has_hair(self):
        print("-> Has Hair")
        print("-> Could have White skin")
        self.declare(Skin(color="white", isPresent=True))

    @Rule(Hair(isPresent=False))
    def has_no_hair(self):
        print("-> Does not have Hair")
        print("-> Could not have White skin")
        self.declare(Skin(color="white", isPresent=False))


class EyesRules:

    @Rule(Eyes(type=L("round") | L("black")))
    def eyes_are_round(self):
        print("-> He has round eyes")
        self.declare(BodyType("humanoid"))
        self.declare(Language(type="english"))

    @Rule(Eyes(type="round", isPresent=False))
    def eyes_are_not_round(self):
        print("-> He does not have round eyes")
        self.declare(BodyType(type="humanoid", isPresent=False))


class BodyTypeRules:

    @Rule(OR(BodyType(type="humanoid", isPresent=False),
             BodyType(type=~L("humanoid"), isPresent=True)))
    def is_not_humanoid(self):
        print("-> He is not humanoid")
        self.declare(Equipment(wearType="jetpack"))

    @Rule(BodyType(type="humanoid", isPresent=True))
    def is_humanoid(self):
        print("-> He is humanoid")
        self.declare(Equipment(wearType="spacesuit"))


class LanguageRules:
    @Rule(Language(type=~L("english")))
    def is_not_english(self, type):
        print("-> He is reptiloid")
        self.declare(BodyType(type=type))


class SkinRules:
    @Rule(OR(Skin(type="green", isPresent=True),
             Skin(type="pigmented", isPresent=True)))
    def is_green_or_pigmented(self):
        self.declare(BodyType(type="humanoid", isPresent=False))
