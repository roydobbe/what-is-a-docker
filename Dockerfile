FROM python:3.8-slim

WORKDIR /quest

ADD tower_of_containment ./tower_of_containment
ADD hero.PNG .
ADD quest.py .

ENTRYPOINT ["python", "quest.py"]