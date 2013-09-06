#!/usr/bin/python3

import os
from tkinter import *

def_font=[ "DejaVuSansMono", 11 ]

class xmlview():
    def __init__(self, txt_wig, string=None):
        self.txtwig=txt_wig
        self.txtwig.tag_config("tags", foreground="purple")
        self.txtwig.tag_config("bold", font=[ def_font[0], def_font[1], "bold"])
        if string: self.parser(string)

    def de_code(self, code, b, e):
        beg=str(b[0])+'.'+str(b[1])
        end=str(e[0])+'.'+str(e[1])
        self.txtwig.tag_add(code, beg, end)

    def parser(self, string):
        self.txtwig.delete('1.0', END)
        beg=end=[0, 0]
        j=1; i=0
        for char in string:
            self.txtwig.insert(END, char)
            if char=='<':
                beg=[j, i+1]
                end[1]+=1
                self.de_code("bold", end, [j, i])
            if char==">":
                end=[j, i]
                self.de_code("tags", beg, end)

            if char=='\n': j+=1; i=-1;
            i+=1

if __name__ == "__main__" :
    if len(sys.argv)<2:
        print("Argument(s) Missing", file=sys.stderr); exit(1);
    root=Tk()
    text=Text(root, font=def_font)
    string=open(sys.argv[1]).read()
    xview=xmlview(text, string)
    text.pack(expand=YES, fill=BOTH)
    root.bind('<Key-Escape>', lambda event: quit())
    root.mainloop()
