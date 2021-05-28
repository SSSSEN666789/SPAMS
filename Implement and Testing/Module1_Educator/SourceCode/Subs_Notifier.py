class Notifier:

    ### Methods

    def notice_AssignmentCreated(self, kA):
        #학생들에게 과제 생성 알림.
        #실 구현 하려면 학생DB가 있어야 할듯.
        print("Notifier: Creation of assignment \'" + kA.title + "\' is notified to students")
        return True

    ### Subscribing Events

    def event_AssignmentCreated(self, kA):
        return ('Notifier', self.notice_AssignmentCreated(kA)) 