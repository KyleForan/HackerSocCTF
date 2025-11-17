FROM ubuntu AS app
RUN apt-get update && apt-get install -y gcc-multilib && rm -rf /var/lib/apt/lists/*

FROM pwn.red/jail
ENV JAIL_TIME=150

COPY --from=app / /srv
COPY level2 /srv/app/run
COPY flag /srv/app/flag
RUN chmod 755 /srv/app/run
