FROM python:3.9.7-buster
RUN useradd -m -U skysoft
RUN mkdir -p /webapp
RUN chown -R skysoft\: /webapp
USER skysoft
WORKDIR /webapp
ADD requirements.txt /webapp/requirements.txt
RUN pip install --user -r requirements.txt
ADD . /webapp
EXPOSE 8080
CMD [ "/usr/local/bin/python3", "main.py" ]
