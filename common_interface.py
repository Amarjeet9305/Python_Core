class PDF:
    def open(self):
        print("Opening PDF file")

class Word:
    def open(self):
        print("Opening Word file")

def open_file(file):
    file.open()

open_file(PDF())
open_file(Word())
