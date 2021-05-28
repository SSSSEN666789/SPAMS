class EventManager:

    def __init__(self):
        self.subs_WrongRequestWarning = []
        self.subs_AssignmentEditor = []
        self.subs_AssignmentList = []
        self.subs_AssignmentCont = []
        self.subs_CreateAssignmentObject = None # AssignmentMaker가 와야 함.
        self.subs_AassignmentCreated = []
        self.subs_ModifyAssignmentObject = None # AssignmentDBConnection이 와야 함.
        self.subs_AssignmentModified = []
        self.subs_SubCont = []
        self.subs_SubList = []

        self.pageMaker = None

    def set_pageMaker(self, pageMaker):
        self.pageMaker = pageMaker

    ### events
    
    def activate_event(self, validChkRes, params):

        if validChkRes != 'accepted':
            return self.event_WrongRequestWarning(validChkRes)

        request = params[0]
        parsed = params[1]

        if request == 'AssignmentEditor': self.event_AssignmentEditor(parsed)
        if request == 'AssignmentList': self.event_AssignmentList(parsed)
        if request == 'AssignmentContent': self.event_AssignmentCont(parsed)
        if request == 'RegisterAssignment': self.event_CreateAssignmentObject(parsed)
        if request == 'ModifyAssignment': self.event_ModifyAssignmentObject(parsed)
        if request == 'SubmissionList': self.event_SubList(parsed)
        if request == 'SubmissionContent': self.event_SubCont(parsed)
       
    def event_WrongRequestWarning(self, warning_msg):
        for i in range(len(self.subs_WrongRequestWarning)):
            self.subs_WrongRequestWarning[i].event_WrongRequestWarning(warning_msg)
        return self.pageMaker.event_WrongRequestWarning(warning_msg)

    def event_AssignmentEditor(self, parsed):
        for i in range(len(self.subs_AssignmentEditor)):
            self.subs_AssignmentEditor[i].event_AssignmentEditor(parsed)
        return self.pageMaker.event_AssignmentEditor(parsed)

    def event_AssignmentList(self, parsed):
        for i in range(len(self.subs_AssignmentList)):
            self.subs_AssignmentList[i].event_AssignmentList(parsed)
        return self.pageMaker.event_AssignmentList(parsed)

    def event_AssignmentCont(self, parsed):
        for i in range(len(self.subs_AssignmentCont)):
            self.subs_AssignmentCont[i].event_AssignmentCont(parsed)
        return self.pageMaker.event_AssignmentCont(parsed)

    def event_CreateAssignmentObject(self, parsed):
        kA = self.subs_CreateAssignmentObject.event_CreateAssignmentObject(parsed)
        return self.event_AssignmentCreated(kA)

    def event_AssignmentCreated(self, kA):
        for i in range(len(self.subs_AssignmentCreated)):
            self.subs_AssignmentCreated[i].event_AssignmentCreated(kA)
        return self.pageMaker.event_AssignmentCreated(kA)

    def event_ModifyAssignmentObject(self, parsed):
        kA = self.subs_ModifyAssignmentObject.event_ModifyAssignmentObject(parsed)
        return self.event_AssignmentModified(kA)

    def event_AssignmentModified(self, kA):
        for i in range(len(self.subs_AssignmentModified)):
            self.subs_AssignmentModified[i].event_AssignmentModified(kA)
        return self.pageMaker.event_AssignmentModified(kA)

    def event_SubCont(self, parsed):
        for i in range(len(self.subs_SubCont)):
            self.subs_SubCont[i].event_SubCont(parsed)
        return self.pageMaker.event_SubCont(parsed)

    def event_SubList(self, parsed):
        for i in range(len(self.subs_SubList)):
            self.subs_SubList[i].event_SubList(parsed)
        return self.pageMaker.event_SubList(parsed)

    ### register
    
    def register_WrongRequestWarning(self, subs):
        if subs not in self.subs_WrongRequestWarning:
            self.subs_WrongRequestWarning.append(subs)

    def register_AssignmentEditor(self, subs):
        if subs not in self.subs_AssignmentEditor:
            self.subs_AssignmentEditor.append(subs)

    def register_AssignmentList(self, subs):
        if subs not in self.subs_AssignmentList:
            self.subs_AssignmentList.append(subs)

    def register_AssignmentCont(self, subs):
        if subs not in self.subs_AssignmentCont:
            self.subs_AssignmentCont.append(subs)

    def register_CreateAssignmentObject(self, subs):
        self.subs_CreateAssignmentObject = subs

    def register_AssignmentCreated(self, subs):
        if subs not in self.subs_AssignmentCreated:
            self.subs_AssignmentCreated.append(subs)

    def register_ModifyAssignmentObject(self, subs):
        self.subs_ModifyAssignmentObject = subs

    def register_AssignmentModified(self, subs):
        if subs not in self.subs_AssignmentModified:
            self.subs_AssignmentModified.append(subs)

    def register_SubCont(self, subs):
        if subs not in self.subs_SubCont:
            self.subs_SubCont.append(subs)

    def register_SubList(self, subs):
        if subs not in self.subs_SubList:
            self.subs_SubList.append(subs)
    
    ### unregister
    def unregister_WrongRequestWarning(self, subs):
        if subs in self.subs_WrongRequestWarning:
            self.subs_WrongRequestWarning.pop(subs)

    def unregister_AssignmentEditor(self, subs):
        if subs in self.subs_AssignmentEditor:
            self.subs_AssignmentEditor.pop(subs)

    def unregister_AssignmentList(self, subs):
        if subs in self.subs_AssignmentList:
            self.subs_AssignmentList.pop(subs)

    def unregister_AssignmentCont(self, subs):
        if subs in self.subs_AssignmentCont:
            self.subs_AssignmentCont.pop(subs)

    def unregister_CreateAssignmentObject(self, subs):
        if subs is self.subs_CreateAssignmentObject:
            self.subs_CreateAssignmentObject = None

    def unregister_AssignmentCreated(self, subs):
        if subs in self.subs_AssignmentCreated:
            self.subs_AssignmentCreated.pop(subs)

    def unregister_ModifyAssignmentObject(self, subs):
        if subs is self.subs_ModifyAssignmentObject:
            self.subs_ModifyAssignmentObject = None

    def unregister_AssignmentModified(self, subs):
        if subs in self.subs_AssignmentModified:
            self.subs_AssignmentModified.pop(subs)

    def unregister_SubCont(self, subs):
        if subs in self.subs_SubCont:
            self.subs_SubCont.pop(subs)

    def unregister_SubList(self, subs):
        if subs in self.subs_SubList:
            self.subs_SubList.pop(subs)

    