FROM python:3.9.4

WORKDIR /

ADD . .

RUN pip install -r requirements.txt

CMD ["python","/src/server.py"]