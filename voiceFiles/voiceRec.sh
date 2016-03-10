#!/bin/bash

pocketsphinx_continuous -hmm /usr/local/share/pocketsphinx/model/en-us/en-us -lm 7511.lm -dict 7511.dic -samprate 16000/8000/48000 -kws_threshold 1e-20 -inmic yes >test.txt

ps -elf | grep pocketsphinx_co | grep -v grep | awk '{ print $4}' | xargs kill -9

cat test.txt

print "YAY! I killed a process! and printed the words translated!"
