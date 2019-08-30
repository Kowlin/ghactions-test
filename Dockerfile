FROM python:3.7.4-alpine3.10

COPY LICENSE README.md /

COPY entryscript.py /entryscript.py
COPY requirements.txt /requirements.txt

RUN ["chmod", "+x", "/entryscript.py"]
RUN ["pip3.7", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python3.7", "/entryscript.py"]
