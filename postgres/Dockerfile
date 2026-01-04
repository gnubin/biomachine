FROM postgres:16-alpine

# =========================
# Environment
# =========================
ENV POSTGRES_DB=biomachine \
  POSTGRES_USER=biomachine \
  POSTGRES_PASSWORD=biomachine_password

# =========================
# Init scripts
# =========================
COPY init.sql /docker-entrypoint-initdb.d/

# =========================
# Expose
# =========================
EXPOSE 5432

