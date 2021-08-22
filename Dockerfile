FROM bitnami/python:3.9-prod

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./ /app/

HEALTHCHECK --interval=10s --timeout=2s --start-period=5s --retries=3 \
	CMD curl http://localhost:8000/healthcheck -sf || exit 1

ENTRYPOINT [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker" ]
CMD [ "qna:qna" ]
