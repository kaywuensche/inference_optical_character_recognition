# Inference for Optical Character Recognition

API for Optical Character Recognition.

In combination with an API for [Object Detection](https://github.com/BMW-InnovationLab/BMW-YOLOv4-Inference-API-CPU) it can be used e.g. for Document Layout Analysis.

## Prerequisites:
- docker
- docker-compose

### Check for prerequisites
To check if docker-ce is installed:

```docker --version```

To check if docker-compose is installed:

```docker-compose --version```

### Install prerequisites
**Ubuntu**

To install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/) on Ubuntu, please follow the link.

**Windows 10**

To install Docker on [Windows](https://docs.docker.com/docker-for-windows/install/), please follow the link.

## Build The Docker Image
In order to build the project run the following command from the project's root directory:

```sudo docker-compose up --build --remove-orphans```

## API Endpoint
To see the available endpoint, open your favorite browser and navigate to:

```http://<machine_IP>:5001/docs```

You can change the port in the docker compose file.

Also you can test the endpoint with image files from the test directory.

**/optical_character_recognition (POST)**

This endpoint performs inference on specified language and uploaded image and returns extracted text:

<img width="964" alt="ocr" src="https://user-images.githubusercontent.com/58667455/120218792-8a5a5680-c23a-11eb-9156-c0f0c02e7308.png">

