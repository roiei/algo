# Read from the file file.txt and output the tenth line to stdout.
cnt=0
while read  LINE; do
    if [ -z "$LINE" ]; then continue; fi
    if [ $cnt -eq 9 ]; then
        echo $LINE
    fi
    ((cnt++))
done < file.txt