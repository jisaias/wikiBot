import wikipedia

subjectKey = raw_input("What subject would you like to find more about? ")

summaryParagraph = wikipedia.summary(subjectKey)

subjectKey = subjectKey.replace(' ','_')

wikiURL = 'https://en.wikipedia.org/wiki/' + subjectKey

print(summaryParagraph)

print(wikiURL)



