# running-your-wedding-agent
## Data sources

### Wedding venues — Panigrahana

`data/panigrahana_venues_raw.csv` is the **Wedding Venue Cost Registry 2026**
by [Panigrahana](https://panigrahana.com/wedding-data.html) (version generated 2026-09-27),
licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Changes we made** (see `clean_venues.py`) to create `data/vendors.csv`:

- Kept only venues in India (891 of 992 rows)
- Converted columns into this project's vendor schema
- Marked missing information as `NA` instead of guessing it
- Added `data_confidence` (high / medium / low), based on Panigrahana's evidence tier
- Added `style_tags`. **These are our own inference** from venue type, star rating,
  region and capacity, not part of the original data.

Many prices in the original dataset come from public wedding listing sites, as recorded
in Panigrahana's evidence tiers and source links.