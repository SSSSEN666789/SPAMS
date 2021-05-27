class EventManager:

    def __init__(self):
        self.subs_wrongRequestWarning = []
        self.subs_createAssignmentEditor = []
        self.subs_createAssignmentList = []
        self.subs_createAssignmentCont = []
        self.subs_assignmentCreated = []
        self.subs_createAssignmentObject = []
        self.subs_assignmentModified = []
        self.subs_modifyAssignmentObject = []
        self.subs_createSubCont = []
        self.subs_createSubList = []

        self.pageMaker = None

    def set_pageMaker(self, pageMaker):
        self.pageMaker = pageMaker

    ### events
    def event_wrongRequestWarning(self, warning_msg):
        for i in range(len(self.subs_wrongRequestWarning)):
            self.subs_wrongRequestWarning[i].event_wrongRequestWarning(warning_msg)
        return self.pageMaker.event_wrongRequestWarning(warning_msg)

    def event_createAssignmentEditor(self, parsed):
        for i in range(len(self.subs_createAssignmentEditor)):
            self.subs_createAssignmentEditor[i].event_createAssignmentEditor(parsed)

    def event_createAssignmentList(self, parsed):
        for i in range(len(self.subs_createAssignmentEditor)):
            self.subs_createAssignmentEditor[i].event_createAssignmentEditor(parsed)

    def event_createAssignmentCont(self, parsed):
        pass

    def event_assignmentCreated(self, kA):
        pass

    def event_createAssignmentObject(self, parsed):
        pass

    def event_assignmentModified(self, kA):
        pass

    def event_modifyAssignmentObject(self, parsed):
        pass

    def event_createSubCont(self, parsed):
        pass

    def event_createSubList(self, parsed):
        pass

    ### register
    def register_wrongRequestWarning(self, subs):
        if subs not in self.subs_wrongRequestWarning:
            self.subs_wrongRequestWarning.append(subs)



    ### unregister
    def unregister_wrongRequestWarning(self, subs):
        if subs in self.subs_wrongRequestWarning:
            self.subs_wrongRequestWarning.pop(subs)

   