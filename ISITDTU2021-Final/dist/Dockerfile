FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y upgrade && apt-get -y install locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     
RUN apt-get install -y nginx lighttpd python3-pip curl
RUN mkdir -p /tmp/session/ && chmod -R 777 /tmp/session/
ADD ./flag /flag
RUN chmod 444 /flag
ADD ./flag2 /flag2
RUN chmod 400 /flag2
ADD ./flagreader /flagreader
RUN chmod 555 /flagreader && chmod +s /flagreader
CMD ["/run.sh"]
