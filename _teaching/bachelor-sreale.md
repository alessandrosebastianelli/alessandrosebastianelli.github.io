---
title: "Bachelor Thesis Co-Relator - Simona Reale"
collection: teaching
type: "Bachelor Degree in Electronic Engineering for Automation and Telecommunications"
permalink: /teachingbachelor/bachelor-sreale
venue: "University of Sannio, Engineering Department"
date: 2021-10-18
location: "Benevento, Italy"
---

**Thesis title**: Performance analysis of a new splitting method for datasets in machine learning models. Case study: detection of volcanic eruptions

### Abstract
Remote sensing is a technique based on the collection of data, to obtain information from objects, without there being direct contact with the object in question.

In remote sensing by means of sensors, it is possible to acquire information that the human eye is normally unable to pick up (through radiation with different frequencies, even outside the visible band). In remote sensing there are three essential elements: a platform on which the instrument containing the sensor will be mounted, the object to be observed, the instrument containing the sensor by means of which the object of interest is observed.
I would like to specify in this regard that part of this thesis relating to the study of remote sensing was conducted with my colleague Luigi Russo.

In my thesis work I dealt with satellite remote sensing and I used data from the COPERNICUS program, which was born thanks to the European Space Agency (ESA) to guarantee Europe substantial independence in the detection and management of data for observation. of the Earth, in support of European public policies through the provision of precise and reliable services on environmental and safety aspects.
COPERNICUS is based on a series of six types of satellites, called Sentinels, designed by ESA, under the supervision of the European Commission, in order to satisfy all the operations required by the program.

In particular, for the purpose of monitoring volcanic eruptions, the data of Sentinel-2, one of the satellites of the Copernicus mission with bands also in the infrared, are suitable for example. To select the data of interest, I used the Google Earth Engine (GEE) cloud platform. This platform acts as a "repository" for storing satellite images, but also allows for processing in the cloud.

In the specific case, I used JavaScript, an object-oriented programming language, and I used Sentinel-2 images filtered by date and by type of volcano considered, choosing the infrared bands. The presence of a high temperature when the eruption is in progress, allows to highlight the lava flow through the use of the thermal bands. Through GEE I selected three images for each volcano, ie pre, during and post-eruption, and then I chose the most significant ones to distinguish the various periods.

A second part of my thesis work involved the use of Machine Learning (ML) techniques. ML is a discipline of artificial intelligence, which is based on the ability of some networks (called neural networks) to learn and make decisions. Deep Learning (DL) is a subset of ML techniques and represents the latest generation. These models are also based on neural networks, and the term deep refers to the fact that a large number of layers are included in the network.

Artificial intelligence and the various techniques related to it have been increasingly used in recent years, including in the field of satellite remote sensing and data and image processing. These techniques can be applied to remote sensing data for many cases of interest, from weather forecasts to natural disaster monitoring, and many others.

In ML, one of the main requirements is to build computational models with high prediction and generalization capabilities. In the case of supervised learning, a computational model is trained to predict the outputs of an unknown target function.
A common technique is cross-validation. The basic problem of this technique is to decide on an appropriate subdivision of the data which can be handled as a statistical sampling problem. Therefore, various classical statistical sampling techniques can be employed to divide the data (splitting).

In this second part of the thesis I examined a new splitting technique based on a histogram dissimilarity index. The proposed method is iterative and consists in dividing the input dataset into two parts through the use of a dissimilarity index, calculated on the cumulative histograms of these two parts. The method is applied to the input dataset to get the initial train-validation split. Then the same procedure is applied to the training dataset to obtain, together with the first division, the final train-validation-test division.

A specific data set was therefore built using a Tool capable of selecting volcanic events from an online catalog, also including geolocation information. The satellite images acquired for the place and date of interest were collected and tagged using the Python open-access tool, and some pre-processing procedures were applied to the downloaded data.
The detection task (volcanic eruption detection) was addressed by implementing a binary classifier where the first class is assigned to images with eruptions and the second is addressed to all other scenarios. The network used was a Convolutional Neural Network (CNN) divided into two subnets: the first is a convolutional network responsible for extracting the characteristics and the second fully connected network is responsible for the classification.

The experiments conducted and the results shown made it possible to positively evaluate the proposed method for splitting, which represents an innovation compared to the state of the art.
