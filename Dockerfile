FROM python:3.9

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME World

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
