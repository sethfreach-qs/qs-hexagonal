FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /usr/src/app

COPY . .

CMD [ "flask", "--app", "src.adapters.api.application", "run", "--host", "0.0.0.0" ]

EXPOSE 5000

