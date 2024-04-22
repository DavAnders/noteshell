import os

NOTES_DIRECTORY = "./notes"

def create_note(filename, content="# New Note\nEnter your markdown content here."):
    if not os.path.exists(NOTES_DIRECTORY):
        os.makedirs(NOTES_DIRECTORY)

    path = os.path.join(NOTES_DIRECTORY, filename)
    with open(path, 'w') as f:
        f.write(content)

def read_note(filename):
    path = os.path.join(NOTES_DIRECTORY, filename)
    with open(path, 'r') as f:
        return f.read()

def delete_note(filename):
    path = os.path.join(NOTES_DIRECTORY, filename)
    os.remove(path)
