from SubmissionDBConnection import SubmissionsDBConnection
import string


class ResultParser:

    def parseRequest(self, result):
        my_dict = {}
        subResult = []

        result = result.split(':')
        result = [i.strip() for i in result]

        my_dict['Submission ID'] = result[0]
        my_dict['Result'] = result[1]
        my_dict['Message'] = result[2]
        my_dict['Runtime(sec)'] = result[3]

        subResult.append(my_dict)

        return subResult
