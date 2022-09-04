FROM ubuntu

WORKDIR /files

COPY panel_artec_scan.obj /files/

RUN apt-get update && apt-get install -y cloudcompare

RUN apt-get update && apt-get install -y xvfb
