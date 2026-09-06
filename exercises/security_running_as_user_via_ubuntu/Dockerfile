FROM ubuntu:24.04
RUN useradd mark
RUN mkdir /home/mark
COPY app.sh /home/mark
RUN chown -R mark:mark /home/mark
USER 1000
WORKDIR /home/mark
CMD ["./app.sh"]
