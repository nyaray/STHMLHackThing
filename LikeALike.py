#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys
from pprint import pprint

# put the facebook auth token here
# later get it directly through the JS SDK provided from FB
oauth_access_token = "CAACEdEose0cBAEh7ZCbvNIeN7qPihDQE6mn1PwGEAAUzXPyzUQhk61oA8Dw50LBGMSCAgRWwP4H7RYlnDu2Tbk4DZAQ9CliZB1oU2YP1V26xUQLZCgqYnzio7F8uoPjTb1tseslZCcxCEyY0M9rPXLHZBOux8xV766g4UGkPpufQZDZD"


def getGraph():
    return facebook.GraphAPI(oauth_access_token)


def getProfile(graph, profile="me"):
    return graph.get_object(profile)


def getLikes(graph, profile):
    return graph.get_connections(profile['id'], "likes")


def getFriends(graph, profile):
    return graph.get_connections(profile['id'], "friends")


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

    friendsList = []
    friendsList.extend(getIDList(miaLikes))
    friendsList.extend(getIDList(jensLikes))
    friendsList.extend(getIDList(nyarayLikes))

    intersectionList = []
    intersectionList.extend(getIntersection(getIDList(meLikes), getIDList(miaLikes)))
    intersectionList.extend(getIntersection(getIDList(meLikes), getIDList(jensLikes)))
    intersectionList.extend(getIntersection(getIDList(meLikes), getIDList(nyarayLikes)))

    stuffInCommonDict = {}
    finalList = []
    for element in meLikes['data']:
        # print element['id']
        if (int(element['id']) in intersectionList):
            finalList.append(element['name'])
            stuffInCommonDict[element['name']] = int(element['id'])
            stuffInCommonDict[element['id']] = (element['name'])
        # print
        # u"{}".format(element['name']).encode(sys.getfilesystemencoding())
        # tmpList.append(int(element['id']))
    finalList.sort()
    # pprint(finalList)
    # print "-------------"
    pprint(stuffInCommonDict)


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        main(sys.argv)
    except:
        print "Error: Exception raised!"
        raise
