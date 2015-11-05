#!/bin/bash
#Mitchell Childerhose, 100553756
cat $3 | tail -n +$1 | head -n -$2 
