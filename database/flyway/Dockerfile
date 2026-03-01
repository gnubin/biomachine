FROM flyway/flyway:12.0-alpine

WORKDIR /flyway

COPY migrations /flyway/migrations

ENV DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=myapp_db \
    DB_USER=myapp_user \
    DB_PASSWORD=myapp_password \
    FLYWAY_CONNECT_RETRIES=60


