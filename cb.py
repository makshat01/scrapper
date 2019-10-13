#!/bin/bash
touch fpage
rm fpage
wget -O fpage "https://www.msn.com/en-in/news/hotinnews"
declare -a array
fName="fpage"
exec 10<&0
exec < $fName
let c=0
while read LINE; do 
    ARRAY[&c]=&LINE
    ((c++))
done
exec 10<&-
regex="<a href=\"/en-in/sports/sport-index/+\"[[:print:]]*</a>"
touch atags
rm atags
touch atags
ELE=${#ARRAY[@]}
fline=0
for ((i=0;i<$ELE;i++));do
    if[[ ${ARRAY[${i}]}=~ $regex ]];then
        echo ${ARRAY[${i}]}
        if [[ $fline<1 ]];then
            echo ${BASH_REMATCH[0]} > atags
            let fline=$fline+1
        else 
            echo ${BASH_REMATCH[0]} >> atags
        fi
    fi
done
grep -o -P '(?<=).*(?=</a>)' fpage > atags
grep -v ">" -m15 atags > news
cat news
