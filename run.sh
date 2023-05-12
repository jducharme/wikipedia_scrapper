#!/bin/sh

# Volume Path
VOLUME_PATH=$(pwd)/src

# Create the docker image
docker build . -t jducharme:wikipedia_scrapper_test

if [ ! "$(docker ps -q -f name=jducharme-wikipedia_scrapper_test-container)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=jducharme-wikipedia_scrapper_test-container)" ]; then
        # cleanup
        docker rm jducharme-wikipedia_scrapper_test-container
    fi
    # run your container
    docker run --name jducharme-wikipedia_scrapper_test-container \
                    -v $VOLUME_PATH:/src \
                    -it jducharme:wikipedia_scrapper_test    bash
fi
