import glob
import re

for fpath in glob.glob('*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all occurrences of entertainer_detail.html
    matches = re.findall(r'href=["\']entertainer_detail\.html(?:[?#][^"\']*)?["\']', content)
    bare = [m for m in matches if '?' not in m]
    if bare:
        print(f"{fpath} has {len(bare)} BARE links to entertainer_detail.html without ?id=:")
        for b in bare:
            print("  ", b)
