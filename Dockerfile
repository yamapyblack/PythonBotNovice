FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV PYTHONPATH=".:$PYTHONPATH"

COPY requirements.txt ./
COPY src ./src/

RUN pip install -r requirements.txt

CMD [ "python" , "src/main.py" ]
