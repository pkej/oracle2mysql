# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:2.7.13
RUN mkdir -p opt/oracle
ADD ./oracle/linux/ ./app
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py
ENV LD_LIBRARY_PATH="/opt/oracle/instantclient"
ENV OCI_HOME="/opt/oracle/instantclient"
ENV OCI_LIB_DIR="/opt/oracle/instantclient"
ENV OCI_INCLUDE_DIR="/opt/oracle/instantclient/sdk/include"
ENV OCI_VERSION=12
RUN cd /app \
    && chmod a+x env-vars-linux.sh \
    && apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y unzip \
    && apt-get install -y curl \
    && apt-get install -y libaio1 \
    && unzip instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/oracle \
    && unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip -d /opt/oracle  \
    && mv /opt/oracle/instantclient_12_2 /opt/oracle/instantclient \
    && ln -s /opt/oracle/instantclient/libclntsh.so.12.1 /opt/oracle/instantclient/libclntsh.so \
    && ln -s /opt/oracle/instantclient/libocci.so.12.1 /opt/oracle/instantclient/libocci.so \
    && sh -c "echo /opt/oracle/instantclient > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache \
    && chmod a+x app.py \
    && more /app/env-vars-linux.sh >> /root/.bashrc