FROM ctf2204:latest

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev
RUN pip3 install pwntools
RUN pip3 install ROPgadget
RUN cd $HOME && echo "export PATH=$PATH:/usr/local/lib/python3.10/dist-packages/bin/" >> .bashrc
