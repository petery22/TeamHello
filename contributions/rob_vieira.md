# Contribution Summary: Rob Vieira

For this milestone, my responsibilites included cleaning the data from all three museums and assessing its quality.

1. **Normalization:** Wrote `scripts/clean_data.py`. This gives all three datasets the same column names and formats. It pulls just the ID out of the Met's Wikidata and ULAN web links so they match MoMA and NGA, keeps only the year from dates, and creates a simplified version of each artist's name to use for matching. This version is in lowercase and there are no accents or punctuation.
2. **Missing, inconsistent, and duplicate records:** The script turns placeholder values (MoMA's `0` years, the Met's `9999` years and "(not assigned)" IDs) into true blanks and removes impossible dates. It also drops anonymous, unknown, and workshop records along with removing duplicates. For example, the Met listed Rembrandt once per artwork, which was 505 rows. The cleaning reduced to one record per museum.
3. **Quality assessment:** The script measures completeness, accuracy, and consistency, and saves the results to `results/quality_report.csv`. The cleaned data is saved to `clean/artists_clean.csv` for the matching step.
4. **Documentation:** Wrote `docs/cleaning_and_quality.md`. This explains each cleaning step and the quality findings including timeliness.

**Key findings:**
- 6,145 artists appear in more than one museum. The museums disagree on birth year for 12% of them, death year for 9%, and nationality for 7%.
- About 3,100 Met artists have guessed dates, such as 1800 to 1900. Some Wikidata IDs are also assigned to the wrong person.
- The data updates often (NGA updates daily and the Met/MoMA update weekly), so the team needs to keep a copy of the exact files used.

**Next steps:** Help Peter match artists across the museums using the cleaned data.