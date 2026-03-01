FROM postgres:17-alpine

ENV POSTGRES_DB=biomachine \
    POSTGRES_USER=biomachine \
    POSTGRES_PASSWORD=biomachine_password

EXPOSE 5432

VOLUME ["/var/lib/postgresql/data"]

CMD ["postgres"]