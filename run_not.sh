#!/bin/bash

python script_n.py| mysql --defaults-file=~/replica.my.cnf -h cswiki.labsdb cswiki_p | sed '1d'
