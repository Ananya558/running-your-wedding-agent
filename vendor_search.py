import vendor_database

# Our assumption: share of the total budget that goes to venue + food.
# Not from the dataset. Change this number to try other splits.
VENUE_FOOD_SHARE = 0.40


def search_vendors(vendors, city, category):
    """Return the vendors in a given city (or region) and category."""
    city = city.strip().lower()
    category = category.strip().lower()
    results = []

    for vendor in vendors:
        in_city = (vendor["city"].lower() == city
                   or vendor["service_area"].lower() == city)
        right_category = vendor["category"].lower() == category

        if in_city and right_category:
            results.append(vendor)

    return results


def filter_by_guests(vendors, guests):
    """Keep vendors whose known capacity can hold all the guests."""
    results = []

    for vendor in vendors:
        capacity = vendor["capacity_max"]
        if capacity is not None and capacity >= guests:
            results.append(vendor)

    return results


def filter_by_budget(vendors, guests, total_budget):
    """Keep vendors whose cheapest per-plate price fits the venue + food budget."""
    food_budget = total_budget * VENUE_FOOD_SHARE
    results = []

    for vendor in vendors:
        price = vendor["price_min"]
        if price is not None and price * guests <= food_budget:
            results.append(vendor)

    return results


def split_by_confidence(vendors):
    """Split vendors into two lists: high confidence and low confidence."""
    high = []
    low = []

    for vendor in vendors:
        if vendor["data_confidence"] == "high":
            high.append(vendor)
        else:
            low.append(vendor)

    return high, low


def show_results(vendors, guests, limit=5):
    """Print matches, with high-confidence vendors highlighted first."""
    high, low = split_by_confidence(vendors)

    print(f"\n⭐ RECOMMENDED: price is confirmed or published ({len(high)} venues)")
    for vendor in high[:limit]:
        food_cost = vendor["price_min"] * guests
        print(f"  ⭐ {vendor['vendor_name']}: ₹{vendor['price_min']:,}/plate "
              f"→ about ₹{food_cost:,} for food")

    print(f"\nOther options: price is only an estimate ({len(low)} venues)")
    for vendor in low[:limit]:
        food_cost = vendor["price_min"] * guests
        print(f"  -  {vendor['vendor_name']}: ₹{vendor['price_min']:,}/plate "
              f"→ about ₹{food_cost:,} for food (estimate)")


# Test: only runs when you run this file directly
if __name__ == "__main__":
    vendors = vendor_database.load_vendors()

    city = "Goa"
    guests = 250
    total_budget = 2500000  # ₹25 lakh

    step1 = search_vendors(vendors, city, "Venue")
    step2 = filter_by_guests(step1, guests)
    step3 = filter_by_budget(step2, guests, total_budget)

    print(f"Wedding: {city}, {guests} guests, budget ₹{total_budget:,}")
    print(f"Venue + food budget ({VENUE_FOOD_SHARE:.0%}): ₹{total_budget * VENUE_FOOD_SHARE:,.0f}")
    print(f"\nVenues in {city}:            {len(step1)}")
    print(f"...that fit {guests} guests:     {len(step2)}")
    print(f"...that fit the budget:      {len(step3)}")

    show_results(step3, guests)