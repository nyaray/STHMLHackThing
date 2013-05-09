#!/bin/bash

# put your secret token in there
source token.txt

# "me" referes to the actuall user
USER=me

# fields you want to get back
#FIELDS=id,name,picture # this works w/o token but you have to provide a USER (not "me")
FIELDS=id,name,likes

# build the request together and beautify it
#wget -qO - https://graph.facebook.com/$USER?fields=$FIELDS\&access_token=$TOKEN | cat | python -mjson.tool
curl https://graph.facebook.com/$USER?fields=$FIELDS\&access_token=$TOKEN | python -mjson.tool

## side note
## sh get.sh | grep category | sort | uniq


