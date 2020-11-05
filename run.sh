#!/bin/bash

DIR=`cd $( dirname $0 ) && pwd`

if [ -z $1 ];then
	echo "Please specify project folder"
	exit 1
fi

docker run -ti --rm \
	-v $1:/project \
	-v $DIR/app.py:/app/main.py \
	-w /app \
	python \
  python main.py