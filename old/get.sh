#!/bin/bash


# the config file, a template can be found at config.sample.txt
source config.txt

# you can override the user and fields variable from the command line
# $ ./get.sh <user> <fields>
USER=$1
FIELDS=$2

# build the request together and beautify it
#wget -qO - https://graph.facebook.com/$USER?fields=$FIELDS\&access_token=$TOKEN | cat | python -mjson.tool
echo "curl https://graph.facebook.com/$USER?fields=$FIELDS&access_token=\$TOKEN | python -mjson.tool"
curl "https://graph.facebook.com/$USER?fields=$FIELDS&access_token=$TOKEN" | python -mjson.tool

## side note
## sh get.sh | grep category | sort | uniq


