#! /bin/bash

# echo "The time is 'date'"

# test -c/oot && echo "Існує така папка"  || echo "Нема такої папки "

# echo $?

# touch /d/git/public90/sh/file  && echo "File created or updated" || echo "Can't get access"

if echo $1 | grep 'T'
    then echo 'Є така буква в слові'
    else echo 'Нема такої букви '
fi 