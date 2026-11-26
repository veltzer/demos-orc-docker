FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flask \
    && mkdir app
WORKDIR /app
COPY app.py .
CMD ["./app.py"]
