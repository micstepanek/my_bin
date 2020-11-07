#!/usr/bin/env bash
#
cd ~/aa/background
pdflatex pc_list.tex

convert           \
   -verbose       \
   -density 150   \
   -trim          \
    pc_list.pdf\
   -quality 100   \
   -flatten       \
   -sharpen 0x1.0 \
    pc_list.png
    
feh --bg-tile pc_list.png
