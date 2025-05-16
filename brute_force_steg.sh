#!/bin/bash

STEG_PROGRAM="./Steg.py" #name of the steg program
INPUT_FILE="output.bmp" #name of the wrapper file
FILE_TYPE="txt" #file type of the  output file change to bmp/jpeg/txt

MAX_OFFSET=2048 #maximum offset to test
MAX_INTERVAL=256 #maximum interval to test
MODE=b #b for bit mode, B for byte mode
OFFSET_ADDITION=0 #change if offset will be <power of 2 + #>
INTERVAL_ADDITION=0 #same here as offset

OFFSET=1 #starting offset
while [ $OFFSET -le $MAX_OFFSET ]; do
	INTERVAL=1 #starting interval
	while [ $INTERVAL -le $MAX_INTERVAL ]; do
		echo "Running with mode=$MODE, offset=$OFFSET, interval=$INTERVAL"
		python3 $STEG_PROGRAM -r -$MODE -o$((OFFSET + OFFSET_ADDITION)) -i$((INTERVAL + INTERVAL_ADDITION)) -w$INPUT_FILE > "output_${MODE}_interval${INTERVAL}_offset${OFFSET}.${FILE_TYPE}"
		INTERVAL=$((INTERVAL * 2)) #squares interval, to reach the next power of two, will need to change if testing for something else
	done
OFFSET=$((OFFSET * 2)) #same here as interval
done

#this will generate A LOT of files, make sure to put in its own directory

#when finding image files, the icon in the directory will show if a compatible image was generated

#if testing for txt files use the command: grep -rEl --include="*.txt" '^[[:print:][:space:]]{20,}$' /path/to/directory
#will find all files with printable text, will narrow it down to the correct interval, and will just have to check each offset

#to run the script, make sure it is executable with chmod +x brute_force_steg.sh
#then type ./brute_force_steg.sh in terminal
