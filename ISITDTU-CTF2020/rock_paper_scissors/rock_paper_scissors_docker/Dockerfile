FROM ubuntu:latest

MAINTAINER quynhnhu

RUN apt-get update -y
RUN apt install gdb -y
RUN apt-get install tzdata -y
ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN useradd -m rock_paper_scissors

COPY ./share/flag /flag
COPY ./share/run.sh /home/rock_paper_scissors/run.sh
COPY ./share/rock_paper_scissors /home/rock_paper_scissors/rock_paper_scissors

COPY ./init.sh /init.sh

RUN chmod +x /init.sh
RUN chmod +x /home/rock_paper_scissors/run.sh

RUN chown -R root:rock_paper_scissors /home/rock_paper_scissors
RUN chmod -R 755 /home/rock_paper_scissors
RUN chmod 644 /flag

RUN echo rock_paper_scissors > /etc/cron.deny
RUN chmod 644 /etc/cron.deny

RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /dev/shm

WORKDIR /home/rock_paper_scissors

#CMD ["/init.sh"]

EXPOSE 12345
