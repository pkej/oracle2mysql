# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:2.7.13
LABEL version="1.0"
LABEL description="ETLAlchemy"
LABEL tag "ETLAlchemy:latest"
#ENV PATH /usr/local/bin:$PATH
#ENV LANG C.UTF-8

RUN mkdir -p opt/oracle
ADD ./oracle/linux/ ./app
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

RUN dd if=/dev/zero of=/tmp/tempswap.img bs=1024 count=11M \
    && mkswap /tmp/tempswap.img \
    && swapon /tmp/tempswap.img

RUN apt-get update \
#    && apt-get install -y software-properties-common \
#    && add-apt-repository ppa:deadsnakes/ppa \
#    && apt-get install -y python2.7 \
    && apt-get install -yd mariadb-server \
    && apt-get install -y build-essential \
    && apt-get install -y unzip \
    && apt-get install -y curl \
    && apt-get install -y libaio1 
    #&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache

RUN cd /app \
    && unzip /app/instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/oracle \
    && unzip /app/instantclient-sdk-linux.x64-12.2.0.1.0.zip -d /opt/oracle  \
    && mv /opt/oracle/instantclient_12_2 /opt/oracle/instantclient \
    && ln -s /opt/oracle/instantclient/libclntsh.so.12.1 /opt/oracle/instantclient/libclntsh.so \
    && ln -s /opt/oracle/instantclient/libocci.so.12.1 /opt/oracle/instantclient/libocci.so \
    && sh -c "echo /opt/oracle/instantclient > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig \
    && chmod a+x app.py \
    && more /app/env-vars-linux.sh >> /root/.bashrc \
    && gzip -d mysql-utilities-1.6.5.tar.gz \
    # && tar -x mysql-utilities-1.6.5.tar \
    # && cd /app/mysql-utilities-1.6.5 \
    # && python setup.py \
    && rm /app/*.zip

ENV LD_LIBRARY_PATH="/opt/oracle/instantclient"
ENV OCI_HOME="/opt/oracle/instantclient"
ENV OCI_LIB_DIR="/opt/oracle/instantclient"
ENV OCI_INCLUDE_DIR="/opt/oracle/instantclient/sdk/include"
ENV OCI_VERSION=12

RUN cd /app \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache