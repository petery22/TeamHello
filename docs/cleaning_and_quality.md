# Data Cleaning and Quality Assessment

`scripts/clean_data.py` cleans the three museum datasets and combines them into one file (`clean/artists_clean.csv`). It then checks the quality of the result. Run it after `download_data.py`:

`python scripts/clean_data.py`

## Cleaning Steps

| Problem | What we did |
|---|---|
| Met lists several artists in one cell (`A\|B`) | Split into one row per artist |
| NGA includes donors, companies, and funds | Kept only individual artists |
| Met stores IDs as full web links | Kept just the ID (e.g. `Q5598`), same as MoMA and NGA |
| Invalid IDs, like the Met's "(not assigned)" | Made blank |
| Some Met dates are full dates (`1938-05-20`) | Kept the year only |
| MoMA uses `0` and the Met uses `9999` for unknown years | Made blank |
| Impossible dates (death before birth, or over 110 years apart) | Made blank |
| Met nationality has extra detail ("American, born Hungary") | Kept the first part ("American") |
| Names are written differently across museums | Added a simplified name for matching: lowercase, no accents or punctuation ("Rembrandt (Rembrandt van Rijn)" becomes "rembrandt") |
| Anonymous, unknown, and workshop records | Removed because they aren't one identifiable person |
| Duplicate records | Removed records in the same museum with the same name and birth and death years |

## Quality Assessment

**Completeness:** percent of artists with each field filled in, after cleaning.

| | Met | MoMA | NGA |
|---|---:|---:|---:|
| Number of artists | 62,571 | 15,949 | 15,989 |
| Nationality | 85% | 84% | 98% |
| Gender | 4% | 80% | 0% |
| Birth year | 75% | 79% | 88% |
| Death year | 69% | 38% | 76% |
| Wikidata ID | 33% | 20% | 57% |
| ULAN ID | 26% | 18% | 51% |

NGA is the most complete. MoMA has the fewest IDs, which means its artists will mostly be matched by name. Only MoMA has usable gender data.

**Accuracy:** About 3,100 Met artists have guessed dates, such as 1800 to 1900. NGA also stores wide guesses for artists only known by when they were active ("active 1827" is stored as 1747 to 1887), which the cleaning removes. Some IDs are wrong: MoMA gives Dorothea Lange and Russell Lee the same Wikidata ID.

**Consistency:** 6,145 artists appear in more than one museum. The museums disagree on birth year for 12% of them, death year for 9%, and nationality for 7%. Many date differences are about five years apart for older artists, where the exact year is unknown.

**Timeliness:** The data is current, but it changes often. NGA updates daily and the Met and MoMA weekly, so downloading again later will give different files slightly, and the checksums in `download_data.py` will stop matching. The team should keep a copy of the exact files used.