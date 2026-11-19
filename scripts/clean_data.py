import os
import unicodedata
import pandas as pd

met = pd.read_csv("data/MetObjects.csv", dtype=str, encoding="utf-8-sig").rename(columns={
    "Artist Display Name": "name", "Artist Nationality": "nationality", "Artist Gender": "gender",
    "Artist Begin Date": "birth_year", "Artist End Date": "death_year",
    "Artist Wikidata URL": "wikidata", "Artist ULAN URL": "ulan"})
moma = pd.read_csv("data/Artists.csv", dtype=str, encoding="utf-8-sig").rename(columns={
    "DisplayName": "name", "Nationality": "nationality", "Gender": "gender",
    "BeginDate": "birth_year", "EndDate": "death_year", "Wiki QID": "wikidata", "ULAN": "ulan"})
nga = pd.read_csv("data/constituents.csv", dtype=str).rename(columns={
    "forwarddisplayname": "name", "beginyear": "birth_year", "endyear": "death_year",
    "wikidataid": "wikidata", "ulanid": "ulan"})

FIELDS = ["name", "nationality", "gender", "birth_year", "death_year", "wikidata", "ulan"]

met = met[FIELDS].dropna(subset=["name"]).fillna("")
met = met.apply(lambda col: col.str.split("|")).explode(FIELDS)
nga = nga[(nga["artistofngaobject"] == "1") & (nga["constituenttype"] == "individual")]
nga["gender"] = None

met["museum"], moma["museum"], nga["museum"] = "Met", "MoMA", "NGA"
df = pd.concat([met, moma, nga])[["museum"] + FIELDS]
df[FIELDS] = df[FIELDS].apply(lambda col: col.str.strip()).replace("", None)
df["wikidata"] = df["wikidata"].str.extract(r"(Q\d+)$", expand=False)
df["ulan"] = df["ulan"].str.extract(r"(\d{9})$", expand=False)

for col in ["birth_year", "death_year"]:
    df[col] = pd.to_numeric(df[col].str.extract(r"^(-?\d+)", expand=False))
    df[col] = df[col].replace([0, 9999], None)

bad_dates = (df["death_year"] < df["birth_year"]) | (df["death_year"] - df["birth_year"] > 110)
df.loc[bad_dates, ["birth_year", "death_year"]] = None
df[["birth_year", "death_year"]] = df[["birth_year", "death_year"]].astype("Int64")
df["gender"] = df["gender"].str.lower()
df["nationality"] = df["nationality"].replace("Nationality unknown", None).str.split(",").str[0]

def simplify(name):
    name = unicodedata.normalize("NFKD", name.split("(")[0]).encode("ascii", "ignore").decode()
    return " ".join("".join(c if c.isalnum() else " " for c in name.lower()).split())

df["name_simple"] = df["name"].fillna("").apply(simplify)

unknown = df["name_simple"].str.contains(r"\b(?:anonymous|unknown|workshop|school|circle of|follower)\b")
df = df[~unknown & (df["name_simple"] != "")]
df = df.sort_values(["wikidata", "ulan"]).drop_duplicates(["museum", "name_simple", "birth_year", "death_year"])

os.makedirs("clean", exist_ok=True)
df.to_csv("clean/artists_clean.csv", index=False)

#Quality check
quality = (df.groupby("museum")[FIELDS].apply(lambda d: d.notna().mean() * 100).round(1)).T
quality.loc["number_of_artists"] = df["museum"].value_counts()

# Accuracy:
guessed = (df["birth_year"] % 100 == 0) & (df["death_year"] - df["birth_year"] == 100)
quality.loc["guessed_dates"] = df[guessed]["museum"].value_counts()
print(quality.fillna(0))
os.makedirs("results", exist_ok=True)
quality.fillna(0).to_csv("results/quality_report.csv")

# Consistency:
shared = df.dropna(subset=["wikidata"]).groupby("wikidata").filter(lambda g: g["museum"].nunique() > 1)
print(f"\nArtists in more than one museum: {shared['wikidata'].nunique():,}")
for col in ["birth_year", "death_year", "nationality"]:
    disagree = (shared.dropna(subset=[col]).groupby("wikidata")[col].nunique() > 1).mean() * 100
    print(f"  Museums disagree on {col}: {disagree:.1f}%")