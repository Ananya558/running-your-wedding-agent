import wedding_profile
import wedding_budget


print("\n💍 WELCOME TO HAPPILY EVER AFTER!")
print("=" * 40)

while True:
    print("\nWhat would you like to do?")
    print("1. Create / Update Wedding Profile")
    print("2. Calculate Wedding Budget")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        wedding_profile.run_profile()

    elif choice == "2":
        wedding_budget.run_budget()

    elif choice == "3":
        print("\n💍 Goodbye! Happy wedding planning!")
        break

    else:
        print("\n❌ Invalid option. Please choose 1, 2, or 3.")