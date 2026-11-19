import hashlib
import os
import requests

#file name with the download link and expected sha-256 checksum
Datasets = {
    "MetObjects.csv": (
        "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv",
        "f53eb3bd6e321a051ce11ad40bd7f5ee204c6c534cb07508f0f617d03bea0d3a",
    ),
    "Artists.csv": (
        "https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/Artists.csv",
        "88df2b9198b829994fbdd26aa1bf7f15f46cafe3244ac6098412ac606b281cdb",
    ),
    "constituents.csv": (
        "https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data/constituents.csv",
        "ee511c37f9d1b31ae985eb9d779a89754bf81966d1f0a380f1522a11545772ba",
    ),
}

os.makedirs('data', exist_ok=True)

for name, (url, expected) in Datasets.items():
    path = os.path.join ("data", name)

    if not os.path.exists(path):
        print(f"Downloading {name}...")
        with requests.get(url, stream = True) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024*1024):
                    f.write(chunk)

    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            sha.update(chunk)
    
    if sha.hexdigest() == expected:
        print(f"{name}: checksum OK")
    else:
        print(f"{name}: checksum DOES NOT MATCH (file may have been changed)")
        print(f"  got: {sha.hexdigest()}")