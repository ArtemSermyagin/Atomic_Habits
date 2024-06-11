FROM python:3

WORKDIR /Atomic_Habits

COPY ./requirements.txt /Atomic_Habits/

RUN pip install -r requirements.txt

COPY . .

