FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pyvardump
COPY app.py /
CMD ["/app.py"]
