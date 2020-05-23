#!/bin/sh
# Inspired by Luke Smith's video "https://youtu.be/UCEXY46t3OA"

cat emoji_list | dmenu -i -l 20 -fn Monospace-14 | awk '{print $1}u' | tr -d '\n' | xclip -selection clipboard
pgrep -x dunst > /dev/null && notify-send "$(xclip -o -selection clipboard) 已複製到剪貼簿"
