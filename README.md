# Signals Matter: Understanding Popularity and Impact of Users on Stack Overflow
---

This is the Python implementation of the experiments described in the [Signals Matter](http://precog.iiitd.edu.in/pubs/SignalsMatter-TheWebConf19.pdf) paper.

```
@inproceedings{merchant2019signals,
  title={Signals Matter: Understanding Popularity and Impact of Users on Stack Overflow},
  author={Merchant, Arpit and Shah, Daksh and Bhatia, Gurpreet Singh and Ghosh, Anurag and Kumaraguru, Ponnurangam},
  booktitle={The World Wide Web Conference},
  pages={3086--3092},
  year={2019},
  organization={ACM}
}
```

## Authors:
  * Arpit Merchant
  * Daksh Shah
  * Gurpreet Singh Bhatia
  * Anurag Ghosh
  * Ponnurangam Kumaraguru

## Overview:

This repository contains information on obtaining the data and a reference implementation of the experiments described in the paper [Signals Matter: Understanding Popularity and Impact of Users on Stack Overflow]() accepted at WebConf (formerly WWW) 2019.

Situating our work in Digital Signaling Theory, we investigate the role of these game elements in characterizing social qualities (specifically, popularity and impact) of its users. We present evidence that certain non-trivial badges, reputation scores and age of the user on the site positively correlate with popularity and impact. Further, we find that the presence of costly to earn and hard to observe signals qualitatively differentiates highly impactful users from highly popular users.

## Dependencies
Our implementation works with Python>=3.5.2. Install other dependencies: `$ pip install -r requirements.txt`

To install xgboost:
```
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost && mkdir build && cd build
cmake .. -DPLUGIN_UPDATER_GPU=ON && make -j4
cd ../python-package && python3 setup.py install
```

## Data
There are three different ways to access the Stack Overflow data we use in our experiments.
1. [Stack Exchange data dump at archive.org](https://archive.org/details/stackexchange) - Anonymized dump of all user-contributed content for all Stack Exchange sites.
2. [Stack Exchange Data Explorer](https://data.stackexchange.com/) - Official online database of all Stack Exchange sites.
3. [Google BigQuery public datasets](https://cloud.google.com/bigquery/public-data/) - Public access to the Stack Overflow dataset with 1 TB per month worth of queries for free (terms and conditions applied).

This repository contains SQL queries that can be run on Google Big Query to download the data needed for the experiments. The query load falls within the free monthly user limit.

The fully processed data can also be downloaded from [Precog Lab's website](http://precog.iiitd.edu.in/requester.php?dataset=signalsMatter19).

## Usage
If you download the data using Google BigQuery, use the methods in `code/preprocessing.py` to preprocess it. If you downloaded the processed data from Precog's website, place `augmented_combined_df.csv` and `augmented_small_df.csv` into the `data` folder.

To run the regression model:
```
python regression_model.py [predict_feature] [model_name] [num_runs] [num_threads]
```
`predict_feature` - Choose between "popularity" or "impact".
`model_name` - Choose between "base", "reputation" and "badges".
`num_runs` - Number of runs of the experiment.
`num_threads` - Number of threads for parallelization

## Cite
Please consider citing our paper if you use our code.

## Acknowledgment
We thank Kushagra Bhargava, Shubham Singh, and Shwetanshu Singh for their help in using and maintaining system infrastructures.
