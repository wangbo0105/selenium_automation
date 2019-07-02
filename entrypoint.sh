#!/usr/bin/env bash


HOME=$(dirname "$0")

TARGET=

print_usage () {
cat << EOF

Usage: $0 <type> <target>

type:
    regression
    smoking

target:
    staging
    production

EOF
}

if [ "$#" -ne 2 ]; then
    echo "Invalid arguments"
    print_usage
    exit 1
fi


if [ $1 = "regression" ]; then
    TARGET=features
elif [ $1 = "smoking" ]; then
    TARGET=smoke
else
    echo "Invalid type"
    print_usage
    exit 1
fi

if [ $2 = "production" ]; then
	echo "ON PRODUCTION"
	cp $HOME/testdata/prod_userdata.robot $HOME/testdata/userdata.robot
    export PRODUCTION=true
    robot -re -l ./report/log -r ./report/report -o ./report/output --pythonpath ${HOME}/services --pythonpath ${HOME}  ${HOME}/${TARGET}

elif [ $2 = "staging" ]; then
	echo "ON STAGING"
	cp $HOME/testdata/stg_userdata.robot $HOME/testdata/userdata.robot
	robot -re -l ./report/log -r ./report/report -o ./report/output -e production --pythonpath ${HOME}/services --pythonpath ${HOME}  ${HOME}/${TARGET}

else
    echo "Invalid target"
    print_usage
    exit 1
fi

#robot --pythonpath ${HOME}/services --pythonpath ${HOME}  ${HOME}/${TARGET}


