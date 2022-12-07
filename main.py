import json

user_info = {}

user_info["name"] = input("Enter your name: ")
user_info["last_name"] = input("Enter your last name: ")
user_info["age"] = input("Enter your age: ")

with open("user_info.json", "w") as file:
    
    json.dump(user_info, file)

print("User information successfully saved to json file.")