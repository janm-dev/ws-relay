FROM bitnami/python:3.9-prod

ENV WS_PORT=80
EXPOSE 80

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./ /app/

HEALTHCHECK --interval=10s --timeout=2s --start-period=5s --retries=3 \
	CMD curl http://localhost/healthcheck -sf || exit 1

ENTRYPOINT [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker" ]
CMD [ "qna:qna" ]
