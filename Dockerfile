# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Tensorflow with pip
# hadolint ignore=DL3013
RUN pip install --no-cache-dir tensorflow && \
    pip install tf-keras &&\
    fix-permissions "${CONDA_DIR}" &&\
    fix-permissions "/home/${NB_USER}" 
    

RUN pip install gensim==4.3.2 && \
    pip install sentence-transformers==2.2.2 && \
    pip install xgboost==2.0.3 && \
    pip install seaborn==0.13.0
