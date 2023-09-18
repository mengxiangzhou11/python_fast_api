FROM python:3.7

WORKDIR ./python_fast_api

ADD . .

#pip更改为阿里云镜像源
RUN pip install -U pip
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com


RUN pip install -r requirements.txt
#docker build -t fast_api_wzz:v1 .
#docker run -p 9090:9090 fast_api_wzz:v1

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=9090"]