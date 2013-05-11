#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import sys
import pprint

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
    # chrisProfile = getProfile(graph, "christopher.loessl")
    # miaProfile = getProfile(graph, "mia5419")
    # jensProfile = getProfile(graph, "jens.rosen")
    # chrisLikes = getLikes(graph, chrisProfile)
    # pprint.pprint(meLikes)
    # print "------"
    # print ("My likes {}").format()
    pprint.pprint(meLikes.values())
    # print


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        main(sys.argv)
    except:
        print "Error: Exception raised!"
        raise
