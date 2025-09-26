import json


def load_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
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


def people_you_may_know(id, data):
    user_friends = {}  # users and their list of friends
    for user in data["users"]:
        user_friends[user["id"]] = user["friends"]

    if id not in user_friends:  # person not found in the data (data sanitization)
        return []

    direct_friends = user_friends[id]
    suggestions = {}

    for fr in direct_friends:
        for mutual in user_friends[fr]:  # looping over friends of friend
            if mutual != id and mutual not in direct_friends:
                # don't show me the original user and don't show me those who are already friends with the original user
                # count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    print(suggestions)
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    # suggestions.items() will return key value pairs return the values (x[1]) and sort them
    print(sorted_suggestions)
    return [user_id for user_id, _ in sorted_suggestions]


data = load_data("data.json")
# display_users(data)
recc = people_you_may_know(1, data)
print(recc)
