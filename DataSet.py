
dataset = {
    "earthing": {"hair": ["light color", "short", "no hair"],
                 "equipment": ["oxygen mask", "spacesuit"],
                 "type": ["humanoid"],
                 "language": ["english"],
                 "skin": ["white", "black"],
                 "eyes": ["round"]
                 },
    "loony": {"hair": ["no hair"],
              "equipment": ["missing"],
              "type": ["humanoid"],
              "language": ["english", "loony"],
              "skin": ["gray"],
              "eyes": ["round", "black"]
              },
    "martian": {"hair": ["no hair"],
                "equipment": ["sun glasses", "spacesuit"],
                "type": ["humanoid"],
                "language": ["english", "martian"],
                "skin": ["brown"],
                "eyes": ["round"]
                },
    "mandalorian": {"hair": ["no hair"],
                    "equipment": ["jetpack"],
                    "type": ["reptiloid"],
                    "language": ["mandalorian"],
                    "skin": ["gray"],
                    "eyes": ["elongated"]
                    },
    "gamorrean": {"hair": ["no hair"],
                  "equipment": ["jetpack"],
                  "type": ["porcine"],
                  "language": ["english"],
                  "skin": ["green", "pigmented"],
                  "eyes": ["elongated"],
                  "other": ["two small horns", "unclear spoken words"]
                  },
    "abednedo": {"hair": ["above eyes"],
                 "equipment": ["sun glasses", "spacesuit"],
                 "type": ["humanoid", "mammalian"],
                 "language": ["english", "martian"],
                 "skin": ["brown", "white"],
                 "eyes": ["round", "black"]
                 }
}


def detect_characteristic_ratio():
    tourists_types = dataset.keys()
    characteristics = set()
    info = {}
    for type in tourists_types:
        keys = set(dataset[type].keys())
        for key in keys:
            if key not in info.keys():
                info[key] = set(dataset[type][key])
            else:
                tmp = set(info[key]).union(dataset[type][key])
                info[key] = tmp
        characteristics = characteristics.union(keys)
    max_key, value = max(info.items(), key=lambda x: len(set(x[1])))
    return info, max_key, list(value)


compresed_info, max_category, max_values = detect_characteristic_ratio()