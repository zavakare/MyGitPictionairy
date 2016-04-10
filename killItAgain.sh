#!/usr/bin/env bash

ps -elf | grep python | grep -v grep | awk '{print $4}' | xargs kill -9
./ChooseCat.py

