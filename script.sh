#!/bin/bash

simple=('dsnmap')
intermediate=.simple+('autre' 'etc...')

if [ -z $1 ]
then
  param='simple'
fi

for program in simple
do
  sudo apt install $program
  printf "[+] " $programe
done

printf "[+] done" 
