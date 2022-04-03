FROM ubuntu:focal

RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get clean
RUN useradd -m bacteria

ADD share/bacteria /home/bacteria/bacteria
ADD share/flag /flag
ADD share/getflag /getflag
ADD share/run.sh /home/bacteria/run.sh
ADD xinetd /etc/xinetd.d/bacteria

RUN chown -R bacteria:bacteria /home/bacteria/
RUN chown root:root /getflag
RUN chown root:root /flag
RUN chmod 400 /flag
RUN chmod 4755 /getflag

USER bacteria
WORKDIR /home/bacteria/

CMD ["/usr/sbin/xinetd", "-dontfork"]
