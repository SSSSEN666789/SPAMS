from ParseCheckDecorators import *
from Pub_EventManager import EventManager
from Subs_PageMaker import PageMaker
from Subs_AssignmentMaker import AssignmentMaker
from Subs_AssignmentsDBConnection import AssignmentsDBConnection
from Subs_SubmissionsDBConnection import SubmissionsDBConnection
from Subs_Notifier import Notifier

decorator_Controller = Controller()
decorator_QueryParser = QueryParser()
decorator_ValidChecker = ValidChecker()

Pub_EventManager = EventManager()
Subs_PageMaker = PageMaker()
Subs_AssignmentMaker = AssignmentMaker()
Subs_AssignmentsDBConnection = AssignmentsDBConnection()
Subs_SubmissionsDBConnection = SubmissionsDBConnection()
Subs_Notifier = Notifier()

decorator_Controller.set_decorator_chain(None, decorator_QueryParser)
decorator_QueryParser.set_decorator_chain(decorator_Controller, decorator_ValidChecker)
decorator_ValidChecker.set_decorator_chain(decorator_QueryParser, Pub_EventManager)

Pub_EventManager.set_pageMaker(Subs_PageMaker)
Pub_EventManager.register_AssignmentEditorModify(Subs_AssignmentsDBConnection)
Pub_EventManager.register_AssignmentList(Subs_AssignmentsDBConnection)
Pub_EventManager.register_AssignmentCont(Subs_AssignmentsDBConnection)
Pub_EventManager.register_CreateAssignmentObject(Subs_AssignmentMaker)
Pub_EventManager.register_AssignmentCreated(Subs_AssignmentsDBConnection)
Pub_EventManager.register_AssignmentCreated(Subs_Notifier)
Pub_EventManager.register_ModifyAssignmentObject(Subs_AssignmentsDBConnection)
Pub_EventManager.register_SubCont(Subs_SubmissionsDBConnection)
Pub_EventManager.register_SubList(Subs_SubmissionsDBConnection)

print("Enter Query: ", end="")
while 1:
    query = str(input())
    print("\n-----Start-----")
    decorator_Controller.createPage(query)
    print("------End------\n")
    print("Enter Query: ", end="")