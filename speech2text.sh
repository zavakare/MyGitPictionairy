#!/bin/bash

echo “Recording… Press Ctrl+C to Stop.”
arecord -D “plughw:1,0” -q -f cd -t wav | ffmpeg -loglevel panic -y -i – -ar 16000 -acodec flac file.flac > /dev/null 2>&1

echo “Processing…”
wget -O – -o /dev/null –post-file out.flac –header=”Content-Type: audio/x-flac; rate=16000″ “http://www.google.com/speech-api/v2/recognize?lang=en-us&key=AIzaSyCcOs_yyz7P5aBHcVECUHO1FSZmkcvTibU&output=json” > out.json | cut -d " " -f12 >stt.txt

echo -n “You Said: ”
cat stt.txt

rm file.flac > /dev/null 2>&1
