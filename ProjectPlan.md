# Project Plan

## Overview

This project investigates the overlap of artist records across three of the major US museum collections: the Metropolitan Museum of Art (Met), the Museum of Modern Art (MoMA), and the National Gallery of Art (NGA). Each museum’s data is open-access and released under a CC0 license. While they are all relatively similar datasets, the way that they record data differ slightly. This includes things like artist identifiers and different date conventions. This project aims to analyze how many shared artists there are across museums and if any records are inconsistent.

Artist data will be acquired through each museum’s official GitHub repository (retrieved from the provided list of datasets) and verified with SHA-256 checksums. The datasets will be cleaned to address issues such as inconsistent identifiers, date conventions, and empty values. They will then be integrated by matching Wikidata and ULAN identifiers as well as matching their names (accounting for inconsistent naming conventions). Once the datasets are integrated, they will be analyzed for overlap or any potential disagreements.

## Team

**Andy McCann**
- Manage scripts for downloading the Met, MoMA, and NGA datasets.
- Implement SHA-256 checksum verification and document data sources, licenses, and metadata.
- Assess the dataset completeness and identifier coverage.

**Rob Vieira**
- Develop scripts to normalize artist names, Wikidata QIDs, ULAN identifiers, and date formats across the datasets.
- Identify missing, inconsistent, or duplicate records and address them.
- Perform data quality assessments. These will be focused on accuracy, completeness, consistency, and timeliness.
- Document cleaning methods and findings from the data quality assessments.

**Peter Youn**
- Develop matching and integration workflows using Wikidata IDs, ULAN IDs, and normalized artist names.
- Analyze the overlap of certain artists across the museums and measure the effectiveness of identifier-based versus name-based matching.
- Find inconsistencies between shared artist records and create visualizations that summarize the results of the findings.

**Shared Responsibilities**
- Making sure the project is documented correctly, GitHub repository is maintained, and our milestones are submitted on time.
- Reviewing other people’s work and making sure code and documentation is approved by all members.
- Test all the work start to finish to ensure reproducibility and that project requirements are met.

## Research Questions

- How many artists are represented in more than one of the three museum collections?
- What proportion of artists appear in all three museum datasets versus only one or two datasets?
- How effectively can artist records be matched across museums using Wikidata QIDs, ULAN identifiers, and normalized artist names?
- What inconsistencies exist between museums for shared artists? These could be differences like names, birth years, death years, nationality, or gender information.
- How complete are the artist records in each museum dataset, particularly for key metadata fields such as identifiers, nationality, gender, and life dates?
- Which museum provides the highest coverage of external identifiers such as Wikidata and ULAN IDs?
- How much more coverage can be achieved through name-based matching when identifier-based matching is unavailable?
- What data quality issues are most common across the three datasets, and how do these issues affect the success of dataset integration?

## Datasets

The three chosen datasets each have data on artists that have artwork in their respective museums. They are all published by the museums themselves on GitHub, and released under a CC0 public domain license.

### Dataset 1: Metropolitan Museum of Art

- Link: https://github.com/metmuseum/openaccess
- File Name: MetObjects.csv
- Size: 324 MB
- Relevant columns: Constituent ID, Artist Display Name, Artist Alpha Sort, Artist Nationality, Artist Begin Date, Artist End Date, Artist Gender, Artist ULAN URL, Artist Wikidata URL

The Met’s dataset is much bigger than the other two datasets we are using. This is because the dataset’s rows are all objects rather than artists, and have the artist’s information as features of each object. Before integration, we will have to create a separate table just for artists. Unlike the other two datasets, the IDs we want to use to integrate the tables (Wikidata and ULAN) are stored as URLs rather than the actual IDs. This dataset contributes to the project by having the largest collection that spans thousands of years.

### Dataset 2: Museum of Modern Art

- Link: https://github.com/MuseumofModernArt/collection
- File Name: Artists.csv
- Size: 1.01 MB
- Relevant columns: ConstituentID, DisplayName, Nationality, Gender, BeginDate, EndDate, Wiki QID, ULAN

MoMA’s dataset contains one row per artist, and the artist is identified by ConstituentID. Many unknown dates (BeginDate and EndDate) are stored as 0, which could pose problems during analysis if not addressed. This dataset contributes because it has a focus on modern and contemporary art, and it also has the most complete gender data.

### Dataset 3: National Gallery of Art

- Link: https://github.com/NationalGalleryOfArt/opendata
- File Name: constituents.csv
- Size: 4.28 MB
- Relevant columns: constituentid, preferreddisplayname, forwarddisplayname, lastname, displaydate, beginyear, endyear, nationality, constituenttype, artistofngaobject, ulanid, wikidataid

NGA’s dataset contains records for anyone associated with a piece of art in their museum. This includes donors, couples, anonymous entries, corporations, and more. Using the artistofngaobject column, we can view the artist of the object. This dataset contributes to the project by having a European and American focus, as well as having the best coverage for identifiers to match with the other datasets.

## Dataset Integration

The three datasets can be integrated by artist. Despite being in all three datasets under the same name, the constituent ID should not be used as they are independent for each museum, so they should not match. We will use the ULAN ID and Wikidata QID. The datasets store these values differently (the Met uses full URLs while MoMA and NGA uses just the ID), so they will be normalized during cleaning. For artists that don’t have identifiers recorded in the datasets, we will normalize and use their names to match them, as well as make sure birth and death years are consistent.

## Timeline

1. Download the data (by early November)
    - Andy: Download all three datasets with SHA-256 checks, store the Met file on Box, and record sources and licenses.
2. Check quality and clean (by mid-November)
    - Rob: Assess data quality and clean IDs, names, dates, and non-artist records.
3. Status report (Nov 19)
    - Everyone
4. Merge the datasets (by end of November)
    - Peter: Match artists by ULAN ID, Wikidata ID, then name plus birth and death years.
5. Analyze and automate (by early December)
    - Peter and Andy: Measures overlap and disagreements.
    - Andy: Build the automated workflow and documentation.
6. Final report and release (Dec 8)
    - Everyone

## Constraints

- The met file of 324MB is too big for GitHub as a single file, so it has to be stored in Box.
- Many artists have no ULAN or Wikidata ID, so some matches rely on solely names, which can end up being wrong due to the nature of people having the same names or names being spelled differently.
- The museums format dates, IDs, and labels differently, and NGA includes non-artists like donors and anonymous entries.
- All data is CC0, so no legal limits, however gender and nationality labels came from museum staff and could be judged wrong and be inaccurate.

## Gaps

- Need to figure out how strict name matching should be.
- We have to figure out if we want to keep or remove workshops and unknown artists as all three datasets have them.
- We have to also figure out if we want to clean the data in Python or OpenRefine as we were given the option to choose in the instructions.
