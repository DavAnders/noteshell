import cmd
from file_management import create_note, read_note, delete_note
from search import search_notes
from manage_markdown import convert_md_to_text

NOTES_DIRECTORY = "./notes"

class NoteShell(cmd.Cmd):
    intro = 'Welcome to NoteShell. Type help or ? to list commands.\n'
    prompt = '(NoteShell) '

    def do_new(self, filename):
        'Create a new note: NEW filename.md'
        if not filename.endswith('.md'):
            filename += '.md'
        
        lines = []
        
        print("Enter text for the note. Type 'END' on a new line to finish.")
        while True:
            line = input()
            if line == 'END':
                break
            lines.append(line)
        
        text = '\n'.join(lines)
        
        create_note(filename, text)
        print(f'Note created: {filename}')

    def do_read(self, filename):
        'Read a note: READ filename.md'
        if not filename.endswith('.md'):
            filename += '.md'
        try:
            content = read_note(filename)
            print(convert_md_to_text(content))
        except FileNotFoundError:
            print("Note does not exist.")

    def do_delete(self, filename):
        'Delete a note: DELETE filename.md'
        if not filename.endswith('.md'):
            filename += '.md'
        try:
            delete_note(filename)
            print(f'Note deleted: {filename}')
        except FileNotFoundError:
            print("Note does not exist.")

    def do_search(self, keyword):
        'Search for notes containing <keyword>'
        results = search_notes(keyword)
        if results:
            print("Found the following notes:")
            for note in results:
                print(note)
        else:
            print("No notes found with that keyword.")

    def do_exit(self, _):
        'Exit the application'
        print('Thank you for using NoteShell')
        return True  # This exits the cmd loop

if __name__ == '__main__':
    NoteShell().cmdloop()
