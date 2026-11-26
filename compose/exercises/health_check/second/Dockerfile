FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir requests \
    && mkdir /app
COPY app.py /app
WORKDIR /app
CMD ["./app.py"]
