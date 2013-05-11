#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys
from pprint import pprint

# put the facebook auth token here
# later get it directly through the JS SDK provided from FB
oauth_access_token = "CAACEdEose0cBAEKhZCdUZAap7Vpnt91ZAEpXEBKHj1QVJF1cuxCnSUf8qedRKsP6pPWc9uBVv6lyw36XcQOkLqlgu0PagZCZBAbssFVhZA5hmBswCmXmk3yOJfgZCT47yInwew2Mun9rFZAKqvetGaCFzo5mzDalHbZC3nVwHL0J73gZDZD"


def getGraph():
    return facebook.GraphAPI(oauth_access_token)


def getProfile(graph, profile="me"):
    return graph.get_object(profile)


def getLikes(graph, profile):
    return graph.get_connections(profile['id'], "likes")


def getFriends(graph, profile):
    return graph.get_connections(profile['id'], "friends")


def main(argv):
    graph = getGraph()

    myProfile = getProfile(graph)
    meLikes = getLikes(graph, myProfile)

    chrisProfile = getProfile(graph, "christopher.loessl")
    chrisLikes = getLikes(graph, chrisProfile)
    nyarayProfile = getProfile(graph, "nyaray")
    nyarayLikes = getLikes(graph, nyarayProfile)
    miaProfile = getProfile(graph, "mia5419")
    miaLikes = getLikes(graph, miaProfile)
    jensProfile = getProfile(graph, "jens.rosen")
    jensLikes = getLikes(graph, jensProfile)

    # gives me the data structure to work with
    # DEBUG!!
    # pprint(meLikes)
    # print "------"
    # pprint(meLikes.values())

    # this is a list of dictionaries
    listOfCoolStuff = meLikes['data']
    listA = []
    for element in listOfCoolStuff:
        # print u"{}".format(element['name']).encode(sys.getfilesystemencoding())
        listA.append(int(element['id']))

    listOfCoolStuff = miaLikes['data']
    listB = []
    for element in listOfCoolStuff:
        # print u"{}".format(element['name']).encode(sys.getfilesystemencoding())
        listB.append(int(element['id']))

    setA = set(listA)
    setB = set(listB)
    setInter = setA & setB
    print setInter


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        main(sys.argv)
    except:
        print "Error: Exception raised!"
        raise
