#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys
from pprint import pprint

# put the facebook auth token here
# later get it directly through the JS SDK provided from FB
oauth_access_token = "CAACEdEose0cBAGe4m6yb8gMBSzTr7U1CyIL0uLWjAwA6U8uZAcFg08wMRp6tE6jGWboXXuDGZAgCTqWqIVIEZAAHh6ZCuCQvz5LN1AuSXoyZCuQvJZAhPKaltyA4TlHYErpGvBTxslCGDIKYw7vmYAWNSivQpATNU0LPSQdr4cgAZDZD"


def getGraph():
    return facebook.GraphAPI(oauth_access_token)


def getProfile(graph, profile="me"):
    return graph.get_object(profile)


def getLikes(graph, profile):
    return graph.get_connections(profile['id'], "likes")


def getFriends(graph, profile):
    return graph.get_connections(profile['id'], "friends")

def makeDict(data):
    dic = []
    for x in data:
        dic.append(x['category'])
    a = list(set(dic))
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


def main(argv):
    graph = getGraph()

    myProfile = getProfile(graph)
    meLikes = getLikes(graph, myProfile)

    # chrisProfile = getProfile(graph, "christopher.loessl")
    # chrisLikes = getLikes(graph, chrisProfile)
    nyarayProfile = getProfile(graph, "nyaray")
    nyarayLikes = getLikes(graph, nyarayProfile)
    miaProfile = getProfile(graph, "mia5419")
    miaLikes = getLikes(graph, miaProfile)
    jensProfile = getProfile(graph, "jens.rosen")
    jensLikes = getLikes(graph, jensProfile)


    print getListByCategory(meLikes['data'])
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
    meLikesIDList = getIDList(meLikes)

    miaLikesList = getIDList(miaLikes)
    jensLikesList = getIDList(jensLikes)
    nyarayLikesList = getIDList(nyarayLikes)

    friendsList = []
    friendsList.extend(miaLikesList)
    friendsList.extend(jensLikesList)
    friendsList.extend(nyarayLikesList)

    intersectionList = []
    intersectionList.extend(getIntersection(meLikesIDList, miaLikesList))
    intersectionList.extend(getIntersection(meLikesIDList, jensLikesList))
    intersectionList.extend(getIntersection(meLikesIDList, nyarayLikesList))

    pprint(getIntersection(meLikes, miaLikes))

    stuffInCommonDict = {}
    finalList = []
    for element in meLikes['data']:
        # print element['id']
        if (int(element['id']) in intersectionList):
            finalList.append(element['name'])
            stuffInCommonDict[element['name']] = int(element['id'])
            stuffInCommonDict[element['id']] = (element['name'])
            print u"{0:50s} ({1})".format(element['name'], int(element['id'])).encode(sys.getfilesystemencoding())
        # tmpList.append(int(element['id']))
    finalList.sort()
    # print "-------------"
    # pprint(stuffInCommonDict)

    # print u"\nWe chose as a test NetHack (112228158790462)\n".encode(sys.getfilesystemencoding())


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        main(sys.argv)
    except:
        print "Error: Exception raised!"
        raise
