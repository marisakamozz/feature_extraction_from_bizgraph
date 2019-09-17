FROM nvidia/cuda:10.0-cudnn7-runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         ca-certificates \
         libjpeg-dev \
         libpng-dev && \
     rm -rf /var/lib/apt/lists/*
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH
RUN conda update -n base -c defaults conda
COPY base.yaml /root/
RUN conda env update --file /root/base.yaml
ENV MLFLOW_TRACKING_URI /project/mlruns
EXPOSE 8888
COPY jupyter_notebook_config.py /root/.jupyter/
CMD jupyter notebook