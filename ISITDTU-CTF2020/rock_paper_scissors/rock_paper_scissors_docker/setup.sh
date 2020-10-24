#!/bin/sh
#

sudo docker build -t "rock_paper_scissors" . && sudo docker run -d -p "0.0.0.0:12345:12345" --cap-add=SYS_PTRACE rock_paper_scissors
