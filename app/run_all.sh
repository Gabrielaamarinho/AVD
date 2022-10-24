#!/bin/bash

cd $(pwd)/containers && docker-compose up -d

cd ..

cd $(pwd)/jobs && python3 get_data.py && python3 create_dataframes.py && python3 database.py

docker run --platform linux/amd64 -d -p 3000:3000 --name metabase-avd metabase/metabase