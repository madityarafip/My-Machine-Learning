FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predictQ6_with_flask_hw5.py", "dv.bin", "./"]

EXPOSE 1208

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1208", "predictQ6_with_flask_hw5:app"]