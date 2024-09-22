FROM quay.io/jupyter/datascience-notebook:2024-08-30

USER jovyan

WORKDIR /home/jovyan/work

COPY ./requirements.txt ./

RUN conda install --file ./requirements.txt

COPY ./ ./