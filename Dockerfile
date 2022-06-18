FROM python:3.8-alpine
COPY ./docker/requirements.txt /app/requirements.txt
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./docker/ /app
ENTRYPOINT [ "python" ]
CMD ["main.py"]
