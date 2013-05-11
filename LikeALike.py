#!/usr/bin/env python

import facebook
import sys

# put the facebook auth token here
# later get it directly through the JS SDK provided from FB
oauth_access_token = "CAACEdEose0cBACMxiVg82sJzAg72oNCX1rLyZAXFZAAYzSZAyltV9U59c0otbEzE8UcdeSBR3ZB9iWwLClPxQvKI3ZCzHTdoPQFdaBQHzZCSim5kMMuWQzC221mQXbRuXa0QlGUy1jRB53UZAjRq4ZA3DVYmSz3NZAyZBAROvAPiLAyQZDZD"


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
    print meLikes
    # print ("My likes {}").format()


if __name__ == '__main__':
    if not sys.version_info > (2, 7, 0):
        print "Error, I need python 2.7 or above"
        exit(1)
    try:
        main(sys.argv)
    except:
        print "Error: Exception raised!"
        raise
