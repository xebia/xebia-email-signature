FROM python:3.10-alpine3.16

RUN apk --no-cache add tidyhtml-dev

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD signature.py /
ADD signature.tpl /

ENTRYPOINT [ "python", "./signature.py" ]
