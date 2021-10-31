FROM python:3.9.7-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "final_model.bin", "./"]

EXPOSE 1208

ENTRYPOINT ["gunicorn", "predict:app"]
