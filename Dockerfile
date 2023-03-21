FROM python:3.12-rc-slim-bullseye

RUN pip install Flask \
 && pip install mysql.connector

COPY . /usr/src/carstore_sys

WORKDIR /usr/src/carstore_sys

RUN mkdir -p /data/db

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8080 3306