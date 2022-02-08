FROM ubuntu:18.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY rasengan .
COPY flag.txt .
COPY ynetd .
COPY hint.txt .

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 9999
CMD ./ynetd -p 9999 ./rasengan