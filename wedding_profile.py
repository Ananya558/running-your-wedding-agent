import json

DATA_FILE = "wedding_data.json"


def load_wedding_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_wedding_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def run_profile():

    data = load_wedding_data()

    print("\n💍 Welcome to Happily Ever After!\n")

    # Budget
    if data["budget"] is None:
        data["budget"] = float(input("What is your total wedding budget (₹)? "))
    else:
        print(f"Your wedding budget is ₹{data['budget']:,.0f}")

    # Number of guests
    if data["guests"] is None:
        data["guests"] = int(input("How many guests are you expecting? "))
    else:
        print(f"Expected guests: {data['guests']}")

    # Location
    locations = [
        "Delhi / NCR",
        "Mumbai",
        "Jaipur",
        "Udaipur",
        "Goa",
        "Dehradun",
        "Other"
    ]

    print("\nWhere are you getting married?")
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")

    choice = int(input("Choose an option: "))

    if choice == len(locations):
        data["location"] = input("Enter your wedding location: ")
    else:
        data["location"] = locations[choice - 1]

    # Style
    styles = [
        "Traditional Indian",
        "Modern & Minimal",
        "Royal / Luxury",
        "Boho",
        "Destination Wedding",
        "Intimate / Small",
        "Other"
    ]

    print("\nWhat is your wedding style?")
    for i, style in enumerate(styles, 1):
        print(f"{i}. {style}")

    choice = int(input("Choose an option: "))

    if choice == len(styles):
        data["style"] = input("Describe your wedding style: ")
    else:
        data["style"] = styles[choice - 1]

    save_wedding_data(data)

    print("\n" + "=" * 40)
    print("YOUR WEDDING PROFILE")
    print("=" * 40)
    print(f"Budget: ₹{data['budget']:,.0f}")
    print(f"Guests: {data['guests']}")
    print(f"Location: {data['location']}")
    print(f"Style: {data['style']}")
    print("=" * 40)

    print("\n✅ Wedding profile saved!")