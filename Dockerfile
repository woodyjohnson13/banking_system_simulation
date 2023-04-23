#kind of like parent image
FROM python

WORKDIR /banking_system_simulation

#source code layer
COPY . .

RUN pip install pillow

EXPOSE 4000

CMD ["python','./main.py"]