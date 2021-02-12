import schema
from experta import *

from DataSet import *


class Action(Fact):
    pass


class FactStructure(Fact):
    type = Field(str)
    isPresent = Field(bool, default=True)


class Equipment(FactStructure):
    pass


class Eyes(FactStructure):
    pass


class BodyType(FactStructure):
    pass


class Hair(FactStructure):
    pass


class Language(FactStructure):
    type = Field(schema.Or(*compresed_info["language"]))


class Skin(FactStructure):
    pass


class Tourist(Fact):
    type = Field(schema.Or(*list(dataset.keys())))


def remover_characterist(key, value):
    try:
        compresed_info[key].remove(value)
    except ValueError:
        pass


def check_last_fact(engine, *fact_list):
    if not any(isinstance(x, Tourist) for x in list(engine.facts.values())):
        for f in fact_list:
            if ((f is not None) and (list(engine.facts.values())[-1] == f)) or not engine.checked_all():
                engine.declare(Action("last"))


characteristics_class_list = {
    "hair": Hair,
    "equipment": Equipment,
    "type": BodyType,
    "language": Language,
    "skin": Skin,
    "eyes": Eyes
}
