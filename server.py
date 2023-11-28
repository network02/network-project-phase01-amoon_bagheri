import json

users = {
    'user1': {'name': 'Alice', 'age': 30},
    'user2': {'name': 'Bob', 'age': 25},
    'user3': {'name': 'Charlie', 'age': 35}
}

while 1:
    user_input = input("Enter 'GET user_id' or 'POST user_name user_age' to simulate a request: ")
    if user_input[:3] == "GET":
        row = users.get(user_input.replace("GET", "").strip())
        if row is not None:
            print("Response from the server:")
            print("HTTP:1/1 200 OK")
            print("Content-Type: application/json\n")
            print(json.dumps(row))
    elif user_input[:4] == "POST":
        inp = user_input.replace("POST", "").strip()
        name, age = inp.split(" ")
        last_key = list(users.keys())[-1]
        users[f'user{int(last_key.replace("user", "")) + 1}'] = {'name': name, 'age': age}
        print("Response from the server:")
        print("HTTP:1/1 200 OK")
        print("User data updated")
    else:
        print('invalid command')
