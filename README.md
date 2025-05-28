# DocFlow: Extracting Taint Specifications from Software Documentation

Evaluation of Information Flows Specifications from Software Documentation

## Supplementary Material

This is a fork of the repository of the DocFlow analysis framework and supplementary material for the paper: 
Tileria, Marcos, Jorge Blasco, and Santanu Kumar Dash. “DocFlow: Extracting Taint Specifications from Software Documentation.”
[Link to article](https://www.computer.org/csdl/proceedings-article/icse/2024/021700a718/1RLIWDGe50s) ,
and temporal [file](evaluation/ICSE_DocFlow_camera_ready.pdf)

DocFlow is an NLP framework to classify methods based on their documentation. 


## Core Features

DocFlow includes:
- Taint specification generator [script](core/docflow.py)
- Android documentation crawler for [AOSP](core/aosp_crawler.py) and [Google-libraries](docflow/core/gps-crawler.py)
- Sensitive methods classifier [script](core/methods_classifier.py)
- Semantic category classifier [script](core/semantic_classifier.py)
- Semantic search  [script](core/semantic_search.py)
- Notebook to reproduce results from the paper. [paper_results](experiments/paper_results.ipynb)


## Getting started


1. Clone this repo: `git clone https://gitlab.com/s3lab-rhul/android/docflow`
2. Create the docker image. Run the following command in the directory that contains the Dockerfile
    `docker build -t docflow_img .` 
3. Go to the file [init_container.sh](init_container.sh) and set your local path pointing to the repository
4. run `./init_container.sh`
5. Go to http://localhost:8888/lab or the link showed in the terminal
6. Open the [paper_results.ipynb](experiments/paper_results.ipynb) and follow the instructions



## Usage


Run the notebook [paper_results](experiments/paper_results.ipynb) in the folder __experiments__ and follow the instruction
To stop/restar the container you can run the following commands. The container name can be found in the [init_container.sh](init_container.sh) script. 

```
docker stop <container_name>
docker restart <container_name>
```


To use DocFlow as a standalone tool run the script [docflow.py](core/docflow.py)
Use -h to see the available options.   
Detailed instruction on how to use DocFlow and expected input/ouput will be added soon. 



