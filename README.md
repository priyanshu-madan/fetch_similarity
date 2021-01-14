# Fetch Rewards Coding Exercise - Data Engineer
This challenge will focus on the similarity between two texts. Your objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

## Installation process

### 1) Running via Docker Hub

#### Step 1. Download and install Docker for desktop: https://www.docker.com/products/docker-desktop

Installation video: https://www.youtube.com/watch?v=LtooWDUL1Js&ab_channel=NRDYTech

#### Step 2. Running Fetch Rewards Coding Exercise

Once the installation is complete. Open terminal / command-prompt and type in the following command:

```cmd
docker pull pmadan3/fetch-similarity
```

It will look something like this

![](readme_gifs/docker_pull.gif)

Next, we want to run the pulled docker container. Type in the following command:

```cmd
docker run --rm -p 8080:8080 pmadan3/fetch-similarity
```
![](readme_gifs/docker_run.gif)

When the command is successful, open your web browser and type in the following URL:

http://localhost:8080/

#### It will look something like this. Type in your texts as shown below and check their similarity

![](readme_gifs/flask_run.gif)

### Docker Repository link: https://hub.docker.com/r/pmadan3/fetch-similarity/builds

### 2) Running via GitHub pull

Open Terminal in a directory (I am opening mine in a Pycharm project).

In the terminal type the following commands one by one:

```cmd
git clone https://github.com/priyanshu-madan/fetch_similarity.git
cd fetch_similarity
pip install -r requirements.txt
python flask_page.py
```
#### Click on the link generated as shown below:

![](readme_gifs/git_clone.gif)


## FAQs
#### 1) Do you count punctuation or only words?
#### 2) Which words should matter in the similarity comparison? 
Everything except stopwords matter in the similarity comparison. Though they are being considered in this excersise. 
#### 3) Do you care about the ordering of words?
#### 4) What metric do you use to assign a numerical value to the similarity?
Cosine similarity is a metric used to measure how similar the texts are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity. (source: https://www.machinelearningplus.com/)

#### 5) What type of data structures should be used?
list and dictionaries have been used in this particular exercise.
list are being used to store tokens of the texts and generate matrix.
dictionaries are being used to store key value pair of the words and thier frequencies.

#### 6) I am getting this error when I run via docker, what should I do?

##### ERROR
```cmd
docker: Error response from daemon: driver failed programming external connectivity on endpoint dreamy_einstein (86be4eb3d4a322378723150912c1452c8a29d8b645b3adc649ea066faa2967e6): Bind for 0.0.0.0:8080 failed: port is already allocated.
```

##### SOLUTION
You need to make sure that the previous container you launched is killed, before launching a new one that uses the same port.
```cmd
docker container ls
docker rm -f <container-name>
```

