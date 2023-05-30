FROM python:3.10.4

WORKDIR /TERRAFORM

ADD . /TERRAFORM/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 6000

CMD ["tail", "-f", "/dev/null"]