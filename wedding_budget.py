import json

DATA_FILE = "wedding_data.json"


def load_wedding_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_wedding_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def run_budget():

    data = load_wedding_data()

    print("\n💰 Wedding Budget Calculator\n")

    # Get wedding budget
    if data["budget"] is None:
        data["budget"] = float(input("What is your total wedding budget (₹)? "))
        save_wedding_data(data)
    else:
        print(f"Your total wedding budget is ₹{data['budget']:,.0f}")

    budget = data["budget"]

    # Ask for expenses
    print("\nEnter your current wedding expenses:\n")

    venue = float(input("Venue cost (₹): "))
    catering = float(input("Catering cost (₹): "))
    photography = float(input("Photography cost (₹): "))
    decor = float(input("Decor cost (₹): "))
    makeup = float(input("Makeup cost (₹): "))

    # Calculate total
    total_spent = venue + catering + photography + decor + makeup

    remaining = budget - total_spent

    # Display results
    print("\n" + "=" * 40)
    print("WEDDING BUDGET SUMMARY")
    print("=" * 40)

    print(f"Total Budget:     ₹{budget:,.0f}")
    print(f"Total Spent:      ₹{total_spent:,.0f}")
    print(f"Remaining:        ₹{remaining:,.0f}")

    print("=" * 40)