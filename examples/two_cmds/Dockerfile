FROM python:3-alpine
COPY app.py /
# this example exists to show that only the last CMD takes effect
CMD ["/app.py", "one"]
# hadolint ignore=DL4003
CMD ["/app.py", "two"]
