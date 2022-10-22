#!/bin/bash

echo HABITICA-PYTOOLS


USER_ID=$(cat credentials.json | jq .USER_ID | sed 's/"//g')
API_TOKEN=$(cat credentials.json | jq .API_TOKEN | sed 's/"//g')

echo $USER_ID $API_TOKEN

DATA='{"text":"todo wowee", "type":"todo"}'



####get tasks
curl https://habitica.com/api/v3/tasks/user -s -X GET \
    -H "x-api-user: $USER_ID " \
    -H "x-api-key: $API_TOKEN" \ | jq .data


    #-H "Content-Type:application/json" \


##create task
#curl https://habitica.com/api/v3/tasks/user -s -X POST \
    #-H "Content-Type:application/json" \
    #-H "x-api-user: $USER_ID " \
    #-H "x-api-key: $API_TOKEN" \
    #-d "$DATA"




