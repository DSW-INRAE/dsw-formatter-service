import questions


def createCSVFile(questionnaireDictionary: dict):
    repliesDictionary: dict = questionnaireDictionary["replies"]
    knowledgeModelDictionary: dict = questionnaireDictionary["knowledgeModel"]
    mapOfPossibleQuestionTypeAndClassAssociated = {
            "listQuestion" = questions.listQuestion,
            "valueQuestion" = questions.valueQuestion,
            "integrationQuestion" = questions.integrationQuestion,
            "multiChoiceQuestion" = 

    
            
