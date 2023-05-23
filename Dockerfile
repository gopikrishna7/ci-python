FROM python:alpine3.17
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
CMD [ "flask","run","--host=0.0.0.0" ]