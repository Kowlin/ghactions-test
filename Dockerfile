FROM python:3.7.4-alpine3.10

COPY LICENSE README.md /

COPY entrypoint.sh /entrypoint.sh
COPY script.py /script.py

RUN ["chmod", "+x", "/entrypoint.sh"]
RUN ["chmod", "+x", "/script.py"]

ENTRYPOINT ["sh", "/entrypoint.sh"]
