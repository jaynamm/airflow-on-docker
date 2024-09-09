FROM apache/airflow:2.10.0

USER root
RUN apt-cache search openjdk
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    openjdk-17-jdk \
    procps \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

USER airflow

RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark