FROM python:3.9.17
LABEL maintainer Neil
ENV PYTHONUNBUFFERED 1
RUN mkdir /project
RUN apt-get -y update
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime
WORKDIR /project
COPY . /project
RUN python -m pip install --upgrade pip
RUN chmod a+x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
