import re
import os

NOTES_DIRECTORY = "./notes"

def search_notes(keyword):
    results = []
    for filename in os.listdir(NOTES_DIRECTORY):
        if filename.endswith('.md'):
            file_path = os.path.join(NOTES_DIRECTORY, filename)
            with open(file_path, 'r') as f:
                contents = f.read()
                if re.search(keyword, contents):
                    results.append(filename)
    return results