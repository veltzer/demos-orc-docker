FROM python:3-alpine

# upgrade pip to latest version and configure it to shut up
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip

# install requirement
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# install your app
COPY app.py /app
WORKDIR /app
CMD ["./app.py"]
