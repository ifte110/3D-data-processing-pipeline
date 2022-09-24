FROM ubuntu

RUN mkdir /file

COPY scan_1.bin /file

COPY scan_2.bin /file

COPY scan_3.bin /file

RUN apt-get update && apt-get install -y cloudcompare

RUN apt-get update && apt-get install -y xvfb
