FROM python:3.8-slim

WORKDIR /quest

ADD tower_of_containers ./tower_of_containers
ADD hero.PNG .
ADD quest.py .

ENTRYPOINT ["python", "quest.py"]