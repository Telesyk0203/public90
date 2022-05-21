#! /bin/bash
datatime_now=`date "+%Y-%m-%d %H:%M"`
git status
git add *
git commit -m "$datatime_now"
git push -u origin master  
