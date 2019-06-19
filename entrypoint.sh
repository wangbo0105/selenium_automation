#!/usr/bin/env bash
#!/bin/bash


HOME=$(dirname "$0")

if [ -z "$PRODUCTION" ]
then
	echo "ON STAGING"
	cp testdata/stg_userdata.robot testdata/userdata.robot
else
	echo "ON PRODUCTION"
	cp testdata/prod_userdata.robot testdata/userdata.robot
fi

robot --pythonpath ${HOME}/services --pythonpath ${HOME}  ${HOME}/features



