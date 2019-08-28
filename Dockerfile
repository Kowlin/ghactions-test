FROM python:3.7.4-alpine3.10

COPY . .

CMD ["./entrypoint.sh"]
