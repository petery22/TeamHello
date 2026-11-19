#Contribution Summary: Andy McCann

For this milestone in our project, I was responsible for acquiring the data, verifying it, and assessing how complete it is.

1. Data acquisition: Wrote scripts/download_data.py, which downloads the Met, MoMA, and NGA artist datasets from each museum's GitHub repository.
2. Checksum verification: the download script checks each file against a sha-256 checksum to make sure the we are all using the same version of the data.
3. Documentation: Wrote docs/data_documentation.md, which records each dataset's source, license, size, checksum, and any known issues. Pretty much just documents everything that was done and found.
4. Completeness assessment: Wrote scripts/assess_data.py to measure how complete each museum's artist records are and how many artists have Wikidata or ULAN Ids.

#Important findings after the completeness assessment:
1. NGA had the best ID coverage with 65.6% of the artists having a Wikidata or ULAN Id, compared to the Met (35.6%) and MoMA (20.4%). This means that name-based matching will be very important in this project.
2. Only MoMA has usable gender data due to NGA having 0% and the Met only having 4.4%.
3. The Met has artist ID data that is unreliable due to the fact that the same ID is sometimes used for different artists. They are currently counted by name instead.

#Next steps for me in this project
Help peter measure the overlap between the museums and eventually build the automated workflow for the final report.