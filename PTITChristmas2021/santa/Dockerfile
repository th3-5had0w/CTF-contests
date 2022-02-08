FROM ubuntu:18.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY santa .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 9998
CMD ./ynetd -p 9998 ./santa
