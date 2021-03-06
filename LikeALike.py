#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys
from pprint import pprint

# put the facebook auth token here
# later get it directly through the JS SDK provided from FB
oauth_access_token = "CAACEdEose0cBAL4uIb60x7GzDJBI5kyUxu5yZAOtTtU9UsKe6WeN8u80fLlpAgdPg3HpkFFTFWLWX61CwQXHU0G1afTIL6ZA3hAzDQ8pf9BlbDXZAR8pB9pVbYXYDvPHlzNUhogHIjLjiigwQEbxnEZAfssFdTYFpcIChgrIFQZDZD"
bigListDic = []
bigHuglyHack = []

def getGraph():
    return facebook.GraphAPI(oauth_access_token)


def getProfile(graph, profile="me"):
    return graph.get_object(profile)


def getLikes(graph, profile):
    return graph.get_connections(profile['id'], "likes")


def getFriends(graph, profile):
    return graph.get_connections(profile['id'], "friends")


def makeDict(data):
    dic = list()
    for x in data:
        dic.append(x['category'])
    a = list(set(dic))
    a.sort()
    return [{'category': x, 'members': list()} for x in a]


def getListByCategory(data):
    dic = makeDict(data)
    for x in data:
        for y in dic:
            if x['category'] == y['category']:
                y['members'].append(x)
    return dic


def getIDList(likes):
    tmpList = []
    for element in likes['data']:
        # print
        # u"{}".format(element['name']).encode(sys.getfilesystemencoding())
        tmpList.append(int(element['id']))
    return tmpList


def getIntersection(listA, listB):
    return list(set(listA) & set(listB))


def getListOfDicOfIntersections():
    # pprint (facebook.get_app_access_token("421157351314971", "168836433e1d0efb56320bca5dcef2fd"))
    graph = getGraph()

    myProfile = getProfile(graph)

    meLikes = getLikes(graph, myProfile)
    meFriends = getFriends(graph, myProfile)

    # chrisProfile = getProfile(graph, "christopher.loessl")
    # chrisLikes = getLikes(graph, chrisProfile)
    nyarayProfile = getProfile(graph, "nyaray")
    nyarayLikes = getLikes(graph, nyarayProfile)
    miaProfile = getProfile(graph, "mia5419")
    miaLikes = getLikes(graph, miaProfile)
    jensProfile = getProfile(graph, "jens.rosen")
    jensLikes = getLikes(graph, jensProfile)

    # pprint(getListByCategory(meLikes['data']))
    # friends = {'nyarayProfile['id']': nyarayLikes,
    #            'miaProfile['id']': miaLikes,
    #            'jensProfile['id']': jensLikes
    #            }

    # gives me the data structure to work with
    # DEBUG!!
    # pprint(meLikes)
    # print "------"
    # pprint(meLikes.values())

    # this is a list of dictionaries
    # this will be needed to have a mapping between id -> name
    listOfCoolStuff = meLikes['data']
    global bigHuglyHack
    bigHuglyHack = listOfCoolStuff
    meLikesIDList = getIDList(meLikes)

    miaLikesList = getIDList(miaLikes)
    jensLikesList = getIDList(jensLikes)
    nyarayLikesList = getIDList(nyarayLikes)

    global bigListDic
    bigListDic.append({'Mia': miaLikesList})
    bigListDic.append({'Jens': jensLikesList})
    bigListDic.append({'Nyaray': nyarayLikesList})

    friendsList = []
    friendsList.extend(miaLikesList)
    friendsList.extend(jensLikesList)
    friendsList.extend(nyarayLikesList)

    intersectionList = []
    intersectionList.extend(getIntersection(meLikesIDList, miaLikesList))
    intersectionList.extend(getIntersection(meLikesIDList, jensLikesList))
    intersectionList.extend(getIntersection(meLikesIDList, nyarayLikesList))

    # pprint(getIntersection(meLikes, miaLikes))

    stuffInCommonListDict = []
    stuffInCommonDict = {}
    finalList = []
    for element in meLikes['data']:
        # print element['id']
        if (int(element['id']) in intersectionList):
            stuffInCommonDict = {}
            finalList.append(element['name'])
            stuffInCommonDict['name'] = element['name']
            stuffInCommonDict['id'] = int(element['id'])
            stuffInCommonDict['category'] = (element['category'])
            stuffInCommonListDict.append(stuffInCommonDict)
            print u"{0:50s} ({1})".format(element['name'], int(element['id'])).encode(sys.getfilesystemencoding())
        # tmpList.append(int(element['id']))
    finalList.sort()
    # print "-------------"
    # pprint(stuffInCommonDict)

    print u"\nWe chose as a test Facebook Developers (19292868552)".encode(sys.getfilesystemencoding())
    chose = 19292868552
    count = 0
    if chose in miaLikesList:
        count = count + 1
        print "Mia"
    if chose in jensLikesList:
        count = count + 1
        print "Jens"
    if chose in nyarayLikesList:
        count = count + 1
        print "Nyaray"

    print "--------"
    print "Count: {}".format(count)

    print u"\nWe chose as a test Facebook Hacker Cup (133954286636768)".encode(sys.getfilesystemencoding())
    chose = 133954286636768
    count = 0
    if chose in miaLikesList:
        count = count + 1
        print "Mia"
    if chose in jensLikesList:
        count = count + 1
        print "Jens"
    if chose in nyarayLikesList:
        count = count + 1
        print "Nyaray"

    print "--------"
    print "Count: {}".format(count)

    return (stuffInCommonListDict)


def printListDic(listOfDicInt):
    for ele in listOfDicInt:
        for key, value in ele.iteritems():
            print u"{} {}".format(key, value).encode(sys.getfilesystemencoding())
    # print u"{0:50s} ({1})".format(element['name'], int(element['id'])).encode(sys.getfilesystemencoding())


def whoLikes(chose):
    # {'name': 'our like', 'friends': []}
    dictio = {}
    print "TEST"
    print u"\nWe chose # {}".format(chose).encode(sys.getfilesystemencoding())

    choseString = str(chose)

    for ele in bigHuglyHack:
        for key, value in ele.iteritems():
            if (key == 'name'):
                saveString = value
            if (key == 'id' and value == choseString):
                print(ele['name'])
                dictio = {'name': ele['name']}

    # pprint(bigListDic)
    # return dictio

    tmpList = []
    if chose in bigListDic[0]['Mia']:
        tmpList.append("Mia")

    if chose in bigListDic[1]['Jens']:
        tmpList.append("Jens")

    if chose in bigListDic[2]['Nyaray']:
        tmpList.append("Nyaray")

    dictio['friends'] = tmpList
    pprint(dictio)
    return dictio

    # count = 0
    # if chose in miaLikesList:
    #     count = count + 1
    #     print "Mia"
    # if chose in jensLikesList:
    #     count = count + 1
    #     print "Jens"
    # if chose in nyarayLikesList:
    #     count = count + 1
    #     print "Nyaray"

    # return dictio


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        # main(sys.argv)
        listOfDicInt = getListOfDicOfIntersections()
        # printListDic(listOfDicInt)
        whoLikes(114266562069063)
        whoLikes(189973461027841)
    except:
        print "Error: Exception raised!"
        raise
