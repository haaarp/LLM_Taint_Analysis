The /core directory contains the following scripts

1. aosp_crawler.py: Download the online documentation. The script include some urls for testing. The full list can be found in outputs/inputs/aosp_classes.txt
2. gps_crawler.py: Similar to aosp crawler. Full list is in inputs/gps-libraries.txt
3. core_utils.py: Several functions for pre-processing, metrics, and transformation
4. fine-tuning.py: script to fine-tune the SentenceBERT model
5. methods_classifier.py: classification of sources/sinks example with NN
6. semantic_classifier.py: semantic classifier example. Zero-shot appraoch 
7. semantic_search.py: semantic search example
8. taint_specification.py: script to generate taint specifications  
