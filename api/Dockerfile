FROM python:3.12.0-bullseye
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
#RUN pip install twisted[http2,tls]
COPY . /code/

EXPOSE 8000
RUN pip install supervisor
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY /docker-entrypoint.sh /code/docker-entrypoint.sh
# Command to run supervisor
RUN pip install supervisor
RUN chmod +x /docker-entrypoint.sh

#CMD ["supervisord"]
CMD ["/code/docker-entrypoint.sh", "supervisord", "-c", "/etc/supervisor/supervisord.conf"]
#CMD ["python", "manage.py", "runserver"]
