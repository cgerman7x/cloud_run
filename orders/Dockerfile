FROM python:slim
ENV PORT 8080

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt


ENTRYPOINT uvicorn orders.app:app --host 0.0.0.0 --port "${PORT}"
