---
title: "Bachelor Thesis Co-Relator - Francesco Mauro"
collection: teaching
type: "Bachelor Degree in Electronic Engineering for Automation and Telecommunications"
permalink: /teachingbachelor/bachelor-fmauro
venue: "University of Sannio, Engineering Department"
date: 2020-10-18
location: "Benevento, Italy"
---

# Analysis of the correlation between Sentinel-5P data and epidemiological data. Case study: spread of Covid-19 in the Lombardy region

## Abstract

The epidemic of what is commonly called "Coronavirus" broke out last December in China, in the province of Hubei. It is thought that the epicenter was the Wuhan market and that from there the virus spread to the rest of China, neighboring countries and around the world. Each pandemic represents a threat to health and a challenge for the countries that must contain it. The virus moves faster than people and in order to limit the damage it takes great efforts. While it is true that strong measures are needed, at the same time these measures must be taken at the right time. We have learned that in the event of a Covid pandemic, certain behaviors and needs such as meetings, mobility, sharing of workspaces, etc. they can heavily affect the number of infected people. In order to reduce the catastrophic effects related to the virus, last March all the countries took action with post-hoc interventions, based on the number of infected and dead, through several consecutive blocking attempts, each time more restrictive, but not always effective. .

In Italy, Covid-19 has not spread equally to all regions. By virtue of this, many scholars have wondered what were the factors that accelerated the spread of the virus. In this regard, the idea has emerged that some environmental pollutants could facilitate the spread of the disease.

Based on the considerations presented so far, in response to an ESA call, we submitted the idea of ​​creating a Decision Support System (DSS) equipped with Artificial Intelligence (AI) that received information from multiple sources and A PRIORI produced as output the degree of risk and the consequent interventions to be implemented by the Decision-Makers. In my thesis I dealt with only a small part of this so complex system: applying my knowledge on Remote Sensing I compared the variation of the average concentration of nitrogen dioxide with the trend of the diffusion of SARS-CoV-2.

The data used for the environmental risk assessment were those of Sentinel-5P, a satellite launched into space by the European Space Agency, as part of the Copernicus project. Sentinel-5P products were downloaded through the Google Earth Engine, whose programming interface (API) is available in JavaScript and Python (making it easy to leverage the power of Google's cloud for your geospatial analysis). In my case I used JavaScript, an object-oriented and event-oriented programming language. In particular, through this Google tool, I was able to acquire the data relating to $ NO_2 $, filtering them both by AOI (Area Of Interest) and by time intervals useful for the analysis.
 
As regards the part relating to the spread of Covid-19 in Italy, I concentrated on the processing of data on new daily infections.
 
The area of ​​interest, chosen for my case study, was the Lombardy region since in the latter the virus spread at a completely different speed compared to the rest of Italy.
 
The acquired data, their processing and use, have been elements of study of my thesis work.