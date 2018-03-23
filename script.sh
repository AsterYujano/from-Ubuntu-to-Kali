#!/bin/bash

simple=('dirbuster' 'burpsuite')
intermediate=.simple+('autre' 'etc...')

#Check parameters

if [ -z $1 ]
then
  #choisir le parametre simple
  param='simple'
fi

for program in simple
do
  sudo apt install $program
done
