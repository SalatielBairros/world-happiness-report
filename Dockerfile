FROM python:3.10.5
RUN pip install pip --upgrade
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./ ./app
WORKDIR ./app
CMD uvicorn main:app --host 0.0.0.0 --port 80