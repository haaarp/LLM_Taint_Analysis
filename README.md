# LLM_Taint_Analysis
This project aims to address the inference of the taint specifications by integrating LLMs with existing taint analysis frameworks and map comprehensive data flows within applications. 

# Getting started
1. Clone this repo: [`git clone [https://gitlab.com/s3lab-rhul/android/docflow](https://github.com/pei-ying-li/LLM_Taint_Analysis.git](https://github.com/pei-ying-li/LLM_Taint_Analysis.git)`](https://github.com/pei-ying-li/LLM_Taint_Analysis.git)
2. Create the docker image. Run the following command in the directory that contains the Dockerfile
    `docker build -t docflow_img .` 
3. Go to the file [init_container.sh](init_container.sh) and set your local path pointing to the repository
4. run `./init_container.sh`
5. Go to http://localhost:8888/lab or the link showed in the terminal
