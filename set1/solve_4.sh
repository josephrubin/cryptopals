best_score=0
best_plain=""
while read line
do
    #echo $line
    plain=$(echo $line | frombase -x | xchar -c)
    score=$(echo $plain | python3 ./score.py)
    #echo $score
    #echo
    
    if [ $score -gt $best_score ]
    then
        best_score=$score
        best_plain=$plain
    fi
done < 4.txt
echo BEST SCORE: $best_score
echo $best_plain
