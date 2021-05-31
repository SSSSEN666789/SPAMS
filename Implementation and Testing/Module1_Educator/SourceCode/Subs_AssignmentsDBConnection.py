from Key_Objects import Assignment

class AssignmentsDBConnection:
    
    ### Methods
    def getAssignment(self, parsed):
        assignmentID = parsed['assignment']

        print("AssignmentsDBConnection: Trying to find " + assignmentID)

        #DB에서 ID 기반으로 탐색해서 결과 반환
        ## 디버깅용 코드 ##

        if assignmentID == '0000':
            print("AssignmentsDBConnection: Fail to find " + assignmentID)
            return 'Cannot find \''+ assignmentID +'\' in Assignment DB'
        else:
            print("AssignmentsDBConnection: Success to find " + assignmentID)
            return Assignment('getAssignment 결과물: ID = ' + assignmentID)

    def getAssignmentList(self, parsed):
        classID = parsed['class']

        print("AssignmentsDBConnection: Trying to find assignments of Class" + classID)

        #DB에서 ID 기반으로 탐색해서 결과 반환
        ## 디버깅용 코드 ##
        if classID == '0000':
            print("AssignmentsDBConnection: There is no class \'" + classID + "\'")
            return "there is no class \'" + classID + "\'"
        elif classID == '9999':
            print("AssignmentsDBConnection: Class" + classID + "has no assignments")
            return 'class \'' + classID + "\' has no assignments"
        else:
            print("AssignmentsDBConnection: Success to find Class" + classID)
            print("AssignmentsDBConnection: Making assignment list of Class" + classID)
            res = [Assignment('getAssignmentList1'), Assignment('getAssignmentList2'), Assignment('getAssignmentList3')]
            return res
        
    def postAssignment(self, kA):
        ##DB에 저장
        print("AssignmentsDBConnection: Assignment \'" + kA.title + "\' is saved to Assignment DB.")
        return True

    def modifyAssignment(self, parsed):
        kA = self.getAssignment(parsed)

        #parsed의 내용대로 수정

        if type(kA) == type(''): return kA
        else:
            print("AssignmentsDBConnection: Assignment \'" + kA.title + "\' is modified.")
            return kA


    ### Subscribing Events

    def event_AssignmentEditorModify(self, parsed):
        return ('AssignmentsDBConnection', self.getAssignment(parsed))

    def event_AssignmentList(self, parsed):
        return ('AssignmentsDBConnection', self.getAssignmentList(parsed))

    def event_AssignmentCont(self, parsed):
        return ('AssignmentsDBConnection', self.getAssignment(parsed)) 

    def event_AssignmentCreated(self, kA):
        return ('AssignmentsDBConnection', self.postAssignment(kA)) 

    def event_ModifyAssignmentObject(self, parsed):
        return ('AssignmentsDBConnection', self.modifyAssignment(parsed)) 