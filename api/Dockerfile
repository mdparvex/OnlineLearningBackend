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
# Command to run supervisor
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
#CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "live_transcribe.asgi:application"]
