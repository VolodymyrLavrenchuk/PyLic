#!/bin/bash

DIR=`cd $( dirname $0 ) && pwd`

docker run -ti --rm \
	-v ~/DMP:/DMP \
	-v $DIR/app.py:/app/main.py \
	-w /app \
	python \
  python main.py