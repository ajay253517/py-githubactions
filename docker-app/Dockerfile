FROM python:3.10-buster
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["app.py"]
