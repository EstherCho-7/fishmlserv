#FROM python:3.11
FROM python:3.11.9-slim-bullseye

WORKDIR /code

#COPY . /code/
COPY src/fishmlserv/main.py /code/

#COPY ./requirements.txt /code/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/EstherCho-7/fishmlserv.git

CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8080"]
