FROM python:3.9

COPY . /src
COPY ./requirements.txt /src/requirements.txt
WORKDIR /src

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
