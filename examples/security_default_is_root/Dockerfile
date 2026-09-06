FROM ubuntu:24.04
RUN apt-get update -y && apt-get install --no-install-recommends -y libcap2-bin systemd-sysv iproute2 && rm -rf /var/lib/apt/lists/*
COPY app.sh /
CMD ["/app.sh"]
