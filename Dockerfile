FROM python:3.9
EXPOSE 8502

RUN apt-get update && apt-get install -y nano
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY . /katana_web_demo
WORKDIR /katana_web_demo

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port", "8502"]