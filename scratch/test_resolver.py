import json
import re

with open('scratch/full_entertainers_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Add aliases
db["captain ray"] = db["captain_ray"]
db["captain leo"] = db["max"]
db["captain_leo"] = db["max"]
db["dj spark"] = db["dj_spark"]
db["the great z"] = db["the_great_z"]
db["princess lily"] = db["lily"]
db["princess aurora"] = db["aurora"]
db["elias thorne"] = db["elias"]
db["jojo the juggler"] = db["jojo"]
db["bubble_mia"] = db["mia"]

def resolve(param):
    if not param:
        return db['elias']
    clean = param.lower().strip()
    if clean in db:
        return db[clean]
    norm = re.sub(r'[^a-z0-9]', '', clean)
    if norm in db:
        return db[norm]
    for k, v in db.items():
        knorm = re.sub(r'[^a-z0-9]', '', k)
        if knorm == norm or knorm in norm or norm in knorm:
            return v
    for k, v in db.items():
        nameNorm = re.sub(r'[^a-z0-9]', '', v['name'].lower())
        if nameNorm in norm or norm in nameNorm:
            return v
    return db['elias']

# Test all links from entertainers.html
with open('entertainers.html', 'r', encoding='utf-8') as f:
    econtent = f.read()

links = re.findall(r'href="entertainer_detail\.html\?id=([^"]+)"', econtent)
print(f"Testing {len(links)} links from entertainers.html:")
for l in links:
    res = resolve(l)
    print(f"  ID: {l:<15} -> Name: {res['name']:<25} | Img: {res['img']}")

# Test all links from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    icontent = f.read()

ilinks = re.findall(r'href="entertainer_detail\.html\?id=([^"]+)"', icontent)
print(f"\nTesting {len(ilinks)} links from index.html:")
for l in ilinks:
    res = resolve(l)
    print(f"  ID: {l:<15} -> Name: {res['name']:<25} | Img: {res['img']}")
