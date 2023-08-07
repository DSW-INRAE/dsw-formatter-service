from abc import abstractclassmethod


class abstractQuestion:

    def __init__(self, uuid):
        
    @abstractclassmethod
    def returnValue(self):
        pass


class listQuestion(abstractQuestion):

    def returnValue(self):
        return "listQuestion"


class valueQuestion(abstractQuestion):

    def returnValue(self):
        return "valueQuestion"


class multiChoiceQuestion(abstractQuestion):

    def returnValue(self):
        return "multiChoiceQuestion"


class optionsQuestion(abstractQuestion):

    def returnValue(self):
        return "optionsQuestion"


class integrationQuestion(abstractQuestion):

    def returnValue(self):
        return "integrationQuestion"
