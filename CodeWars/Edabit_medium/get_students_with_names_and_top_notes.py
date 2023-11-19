# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] }
# and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

def top_note(students):
    students["top_note"] = max(students["notes"])
    students.pop("notes")
    return students


def test_top_note():
    test_data = [{"name": "John", "notes": [3, 5, 4]},
                 {"name": "Max", "notes": [1, 4, 6]},
                 {"name": "Zygmund", "notes": [1, 2, 3]}]

    test_results = [{"name": "John", "top_note": 5},
                    {"name": "Max", "top_note": 6},
                    {"name": "Zygmund", "top_note": 3}]

    for i in range(len(test_data)):
        std = test_data[i]
        result = top_note(std)
        if result == test_results[i]:
            print("Result for", test_data[i], "is passed")
        else:
            print("Result for", test_data[i], "is failed")


print(test_top_note())
