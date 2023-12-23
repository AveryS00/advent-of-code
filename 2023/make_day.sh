#!/bin/zsh

cargo new day${1}
curl -c "session=$(<session_cookie.txt)" https://adventofcode.com/2023/day/${1}/input > day${1}/input.txt

