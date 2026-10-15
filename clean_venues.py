import csv

RAW_FILE = "data/panigrahana_venues_raw.csv"
CLEAN_FILE = "data/vendors.csv"

# Our standard vendor columns, in order (the V1 schema we agreed on)
COLUMNS = [
    "vendor_id", "vendor_name", "category", "subcategory",
    "city", "service_area",
    "price_min", "price_max", "price_unit", "starting_price",
    "rating", "review_count",
    "style_tags", "services",
    "capacity_min", "capacity_max", "indoor_outdoor",
    "source", "source_url", "last_verified", "data_confidence",
]


def value_or_na(text):
    """Return the text without extra spaces, or "NA" if it is empty."""
    text = text.strip()
    if text == "":
        return "NA"
    return text


# 1. Read the raw file
# How much to trust each price, based on Panigrahana's evidence tier
CONFIDENCE_BY_TIER = {
    "studio-confirmed": "high",
    "listing-reference": "medium",
    "studio-estimate": "low",
}


def get_confidence(evidence_tier):
    """Turn Panigrahana's evidence tier into high / medium / low."""
    return CONFIDENCE_BY_TIER.get(evidence_tier.strip(), "low")


def get_services(rooms):
    """Describe on-site accommodation, if the venue has rooms."""
    rooms = rooms.strip()
    if rooms == "":
        return "NA"
    return f"accommodation: {rooms} rooms"


def get_style_tags(venue):
    """Guess which wedding styles a venue suits (our inference, not source data)."""
    venue_type = venue["venue_type_norm"]
    tags = []

    if venue_type == "heritage / palace" or venue["star_tier"] == "5-star":
        tags.append("Royal / Luxury")

    if venue_type in ["heritage / palace", "kalyana mantapa", "lawn / banquet hall"]:
        tags.append("Traditional Indian")

    if venue_type in ["hotel", "convention centre"]:
        tags.append("Modern & Minimal")

    if venue_type in ["villa / boutique", "farmhouse / estate"]:
        tags.append("Boho")

    if venue_type == "resort" or venue["region"] in ["Goa", "Kerala"]:
        tags.append("Destination Wedding")

    capacity = venue["capacity_max"].strip()
    if capacity.isdigit() and int(capacity) <= 100:
        tags.append("Intimate / Small")

    if len(tags) == 0:
        return "NA"
    return "|".join(tags)


with open(RAW_FILE, "r", encoding="utf-8") as file:
    licence_line = file.readline()
    reader = csv.DictReader(file)
    raw_venues = list(reader)

# The licence line ends with "generated 2026-09-27". We keep that date.
dataset_date = licence_line.strip().split("generated ")[-1]

# 2. Convert each Indian venue into our format
clean_venues = []

for venue in raw_venues:
    if venue["country"] != "India":
        continue  # skip Bali, Thailand, Europe

    number = len(clean_venues) + 1
    price_min = value_or_na(venue["per_plate_min_inr"])

    # Only say "per_plate" if there is actually a price
    if price_min == "NA":
        price_unit = "NA"
    else:
        price_unit = "per_plate"

    # Prefer the original price source; otherwise use Panigrahana's venue page
    if venue["source_url"].strip() != "":
        source_url = venue["source_url"].strip()
    else:
        source_url = venue["page_url"].strip()

    # Use the venue's own check date if it has one; otherwise the file's date
    if venue["verified_on"].strip() != "":
        last_verified = venue["verified_on"].strip()
    else:
        last_verified = dataset_date

    clean = {
        "vendor_id": f"PAN-{number:04d}",
        "vendor_name": value_or_na(venue["venue"]),
        "category": "Venue",
        "subcategory": value_or_na(venue["venue_type_norm"]),
        "city": value_or_na(venue["city"]),
        "service_area": value_or_na(venue["region"]),
        "price_min": price_min,
        "price_max": value_or_na(venue["per_plate_max_inr"]),
        "price_unit": price_unit,
        "starting_price": price_min,
        "rating": "NA",           # not in this dataset
        "review_count": "NA",     # not in this dataset
        "style_tags": get_style_tags(venue),
        "services": get_services(venue["rooms"]),
        "capacity_min": value_or_na(venue["capacity_min"]),
        "capacity_max": value_or_na(venue["capacity_max"]),
        "indoor_outdoor": "NA",   # not reliably known
        "source": "Panigrahana Venue Cost Registry 2026 (CC BY 4.0)",
        "source_url": source_url,
        "last_verified": last_verified,
        "data_confidence": get_confidence(venue["evidence_tier"]),
    }
    clean_venues.append(clean)

# 3. Save the clean file
with open(CLEAN_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(clean_venues)

print(f"Dataset version: {dataset_date}")
print(f"Saved {len(clean_venues)} venues to {CLEAN_FILE}")