FROM public.ecr.aws/lambda/python:3.7

RUN yum update && yum -y install \
        zip \
        unzip \
        wget \
        git

RUN pip install pytest rope flake8 autopep8