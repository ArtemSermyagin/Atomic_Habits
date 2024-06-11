FROM python:3

WORKDIR /Atomic_Habits

COPY ./requirements.txt /DRF/

RUN pip install -r requirements.txt

COPY . .

