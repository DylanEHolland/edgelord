#!/usr/bin/env sh

export PYTHONPATH="./";
. etc/settings.sh;
python tests/$1.py;
