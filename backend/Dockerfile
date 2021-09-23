FROM python:3.9.7-buster
RUN useradd -m -U skysoft
RUN mkdir -p /backend
RUN chown -R skysoft\: /backend
USER skysoft
WORKDIR /backend
ADD requirements.txt /backend/requirements.txt
RUN pip install --user -r requirements.txt
ADD . /backend
EXPOSE 8080
CMD [ "/usr/local/bin/python3", "main.py" ]
