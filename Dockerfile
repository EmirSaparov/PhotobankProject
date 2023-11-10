FROM python:3.11
LABEL authors="Emir Saparov"
ENV DISPLAY=:99
WORKDIR /photobank_autotests
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python -m pytest -s -v --alluredir=allureress smoke_test.py
