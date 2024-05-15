---
title: "Bachelor Thesis Co-Relator - Pietro Di Stasio"
collection: teachingbachelor
type: "Bachelor Degree in Electronic Engineering for Automation and Telecommunications"
permalink: /teachingbachelor/bachelor-pdistasion
venue: "University of Sannio, Engineering Department"
date: 2022-10-18
location: "Benevento, Italy"
---

# Use of Sentinel-5P data for the early detection of volcanic eruptions through on-board Artificial Intelligence

## Abstract
Over the last few years, Artificial Intelligence (AI) has made it possible to achieve increasingly important goals, especially thanks to technological development. Moreover, from the point of view of research it is one of the most active sectors, which thanks to the enormous amount of applications available, allows you to manage problems that until recently seemed impossible.

Among the pioneers of the use of AI algorithms applied to cases of interest we must necessarily mention the European Space Agency (ESA). The enormous availability of data collected through satellite missions and the intuition to focus on research and cutting-edge topics have led ESA to always be in the most important and strategic positions, playing impactful roles in many areas of interest.

In recent years, the possibility of the so-called Artificial Intelligence on board has received particular attention, i.e. the ability to transfer specific algorithms on board satellites in orbit in order to optimize the procedures for acquiring and processing satellite data.

Applications of this type are currently implemented for example through the use of visual processing units such as the Movidius Myriad-2 which allows the implementation of AI models on board the satellite while maintaining the right compromise between complexity and energy consumption.

As part of the above, this thesis wanted to highlight the use of Artificial Intelligence for the early detection of volcanic eruptions through the use of Sentinel-5P data. In particular, the purpose of the study was the introduction of AI on board the satellites, with the aim of guaranteeing the monitoring of events such as volcanic eruptions. The use of AI-based algorithms and early detection can be exploited to carry out the necessary detections and inform, for example, law enforcement agencies and guarantee immediate action for the protection of things and people.

The work started from the analysis of the concentration of tropospheric $ SO_2 $ acquired by Sentinel-5P, since this is the major gas emitted by volcanoes in the eruption phase. The study of the gases emitted, in fact, allows to detect really important information regarding the state of activity of a volcano. To carry out an analysis of this type it was necessary to proceed with the creation of a dataset that included cases of eruptions and not eruptions, for the training of the neural network used for the purpose. In the final part of the thesis work, a Machine Learning model is presented that can demonstrate the feasibility of the proposed project. And this model will be the starting point for future developments. \\

This thesis work is divided into the following chapters:

- Chapter 1: the basic principles of remote sensing, the main characteristics and the remote sensing platforms are described.
- Chapter 2: the Sentinel-5P satellite is explored and the TROPOMI instrument that characterizes it is described.
- Chapter 3: an introduction to Machine Learning and some of the most used algorithms is given.
- Chapter 4: this chapter concerns the case study and therefore the processing of the data obtained by the Sentinel-5P satellite for early detection in the case of volcanic eruptions through the application of CatBoost, an appropriate Machine algorithm Learning.

In relation to the thesis work carried out, it should be noted that the initial idea was to use convolutional neural networks (CNN) which, trained on the generated dataset, could then be used to support early detection through an appropriate classification of the images downloaded from the platform. Sentinel-5P satellite.

During the creation of the dataset, however, problems emerged mainly due to a strong lack of information in the downloaded images attributable to acquisition problems of the satellite itself or to the type of data analyzed.

Through an in-depth analysis of the available data, it was decided to proceed with the use of statistical parameters such as mean and standard deviation.

This approach allowed us to apply a specific Machine Learning algorithm, the CatBoost, which in this case proved to be fundamental for the classification operation.

Starting from the generated dataset, quite promising results were obtained, reaching levels of accuracy in the
data classification equal to 80%.

The results obtained therefore demonstrated the potential of the method introduced and the possibility of extending the model to other case studies of interest, besides that of volcanic eruptions.A future goal is to exploit the trained model for the application of AI on board in real cases, as happened for the PhiSat-1 mission which contributed to the debut of Intelligence Artificial in space. Suitably equipped, the satellite can perform real-time processing and inform the authorities within a few minutes in order to ensure immediate action by the party of the police in the event of volcanic eruptions or for any natural disaster that may be dangerous for the planet.