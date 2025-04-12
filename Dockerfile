FROM mariadb:10.4

ENV MYSQL_ROOT_PASSWORD=
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
ENV MYSQL_DATABASE=pygame

# Copy the init SQL file into the container. This file will be executed
# when the container starts and sets up your database.
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306