from Key_Objects import Submission

class SubmissionsDBConnection:

    ### Methods

     ### Methods
    def getSubCont(self, parsed):
        submissionID = parsed['submission']

        print("SubmissionsDBConnection: Trying to find " + submissionID)

        #DB에서 ID 기반으로 탐색해서 결과 반환
        ## 디버깅용 코드 ##

        if submissionID == '0000':
            print("SubmissiontsDBConnection: Fail to find " + submissionID)
            return 'Cannot find \''+ submissionID +'\' in Submission DB'
        else:
            print("SubmissiontsDBConnection: Success to find " + submissionID)
            return Submission('getSubmission 결과물: ID = ' + submissionID)

    def getSubList(self, parsed):
        assignmentID = parsed['assignment']

        print("SubmissiontsDBConnection: Trying to find submissionss of assignment" + assignmentID)

        #DB에서 ID 기반으로 탐색해서 결과 반환
        ## 디버깅용 코드 ##
        if assignmentID == '0000':
            print("SubmissiontsDBConnection: There is no assignment \'" + assignmentID + "\'")
            return "there is no assignment \'" + assignmentID + "\'"
        elif assignmentID == '9999':
            print("SubmissiontsDBConnection: Assignment" + assignmentID + "has no submissions")
            return 'assignment \'' + assignmentID + "\' has no submissions"
        else:
            print("SubmissiontsDBConnection: Success to find Assignment" + assignmentID)
            print("SubmissiontsDBConnection: Making submission list of Assignment" + assignmentID)
            res = [Submission('getSubmissionList1'), Submission('getSubmissionList2'), Submission('getSubmissionList3'), Submission('getSubmissionList4')]
            return res

    ### Subscribing Events

    def event_SubCont(self, parsed):
        return ('SubmissionsDBConnection', self.getSubCont(parsed))

    def event_SubList(self, parsed):
        return ('SubmissionsDBConnection', self.getSubList(parsed)) 