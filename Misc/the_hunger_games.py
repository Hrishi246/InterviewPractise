def who_eats_who(zoo):
    data = zoo.split(",")
    food_relation = {
        "antelope": ["grass"],
        "big-fish": ["little-fish"],
        "bug": ["leaves"],
        "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
        "chicken": ["bug"],
        "cow": ["grass"],
        "fox": ["chicken", "sheep"],
        "giraffe": ["leaves"],
        "lion": ["antelope", "cow"],
        "panda": ["leaves"],
        "sheep": ["grass"]
    }

    expected = [zoo]
    def logic_function(data):
        for i in range(len(data)):
            if i == 0:
                if data[i] in food_relation.keys() and data[i + 1] in food_relation[data[i]]:
                    expected.append(data[i] + " eats " + data[i + 1])
                    data.remove(data[i + 1])
                else:
                    continue
            if i > 0 and i < len(data)+1:
                if data[i] in food_relation.keys() and data[i - 1] in food_relation[data[i]]:
                    expected.append(data[i] + " eats " + data[i - 1])
                    data.remove(data[i - 1])
                if data[i] in food_relation.keys() and data[i + 1] in food_relation[data[i]]:
                    expected.append(data[i] + " eats " + data[i + 1])
                    data.remove(data[i + 1])

        return data


    while len(data) > 1:
        return_data = logic_function(data)
        data = return_data

print(who_eats_who("fox,bug,chicken,grass,sheep"))