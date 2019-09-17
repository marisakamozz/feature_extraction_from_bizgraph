# Feature Extraction from business relationship graphs by GCN
We show the source code used in the paper 
"Feature extraction from business relationship graphs by Graph Convolutional Networks"
in this repository.

## 1. Instructions

### 1.1. Change jupyter notebook password

Open `docker/jupyter_notebook_config.py`, and edit following line to your own password.

```
c.NotebookApp.password = u'sha1:e9d062fde561:61de018d8d0e7c6d355fa7a22bb383a9f193ce46' # change on install
```

You can use following commands to get hashed passwords in python interactive mode.

```
from notebook.auth import passwd
passwd()
```

### 1.2. Build docker image and run docker container

Build docker image and run docker container according to the following commands.

```
docker build -t docker-image docker
nvidia-docker run -v $(pwd):/project -p 8888:8888 docker-image
```

### 1.3. Open jupyter notebook

Open your browser, and access to `http://localhost:8888/`.
Enter your own password.

Then, you can see the directory of this repository.
Open `train.ipynb` file.
This notebook is the source code used in the paper.

## 2. Requirements

In order to execute above instructions and the notebook,
a machine that meets the following conditions is required.

- CUDA 10.0
- NVIDIA-Docker

It has been confirmed that it runs on "Azure Data Science Virtual Machine (Ubuntu)" and NC6 Virtual Machine.