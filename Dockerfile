FROM apache/airflow:2.9.2

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
ENV HADOOP_HOME /opt/hadoop-3.3.6
ENV HADOOP_COMMON_LIB_NATIVE_DIR /opt/hadoop-3.3.6/lib/native
ENV HADOOP_OPTS " -Djava.library.path=/opt/hadoop-3.3.6/lib/native"
ENV LD_LIBRARY_PATH /opt/hadoop-3.3.6/lib/native

USER root

RUN set -eux; \
    apt-get update && \
    apt-get install --yes --no-install-recommends \
    wget \
    openjdk-17-jdk

RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && \
tar xf hadoop-3.3.6.tar.gz && \
mv hadoop-3.3.6 /opt && \
rm -rf hadoop-3.3.6.tar.gz

USER airflow

COPY requirements.txt /

RUN set -eux; \
    pip install -r /requirements.txt
