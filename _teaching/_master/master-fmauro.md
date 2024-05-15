---
title: "Master Thesis Co-Relator - Francesco Mauro"
collection: teaching
type: "Master Degree in Electronic Engineering for Automation and Telecommunications"
permalink: /teachingmaster/master-fmauro
venue: "University of Sannio, Engineering Department"
date: 2022-10-18
location: "Benevento, Italy"
---

# Climate Change Impact Evaluation on levels of water resources through deep learning techniques

## Abstract
This thesis work aims to investigate the impact of climate change on the water basins, pursuing the goal of helping Decision Makers understand the extent and possible direction of adopting the right measures.

In order to build a system, based on Machine Learning, to support the fight against climate change, the first step is to have a good dataset on which to run statistical analysis and to adopt the chosen methodology. In particular, to recognize temporal changes in water basins, it is necessary to have a dataset with multitemporal acquisitions. Therefore, the first part of my thesis work has focused on creating the suitable dataset. 

Sentinel-2A and Sentinel-2B multispectral data related to the places under analysis have been downloaded from Google Earth Engine (GEE) and then processed in Python. The data were collected over a period of two years (July 2020 - August 2022), taking samples every two months. These data were used to calculate the NDWI (Normalized Difference Water Index) to obtain water maps of the areas of interest. 

It is worth to highlight that the dataset allows users to measure how the territory has changed over time, in particular to monitor the lowering of water levels and the consequent emergence of the seabed.  A first  dataset has been created  including  Italian basins (lakes and rivers) with the idea to  extend the dataset to Europe and other parts of the world. Moreover this dataset will be made available on my GitHub page for interested researchers.

As a second step, the objective has been to apply machine learning (ML) models to predict the water level changes. The ML model used to run this analysis is a type of Recurrent Neural Network (RNNs), called LSTM (Long Short-Term Memory). With respect to classical RNNs, LSTMs are able to identify long and short temporal patterns in the input data. More specifically,  the proposed method takes advantage of both Convolutional Neural Networks (CNNs) and LSTM. This combination has allowed the final model to learn and discriminate both spatial and temporal patterns, in order to accurately predict changes in the water levels. All this was also useful to identify potential  desertification areas and take note of them.

This thesis work wants to represent a starting point for the future activities to be carried out during future research activities. The idea is to use the dataset for different ML models, in particular hybrid networks including Quantum layers. The application of Quantum Machine Learning (QML) in RS is representing a cutting-edge topic that is gaining great attention for the Earth Observation (EO)  nowadays.
