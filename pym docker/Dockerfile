FROM ubuntu

RUN apt-get update

RUN apt-get install software-properties-common -y

RUN add-apt-repository universe -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip3 install pymeshlab

RUN apt update && apt install -y libgl1-mesa-dev