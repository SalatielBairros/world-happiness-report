#!/bin/bash

cd /code/app/

npm run build

npm install -g serve

serve -s build -l 3000
