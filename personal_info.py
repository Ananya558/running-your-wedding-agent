import json

DATA_FILE = "personal_info.json"


def load_personal_info():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_personal_info(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def run_personal_info():

    data = load_personal_info()

    print("\n👋 Let's get to know you!\n")

    # Name
    if data["name"] is None:
        data["name"] = input("Name: ")
    else:
        print(f"Name: {data['name']}")
    
     # Age
    if data["age"] is None:
        data["age"] = int(input("Age: "))
    else:
        print(f"Age: {data['age']}")

    # Email
    if data["email"] is None:
        data["email"] = input("Email Address: ")
    else:
        print(f"Email: {data['email']}")

    # Phone
    if data["phone"] is None:
        data["phone"] = input("Phone Number: ")
    else:
        print(f"Phone: {data['phone']}")

    save_personal_info(data)

    print("\n✅ Personal information saved!")