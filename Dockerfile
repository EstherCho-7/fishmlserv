FROM python:3.9

WORKDIR /code

COPY . /code/

#COPY ./requirements.txt /code/requirements.txt

RUN pip install --nocache-dir --upgrade -r /code/requirements.txt


CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8765"]
