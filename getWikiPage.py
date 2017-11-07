import wikipedia

#returns link to Wikipedia article
def getPage(question):

    subjectKey = question
    
    subjectKey = subjectKey.replace(' ','_')
    
    wikiURL = 'https://en.wikipedia.org/wiki/' + subjectKey
    
    return wikiURL
    
#returns summary paragraph
def getPara(question):
    subj = question
    
    para = wikipedia.summary(subj)
    
    return para