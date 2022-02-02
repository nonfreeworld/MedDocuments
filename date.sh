#!/bin/bash
python pfdsh.py
read -p "Введите фамилию пациента "
cp test.pdf test1.pdf
mv test1.pdf $REPLY.pdf

