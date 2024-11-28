from note import Note

class Notebook:
    '''
    Une liste de notes
    '''
    def __init__(self):
        self.notes = []

    def ajouter_note(self, memo, balises):
        self.notes.append(Note(memo, balises))

    def modifier_note(self, id, memo=None, balises=None):
        for note in self.notes:
            if note.note_id == id:
                if memo:
                    note.memo = memo
                if balises:
                    note.balises = balises
                break