FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pytest \
    && mkdir /myapp
COPY module /myapp/module
COPY tests /myapp/tests
WORKDIR /myapp
CMD ["PYTHONPATH=.","python","-m","pytest"]
