import os
import pandas as pd

#rename each musuem's columns so they have same names
met = pd.read_csv("data/MetObjects.csv", dtype = str, encoding="utf-8-sig").rename(columns={
    "Artist Display Name": "name", "Artist Nationality": "nationality", "Artist Gender": "gender",
    "Artist Begin Date": "birth_year", "Artist End Date": "death_year",
    "Artist Wikidata URL": "wikidata", "Artist ULAN URL": "ulan"})

moma = pd.read_csv("data/Artists.csv", dtype=str, encoding="utf-8-sig").rename(columns={
    "DisplayName": "name", "Nationality": "nationality", "Gender": "gender",
    "BeginDate": "birth_year", "EndDate": "death_year", "Wiki QID": "wikidata", "ULAN": "ulan"})

nga = pd.read_csv("data/constituents.csv", dtype=str).rename(columns={
    "forwarddisplayname": "name", "beginyear": "birth_year", "endyear": "death_year",
    "wikidataid": "wikidata", "ulanid": "ulan"})

fields = ['name', 'nationality', 'gender', 'birth_year', 'death_year', 'wikidata', 'ulan']

#Met currently has one row per artwork. Artworks with several artists are split by "|"
#so this is splitting them into one row per artist, keeping one row per artist name

met = met[fields].dropna(subset=['name']).fillna("")
met = met.apply(lambda col: col.str.split("|")).explode(fields)
met = met.apply(lambda col: col.str.strip()).replace("", None)
met = met.drop_duplicates(subset='name')

#replacing the 0s and nationality unknown in MoMA and making them blank
moma = moma.replace({'birth_year': '0', 'death_year': '0', 'nationality': "Nationality unknown"}, None)

#keeping only individual artists in NGA
nga = nga[(nga['artistofngaobject']== "1") & (nga['constituenttype']=='individual')]
nga['gender'] = None

#percent of artists with each field
results = pd.DataFrame()
for museum, df in [("Met", met), ('MoMA', moma), ("NGA", nga)]:
    results[museum] = (df[fields].notna().mean() * 100).round(1)
    results.loc['has_either_id', museum] = round((df['wikidata'].notna() | df['ulan'].notna()).mean()*100,1)
    results.loc['number_of_artists', museum] = len(df)

print(results)
os.makedirs('results', exist_ok = True)
results.to_csv('results/completeness.csv')