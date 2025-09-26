import json


def load_data(file_path):
    with open(file_path, "r") as f:
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

    # print(suggestions)
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    # suggestions.items() will give key value pairs from which use value (x[1]) to sort them
    # sorted() always returns a list
    # print(sorted_suggestions)
    return [user_id for user_id, score in sorted_suggestions]


def pages_you_may_like(id, data):  # user id
    users_pages = {}
    for user in data["users"]:
        users_pages[user["id"]] = set(user["liked_pages"])

    if id not in users_pages:
        return []

    already_liked = users_pages[id]
    suggestions = {}

    for other_user, pages in users_pages.items():
        if other_user != id:
            shared_pages = already_liked.intersection(
                pages
            )  # overlapping pages which both like
        for page in pages:
            if page not in already_liked:
                suggestions[page] = suggestions.get(page, 0) + len(shared_pages)
                # score is the number pages both the users already like

    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [
        x[1] for x in sorted_suggestions if x[1] != 0
    ]  # ignore pages whose score is 0


data = load_data("massive_data.json")
# display_users(data)
recc_people = people_you_may_know(3, data)
print(recc_people)

recc_pages = pages_you_may_like(1, data)
print(recc_pages)
