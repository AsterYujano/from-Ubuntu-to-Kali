#!/bin/bash

simple=('dsnmap')
#intermediate=.simple+('autre' 'etc...')

if [ -z $1 ]
then
  param='simple'
fi

for i in ${simple[@]}
do
  sudo apt install $i
  printf "[+] " $i
done

printf "[+] done" 
