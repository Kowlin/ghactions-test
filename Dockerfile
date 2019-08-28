FROM python:3.7.4-alpine3.10

COPY LICENSE README.md /

COPY entrypoint.sh /entrypoint.sh
COPY mainscript.py /mainscript.py

CMD ["python", "./script.py"]
