FROM python:3.10

COPY ./src/ /opt/TFG/src/
COPY ./data/ /opt/TFG/data/

WORKDIR /opt/TFG/src/
RUN pip install --no-cache-dir pipenv \
    && python3 -m pipenv lock \
    && python3 -m pipenv requirements > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt \
    && touch .env \
    && echo "#Ruta del fichero YAML" >> .env \
    && echo 'PHISHING_QUIZ_EMAILS="/opt/TFG/data/phishing_quiz/emails.yml"' >> .env \
    && echo "#Ruta del directorio con los ficheros YAML" >> .env \
    && echo 'MODULES_DATA_FOLDER="/opt/TFG/data/modules"' >> .env \
    && python3 -m flask db init \
    && python3 -m flask courses db load \
    && python3 -m flask phishing_quiz db load

CMD [ "python3", "-m" , "gunicorn", "-w", "2", "-b", "0.0.0.0", "flaskapp:create_app()"]