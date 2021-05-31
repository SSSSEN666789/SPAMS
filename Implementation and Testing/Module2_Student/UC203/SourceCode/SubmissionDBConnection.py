from Key_Objects import Submission
import string
from PageMaker import PageMaker


class SubmissionsDBConnection:

    # Methods

    def getSubRes(self , subID):

        f= open('SubmissionDB.txt', 'r')

        lines = [] # list

        for paragraph in f: # 제출물 ID를 검색하여 해당하는 줄을 파서로 넘김
            lines = paragraph.split("/")
            for each_line in lines:
                if subID in each_line:
                    return each_line

                else: PageMaker.renderWarningPage()


