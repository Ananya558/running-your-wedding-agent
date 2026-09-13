total_budget = int(input("Enter your total wedding budget: "))


venue = int(input("Enter your venue cost: "))
catering = int(input("Enter your catering cost: "))
photography = int(input("Enter your photography cost: "))
decor = int(input("Enter your decor cost: "))
makeup = int(input("Enter your makeup cost: "))

total_spent = venue + catering + photography + decor + makeup

remaining_budget = total_budget - total_spent
venue_percentage = (venue / total_budget) * 100
catering_percentage = (catering / total_budget) * 100
photography_percentage = (photography / total_budget) * 100
decor_percentage = (decor / total_budget) * 100
makeup_percentage = (makeup / total_budget) * 100

print("Total wedding budget:", total_budget)
print("Total spent:", total_spent)
print("Remaining budget:", remaining_budget)

print("Venue uses", venue_percentage, "% of your budget")
print("Catering uses", catering_percentage, "% of your budget")
print("Photography uses", photography_percentage, "% of your budget")
print("Decor uses", decor_percentage, "% of your budget")
print("Makeup uses", makeup_percentage, "% of your budget")
