#!/bin/bash

# Create an alias called xkcd which runs the shell command ./xkcd.sh
alias xkcd="./xkcd.sh"

python3 -m venv venv

. venv/bin/activate
pip3 install -r requirements.txt
clear
echo Heyy 👋
echo Setup for xkcd-cli is complete 🥳
