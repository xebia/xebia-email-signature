FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /srv
COPY . /srv

RUN pip install build && python -m build .


FROM public.ecr.aws/docker/library/python:3.9-slim

COPY --from=0 /srv/dist/*.whl /tmp/installer/

RUN pip install gunicorn /tmp/installer/*.whl && rm -rf /tmp/installer*

ENV PORT=8080
EXPOSE 8080
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD ["exec gunicorn --bind 0.0.0.0:${PORT} xebia_email_signature.serve:app"]
