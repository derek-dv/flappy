FROM python

RUN apk add python3-dev

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ['python3']
CMD ['main.py']