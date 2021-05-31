class Page:
    def __init__ (self, content):
        self.content = content

class PageMaker:

    ### Methods

    def renderWarningPage(self, warning_msg):
        print("PageMaker: Render error warning page")
        print("-> " + warning_msg)
        page = Page("Warning Page: " + warning_msg)
        return page

    def renderAssignmentEditor(self, param):
        if type(param) == type({}):             ## Editor for New Assignment
            print("PageMaker: Render assignment editor")
            print("-> Editor with 'Blank' for new Assignment of class " + param['class'])
            page = Page("Editor Page: with blank for class " + param['class'])
            return page
        elif type(param) == type(''):           ## DB Search Fail
            return self.renderWarningPage(param)
        else:                                   ## Editor for Modify Assignment
            print("PageMaker: Render assignment editor")
            print("-> Editor for modify " + param.title)
            page = Page("Editor Page: for modify " + param.title)
            return page
            
    def renderAssignmentList(self, param):
        if type(param) == type(''):             ## Something error on DB
            return self.renderWarningPage(param)
        else:                                   ## param = list of Assignment class
            print("Pagemaker: Render assignment list")
            for i in range(len(param)): print("-> " + param[i].title)
            page = Page("Assignment List Page")
            return page

    def renderAssignmentContent(self, param):
        if type(param) == type(''):             ## Something error on DB
            return self.renderWarningPage(param)
        else:                                   ## param = Assignment
            print("Pagemaker: Render assignment content")
            print("-> title:" + param.title)
            page = Page("Assignment Content of " + param.title)
            return page

    def renderSubmissionList(self, param):
        if type(param) == type(''):             ## Something error on DB
            return self.renderWarningPage(param)
        else:                                   ## param = list of Submission class
            print("Pagemaker: Render submission list")
            for i in range(len(param)): print("-> " + param[i].title)
            page = Page("Submission List Page")
            return page

    def renderSubmissionContent(self, param):
        if type(param) == type(''):             ## Something error on DB
            return self.renderWarningPage(param)
        else:                                   ## param = Submission
            print("Pagemaker: Render submission content")
            print("-> title:" + param.title)
            page = Page("Submission Content of " + param.title)
            return page

    ### Subscribing Events

    def event_WrongRequestWarning(self, warning_msg):
        return ('PageMaker',self.renderWarningPage(warning_msg))
    
    def event_AssignmentEditorNew(self, parsed):
        return ('PageMaker',self.renderAssignmentEditor(parsed))

    def event_AssignmentEditorModify(self, param):
        return ('PageMaker', self.renderAssignmentEditor(param))
    
    def event_AssignmentList(self, param):
        return ('PageMaker', self.renderAssignmentList(param))
    
    def event_AssignmentCont(self, param):
        return ('PageMaker', self.renderAssignmentContent(param))
    
    def event_AssignmentCreated(self, kA):
        return ('PageMaker', self.renderAssignmentContent(kA))
    
    def event_AssignmentModified(self, kA):
        return ('PageMaker', self.renderAssignmentContent(kA))
    
    def event_SubCont(self, param):
        return ('PageMaker', self.renderSubmissionContent(param))
    
    def event_SubList(self, param):
        return ('PageMaker', self.renderSubmissionList(param))


