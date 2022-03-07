FROM python:3.9-slim
ENV PROJECT_NAME=/template_project
RUN mkdir -p ${PROJECT_NAME}/app
WORKDIR ${PROJECT_NAME}

ADD requirements.txt ${PROJECT_NAME}
RUN pip install -r requirements.txt

ADD app ${PROJECT_NAME}/app
ADD gunicorn_entrypoint.sh ${PROJECT_NAME}

ENTRYPOINT ["bash","gunicorn_entrypoint.sh"]
