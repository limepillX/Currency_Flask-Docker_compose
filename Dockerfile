FROM python:3.9.7
ADD ./ code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py