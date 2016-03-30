#!/usr/bin/env bash

#ps -elf | grep NewMotion | grep -v grep | awk '{print $4}' | xargs kill -9
ps -elf | grep python | grep -v grep | awk '{print $4}' | xargs kill -9
./ChooseCat.py
