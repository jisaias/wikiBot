import lib.wikiBot as WB
import time
import getWikiPage as wiki

#assigns subject of message to variable
subject = WB.readMessage()

#assigns values to URL and summary
url = wiki.getPage(subject)
para = wiki.getPara(subject)

#posts answer to blog
WB.postAThing(url,para,subject)