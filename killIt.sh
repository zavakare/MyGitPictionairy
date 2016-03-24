#!/usr/bin/bash

ps -elf | grep NewMotion | grep -v grep | awk '{print $4}' | xargs kill -9

