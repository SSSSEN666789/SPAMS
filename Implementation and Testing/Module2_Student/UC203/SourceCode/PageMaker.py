class Page:
    def __init__(self, result):
        self.result = result
        print (result)

class PageMaker:

    # Methods
    def renderWarningPage(self):
        print("PageMaker: Render error warning page")

        page = Page("Warning Page:")
        return page

    def renderSubmissionResult(self):
        page = Page("Rendering Result")
        return page

    # Subscribing Events

    def event_WrongRequestWarning(self):
        return 'PageMaker', self.renderWarningPage(self)

    def event_SubRes(self, param):
        return 'PageMaker', self.renderSubmissionResult(param)
