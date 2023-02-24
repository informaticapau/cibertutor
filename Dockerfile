FROM python:3
WORKDIR /usr/
RUN git clone https://github.com/danielfeitopin/TFG.git

WORKDIR /usr/TFG/src/
RUN pip install --no-cache-dir pipenv \
    && python3 -m pipenv requirements > requirements.txt \
    && pip install --no-cache-dir -r requirements.txt

COPY ./data/ /usr/TFG/data/
RUN touch .env \
    && echo "#Ruta del fichero YAML" >> .env \
    && echo 'PHISHING_QUIZ_EMAILS="/usr/TFG/data/phishing_quiz/emails.yml"' >> .env \
    && echo "#Ruta del directorio con los ficheros YAML" >> .env \
    && echo 'MODULES_DATA_FOLDER="/usr/TFG/data/modules"' >> .env \
    && python3 -m flask db init \
    && python3 -m flask courses db load \
    && python3 -m flask phishing_quiz db load

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
