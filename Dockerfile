FROM redhat/ubi8

RUN apt install python3 -y

RUN pip install flask

COPY first.py /app.py

CMD ["python3","app.py"]
