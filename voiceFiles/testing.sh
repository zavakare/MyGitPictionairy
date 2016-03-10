#!/bin/bash
arecord -D plughw:1 --duration=5 test.wav  	

#arecord -d4 -f dat -t wav -r 48000 -c 2 | sox - -b16 -r16k -c1 -t wav - | flac - -o test.flac
flac test.wav test.flac



INFILE=test.flac
DURATION=3
LANGUAGE=en_US
# Please replace this with your own key
KEY=AIzaSyCcOs_yyz7P5aBHcVECUHO1FSZmkcvTibU

#flac -0 test.wav


#RESULT=`wget -q --post-file $INFILE --header="Content-Type: audio/x-flac; rate=$SRATE" -O - "https://www.google.com/speech-api/v2/recognize?client=chromium&lang=$LANGUAGE&key=$KEY"`
#FILTERED=`echo "$RESULT" | grep "transcript.*}" | sed 's/,/\n/g;s/[{,},"]//g;s/\[//g;s/\]//g;s/:/: /g' | grep -o -i -e "transcript.*" -e "confidence:.*"`


#wget -O – -o /dev/null –post-file lol.flac –header="Content-Type: audio/x-flac; rate=16000" "http://www.google.com/speech-api/v2/recognize?client=chromium&lang=en-US&key=AIzaSyCcOs_yyz7P5aBHcVECUHO1FSZmkcvTibU&output=json" > out.json | cut -d " " -f12 >> stt.txt


#mine experimenting with GOOGLE API
wget -q --post-file test.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v2/recognize?client=chromium&lang=en-US&key=AIzaSyCcOs_yyz7P5aBHcVECUHO1FSZmkcvTibU" 


echo -n “You Said: ”
cat stt.txt

#echo "$FILTERED"



#echo "yo" 
