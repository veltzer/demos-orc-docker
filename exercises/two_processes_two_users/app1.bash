#!/usr/bin/env bash

i=0

while true
do
	echo "hello, from app 1 (${i}) uid ${UID}"
	sleep 1
	((i++))
done
