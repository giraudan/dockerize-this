FROM python:3.9.7-buster
RUN useradd -m -U normaluser
RUN mkdir -p /webapp
RUN chown -R normaluser\: /webapp
USER normaluser
WORKDIR /webapp
ADD requirements.txt /webapp/requirements.txt
RUN pip install --user -r requirements.txt
ADD . /webapp
EXPOSE 8080
CMD [ "/usr/local/bin/python3", "main.py" ]
