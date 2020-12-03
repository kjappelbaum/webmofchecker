#!/bin/bash

echo "connect to http://localhost:8091"
docker run -d -p 8091:8091 -e PORT=8091 -e WORKERS=2 -e CONCURRENCY_LIMIT=2 --rm --name=webmofcheckerinstance mofchecker
