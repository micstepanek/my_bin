#!/usr/bin/env bash
if [ -t 0 ]
then
  exit 0
fi
urxvtc -e run_and_await_key.sh $1
exit 1

