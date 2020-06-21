# SeeFood

## TensorFlow Serve instructions:

- [Install docker](https://docs.docker.com/engine/install/) 
- ```sudo docker ps```
- ```sudo docker run -p 8501:8501 --name=seefood -v "PATH_TO_MODEL/models/:/models/seefood/1" -e MODEL_NAME="seefood" tensorflow/serving```
 