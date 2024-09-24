import PyPDF2
import os
from os import path
import bok


class bibliotek:
    def __init__(self,titles, num, topic):
        self.titles = titles
        self.num = num
        self.topic = topic

    def create_bok(self):
        self.doc_dir =path.join(path.dirname(__file__), 'pdf_docs') ###place to save input documnets.
        self.file_list = os.listdir(self.doc_dir)
        print(str(self.file_list))
        pass
    def doc_pos(self):
        pass
    
    
        
        
    