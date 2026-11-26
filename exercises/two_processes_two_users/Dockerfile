FROM ubuntu:24.04
RUN apt-get update -y && apt-get install --no-install-recommends -y adduser && rm -rf /var/lib/apt/lists/* \
    && adduser app1 \
    && adduser app2
COPY app1.bash /home/app1
COPY app2.bash /home/app2
RUN chown app1:app1 /home/app1 \
    && chown app2:app2 /home/app2
COPY run_two_apps.bash /
CMD ["/run_two_apps.bash"]
