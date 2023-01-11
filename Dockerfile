FROM python:3.7.15

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
