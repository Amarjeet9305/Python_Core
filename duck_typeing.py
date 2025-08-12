class TextEditor:
    def execute(self):
        print("Running editor")

class IDE:
    def execute(self):
        print("Compiling and Running code")

def code_run(software):
    software.execute()

code_run(TextEditor())
code_run(IDE())
