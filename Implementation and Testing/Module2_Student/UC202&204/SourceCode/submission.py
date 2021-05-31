from tkinter.constants import NUMERIC
import quizfile


class Submission:
    def __init__(self):
        """
        self.s_name
        self.student_name
        self.anum
        self.s_title
        """
    
    def student_name(self, s_name):
        self.s_name = s_name
        return self.s_name

    def student_ID(self, snum):
        self.snum = snum
        return self.snum

    def Submission_ID(self, anum):
        self.anum = anum
        return self.anum

    def title(self, s_title):
        self.s_title = s_title
        return self.s_title

    def file_name(self, filename):
        self.filename = filename
        return self.filename
