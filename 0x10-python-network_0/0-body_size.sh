#!/bin/bash
# Check if the argument is provided
curl -s "$1" | wc -c