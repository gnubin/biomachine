FROM postgres:16-alpine

ENV POSTGRES_DB=biomachine \
  POSTGRES_USER=biomachine \
  POSTGRES_PASSWORD=biomachine_password

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

