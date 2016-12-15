import os

excluded_files = [
    '.DS_Store',
    'LICENSE',
    'README.md',
]

for root, dirs, files in os.walk("."):
    if '.git' not in root:
        for filename in files:
            if filename not in excluded_files:
                path = os.path.join(root, filename)
                print(path[2:])
