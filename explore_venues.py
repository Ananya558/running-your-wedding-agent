import csv

RAW_FILE = "data/panigrahana_venues_raw.csv"

# Open the file and read every row
with open(RAW_FILE, "r", encoding="utf-8") as file:
    licence_line = file.readline()   # line 1 is a licence note, not data
    reader = csv.DictReader(file)    # the remaining lines are the table
    venues = list(reader)

print("Licence line:", licence_line)
print("Total rows:", len(venues))

# Count venues in India, and in Goa specifically
india_count = 0
goa_count = 0

for venue in venues:
    if venue["country"] == "India":
        india_count = india_count + 1
    if venue["city"] == "Goa":
        goa_count = goa_count + 1

print("Venues in India:", india_count)
print("Venues in Goa:", goa_count)

# Show one Goa venue so we can see what a single row looks like
for venue in venues:
    if venue["city"] == "Goa":
        print("\nGoa venue:")
        print("  Name:", venue["venue"])
        print("  Type:", venue["venue_type_norm"])
        print("  Capacity:", venue["capacity_min"], "to", venue["capacity_max"])
        print("  Price per plate (₹):", venue["per_plate_min_inr"], "to", venue["per_plate_max_inr"])
        print("  Evidence tier:", venue["evidence_tier"])
        break