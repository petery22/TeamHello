# Data Documentation

This project uses artist data from three museums:
1. Metropolitan Musuem of Art (Met)
2. Museum of Modern Art (MoMA)
3. National Gallery of Art (NGA)

# The Datasets
|""| Met | MoMA | NGA
|File| MetObjects.csv | Artists.csv | constituents.csv |
|Source| [metmuseum/openaccess](https://github.com/metmuseum/openaccess) | [MuseumofModernArt/collection](https://github.com/MuseumofModernArt/collection) | [NationalGalleryOfArt/opendata](https://github.com/NationalGalleryOfArt/opendata) |
|License| CC0 (public doman) | CC0 (public domain) | CC0 (public domain) |
|Size| 341 MB | 1.1 MB | 4.5 MB |
|Each row| One artwork | One artist | One person or group linked to artwork |
*Since CC0 means the data is public domain, we are edit it freely without needing permission

# How to get the data

From the main project folder, run this:
1. pip install pandas requests
2. python scripts/download_data.py (downloads the three files into the data/ folder and checks them all)
3. python scripts/assess_data.py (measures the completeness of the datasets and saves the results to results/completeness.csv)

*The data/ folder can not be uploaded to Github because the Met file is too large. So, running download_data.py downloads all three files directly from the museums

*Checksums: the download script checks each file against the sha-256 checksums below to make sure it is the same version that we used.

| File | sha-256 checksum |
| MetObjects.csv | f53eb3bd6e321a051ce11ad40bd7f5ee204c6c534cb07508f0f617d03bea0d3a |
| Artists.csv | 88df2b9198b829994fbdd26aa1bf7f15f46cafe3244ac6098412ac606b281cdb |
| constituents.csv | ee511c37f9d1b31ae985eb9d779a89754bf81966d1f0a380f1522a11545772ba |

# Results from Completeness
This is the table that shows up in the completeness file in results which shows the percent of artists in each museum that have each piece of info. For NGA, only individual artist were counted, not donors or companies.

| "" | Met | MoMA | NGA |
| Number of artists | 62487 | 16018 | 16003 |
| Name | 100% | 100% | 100% |
| Nationality | 84.3% | 83.7% | 98.2% |
| Gender | 4.4% | 79.4% | 0% |
| Birth year | 76.1% | 78.4% | 95.3% |
| Death year | 76.2% | 37.3% | 83.2% |
| Wikidata ID | 32.9% | 20.3% | 56.9% |
| ULAN ID | 35.1% | 18.3% | 51.1% |
| Has at least one ID | 35.6% | 20.4% | 65.6% |

What does this exactly mean:
1. NGA has the best ID coverage with 65.6% and MoMA has the worst with only 20.4%. Since most artists in every museum have no ID, many of the matches between the museums will have to found through names and dates.
2. Only MoMA has usable gender data because NGA does not record gender and the Met only records "females", leaving things incomplete.
3. MoMA has a low death year because most of the artists are most likely still alive.

# What to address specifically in cleaning
1. The same artist ID is sometimes used in the Met's data if a certain artwork had several artists. Met artists right now are counted by name instead.
2. The Met lists several artist in one cell
3. The Met stores IDs as web links, instead of just a numbered ID
4. MoMA records unknown years as 0 instead of leaving them blank. The completeness check treats these as missing, but they still need to be fixed in the cleaned data
5. Some Met dates are simple placeholders using very old dates
6. NGA includes non-artists like donors and companies