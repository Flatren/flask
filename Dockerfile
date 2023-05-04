FROM python:3-alpine

ENV DBNAME railway
ENV HOST https://containers-us-west-123.railway.app
ENV USER postgres
ENV PASSWORD WjxmdLfc4ExkKiEwIVvo
ENV PORT 8006
ENV PORT_EXEC 5000

WORKDIR /app
COPY . /app


RUN pip3 install --no-cache-dir -r /app/req.txt
RUN apk add --no-cache alpine-conf && \
    setup-timezone -z Europe/Moscow
ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]