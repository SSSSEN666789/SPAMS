'''
규칙 깨는 이벤트: 
CreateAssignmentObject
ModifyAssignmentObject


'''
class EventManager:

    def __init__(self): 
        
        ### 구독자 목록.
        # 공통적으로 PageMaker는 제외. self.pageMaker로 별도 지정.
        # 단순 작업이 아니라 특별한 리턴값 필요한 경우 리스트에 포함하지 않음.
        # 대신 주석으로 기록할 것

        self.subs_WrongRequestWarning = []      
        self.subs_AssignmentEditorNew = []
        self.subs_AssignmentEditorModify = []
        self.subs_AssignmentList = []
        self.subs_AssignmentCont = []
        self.subs_CreateAssignmentObject = None # AssignmentMaker만 와야 함.
        self.subs_AssignmentCreated = []
        self.subs_ModifyAssignmentObject = None # AssignmentDBConnection만 와야 함.
        self.subs_AssignmentModified = []
        self.subs_SubCont = []
        self.subs_SubList = []

    def set_pageMaker(self, pageMaker):
        self.pageMaker = pageMaker

    def activate_event(self, validChkRes, params):

        if validChkRes != 'accepted':
            return self.event_WrongRequestWarning(validChkRes)

        request = params[0]
        parsed = params[1]

        if request == 'AssignmentEditorNew': self.event_AssignmentEditorNew(parsed)
        if request == 'AssignmentEditorModify': self.event_AssignmentEditorModify(parsed)
        if request == 'AssignmentList': self.event_AssignmentList(parsed)
        if request == 'AssignmentContent': self.event_AssignmentCont(parsed)
        if request == 'RegisterAssignment': self.event_CreateAssignmentObject(parsed)
        if request == 'ModifyAssignment': self.event_ModifyAssignmentObject(parsed)
        if request == 'SubmissionList': self.event_SubList(parsed)
        if request == 'SubmissionContent': self.event_SubCont(parsed)
       
    ##### Event _ Register _ Unregister #####

    ### WrongRequestWarning ###

    def event_WrongRequestWarning(self, warning_msg):
        resdict = {}
        for i in range(len(self.subs_WrongRequestWarning)):
            res = self.subs_WrongRequestWarning[i].event_WrongRequestWarning(warning_msg)
            resdict[res[0]] = res[1] 
        return self.pageMaker.event_WrongRequestWarning(warning_msg)

    def register_WrongRequestWarning(self, subs):
        if subs not in self.subs_WrongRequestWarning:
            self.subs_WrongRequestWarning.append(subs)

    def unregister_WrongRequestWarning(self, subs):
        if subs in self.subs_WrongRequestWarning:
            self.subs_WrongRequestWarning.pop(subs)

    ### AssignmentEditorNew ###

    def event_AssignmentEditorNew(self, parsed):
        resdict = {}
        for i in range(len(self.subs_AssignmentEditorNew)):
            res = self.subs_AssignmentEditorNew[i].event_AssignmentEditorNew(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentEditorNew(parsed)

    def register_AssignmentEditorNew(self, subs):
        if subs not in self.subs_AssignmentEditorNew:
            self.subs_AssignmentEditorNew.append(subs)

    def unregister_AssignmentEditorNew(self, subs):
        if subs in self.subs_AssignmentEditorNew:
            self.subs_AssignmentEditorNew.pop(subs)

    ### AssignmentEditorModify ###

    def event_AssignmentEditorModify(self, parsed):
        resdict = {}
        for i in range(len(self.subs_AssignmentEditorModify)):
            res = self.subs_AssignmentEditorModify[i].event_AssignmentEditorModify(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentEditorModify(resdict['AssignmentsDBConnection'])

    def register_AssignmentEditorModify(self, subs):
        if subs not in self.subs_AssignmentEditorModify:
            self.subs_AssignmentEditorModify.append(subs)

    def unregister_AssignmentEditorModify(self, subs):
        if subs in self.subs_AssignmentEditorModify:
            self.subs_AssignmentEditorModify.pop(subs)

    ### AssignmentList ###

    def event_AssignmentList(self, parsed):
        resdict = {}
        for i in range(len(self.subs_AssignmentList)):
            res = self.subs_AssignmentList[i].event_AssignmentList(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentList(resdict['AssignmentsDBConnection'])

    def register_AssignmentList(self, subs):
        if subs not in self.subs_AssignmentList:
            self.subs_AssignmentList.append(subs)

    def unregister_AssignmentList(self, subs):
        if subs in self.subs_AssignmentList:
            self.subs_AssignmentList.pop(subs)

    ### AssignmentCont ###

    def event_AssignmentCont(self, parsed):
        resdict = {}
        for i in range(len(self.subs_AssignmentCont)):
            res = self.subs_AssignmentCont[i].event_AssignmentCont(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentCont(resdict['AssignmentsDBConnection'])

    def register_AssignmentCont(self, subs):
        if subs not in self.subs_AssignmentCont:
            self.subs_AssignmentCont.append(subs)

    def unregister_AssignmentCont(self, subs):
        if subs in self.subs_AssignmentCont:
            self.subs_AssignmentCont.pop(subs)

    ### CreateAssignmentObject ###

    def event_CreateAssignmentObject(self, parsed):
        res = self.subs_CreateAssignmentObject.event_CreateAssignmentObject(parsed)
        return self.event_AssignmentCreated(res[1])

    def register_CreateAssignmentObject(self, subs):
        self.subs_CreateAssignmentObject = subs

    def unregister_CreateAssignmentObject(self, subs):
        if subs is self.subs_CreateAssignmentObject:
            self.subs_CreateAssignmentObject = None

    ### AssignmentCreated ###

    def event_AssignmentCreated(self, kA):
        resdict = {}
        for i in range(len(self.subs_AssignmentCreated)):
            res = self.subs_AssignmentCreated[i].event_AssignmentCreated(kA)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentCont(kA)

    def register_AssignmentCreated(self, subs):
        if subs not in self.subs_AssignmentCreated:
            self.subs_AssignmentCreated.append(subs)

    def unregister_AssignmentCreated(self, subs):
        if subs in self.subs_AssignmentCreated:
            self.subs_AssignmentCreated.pop(subs)

    ### ModifyAssignmentObject ###

    def event_ModifyAssignmentObject(self, parsed):
        res = self.subs_ModifyAssignmentObject.event_ModifyAssignmentObject(parsed)
        return self.event_AssignmentModified(res[1])

    def register_ModifyAssignmentObject(self, subs):
        self.subs_ModifyAssignmentObject = subs

    def unregister_ModifyAssignmentObject(self, subs):
        if subs is self.subs_ModifyAssignmentObject:
            self.subs_ModifyAssignmentObject = None

    ### AssignmentModified ###

    def event_AssignmentModified(self, kA):
        resdict = {}
        for i in range(len(self.subs_AssignmentModified)):
            res = self.subs_AssignmentModified[i].event_AssignmentModified(kA)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_AssignmentModified(kA)

    def register_AssignmentModified(self, subs):
        if subs not in self.subs_AssignmentModified:
            self.subs_AssignmentModified.append(subs)

    def unregister_AssignmentModified(self, subs):
        if subs in self.subs_AssignmentModified:
            self.subs_AssignmentModified.pop(subs)

    ### SubCont ###

    def event_SubCont(self, parsed):
        resdict = {}
        for i in range(len(self.subs_SubCont)):
            res = self.subs_SubCont[i].event_SubCont(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_SubCont(resdict['SubmissionsDBConnection'])

    def register_SubCont(self, subs):
        if subs not in self.subs_SubCont:
            self.subs_SubCont.append(subs)

    def unregister_SubCont(self, subs):
        if subs in self.subs_SubCont:
            self.subs_SubCont.pop(subs)

    ### SubList ###

    def event_SubList(self, parsed):
        resdict = {}
        for i in range(len(self.subs_SubList)):
            res = self.subs_SubList[i].event_SubList(parsed)
            resdict[res[0]] = res[1]
        return self.pageMaker.event_SubList(resdict['SubmissionsDBConnection'])

    def register_SubList(self, subs):
        if subs not in self.subs_SubList:
            self.subs_SubList.append(subs)

    def unregister_SubList(self, subs):
        if subs in self.subs_SubList:
            self.subs_SubList.pop(subs)
