import json


def load_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
        data = clean_data(data)
        return data


def clean_data(data):
    for user in data["users"]:
        # removing inactive user
        data["users"] = [
            user for user in data["users"] if user["friends"] or user["liked_pages"]
        ]

        # removing invalid user (no name)
        data["users"] = [user for user in data["users"] if user["name"].strip()]

        # removing duplicate friends
        user["friends"] = list(set(user["friends"]))

        # removing duplicate liked_pages
        user["liked_pages"] = list(set(user["liked_pages"]))

    # removing duplicate pages
    d = {}
    for page in data["pages"]:
        if page["id"] in d:
            del page
        else:
            d[page["id"]] = page
    data["pages"] = list(d.values())
    return data


def display_users(data):
    print("\nUser connections:\n")
    for user in data["users"]:
        print(
            f"ID:{user['id']} - {user["name"]} is friends with {user["friends"]} and likes pages {user["liked_pages"]}"
        )

    print("\nPages Information:\n")
    for page in data["pages"]:
        print(f"{page["id"]}:{page["name"]}")


data = load_data("data2.json")
json.dump(data, open("cleaned_data.json", "w"), indent=4)
display_users(data)
