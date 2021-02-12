from KnowledgeBase import *

if __name__ == '__main__':
    engine = KB()
    engine.reset()
    engine.run()

    if not any(isinstance(x, Tourist) for x in list(engine.facts.values())):
        print("============================")
        print("Sorry: No Tourist was found with provided characteristics")
        print("============================")
    print(engine.facts)