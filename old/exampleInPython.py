#!/usr/bin/env python

import facebook

oauth_access_token = ""

graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="If you can read this means I was able to post on my facebook wall from python #test")
likes = graph.get_connections("me", "likes")


