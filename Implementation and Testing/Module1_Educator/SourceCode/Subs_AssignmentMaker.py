from Key_Objects import Assignment

class AssignmentMaker:

    ### Methods

    def createAssignment(self, parsed):
        res = Assignment(parsed['title'])
        print("AssignmentMaker: Created New Assignment")
        print("->title: " + res.title)
        return res

    ### Subscribing Events

    def event_CreateAssignmentObject(self, parsed):
        return ('AssignmentMaker', self.createAssignment(parsed))