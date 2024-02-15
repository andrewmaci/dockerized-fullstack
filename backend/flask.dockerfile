FROM python:3.12
EXPOSE 4000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "flask","run","--host=0.0.0.0","--port=4000" ]