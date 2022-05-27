FROM python:3.10

ADD Database.py .

ENTRYPOINT python Database.py

CMD ["python","./Database.py"]
