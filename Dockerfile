#pull base image
FROM python:3.8

#set environment variable
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

#set working directory
WORKDIR /code

#install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#copy project       
COPY . /code/
