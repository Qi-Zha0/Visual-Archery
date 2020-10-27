# Visual Archery ([link to repo](https://github.com/Qi-Zha0/Visual-Archery/))
![GitHub](https://img.shields.io/github/license/Qi-Zha0/Visual-Archery)
[![Build Status](https://travis-ci.com/Qi-Zha0/Visual-Archery.svg?branch=master)](https://travis-ci.com/Qi-Zha0/Visual-Archery)

### Introduction
A tool that automatically scores archery targets based on images. The archer can simply snap a photo of the target face after each end and have the scores and positions of arrows recorded without having to manually enter the numbers or mark the arrows. It aims to make score keeping for at archery ranges more efficient and to provide more insight beyond just numbers with less effort from the archer.

### Motivation
As an amateur archer, I practice shooting my recurve bow at a rental indoor archery range and aspire to be goot at target shooting one day. Naturally, I would like to track my training progress. There exists a handful of target scoring apps that allow archers to either manually enter their scores after each end, or mark the position of their shots on a target face image. But here's the problem: for safety purposes, archers training at the same range have to act synchronizely. All archers step up to the shooting line at the same time, wait for the last person to finish shooting, retrieve the arrows, and wait behind the waiting line until no one is in the range. I would like to take time to record my scores for each round but do not want to waste everyone else's paid time. More importantly, I perfer spending the few minutes in between rounds focusing on improving my form rather than doing data entry. Usually at the begining of the rental session, the customer gets a piece of target paper and can keep it for record, but looking at the target face with hundreds of overlapping arrow holes does not help much. 

### Objective
This project aims to create a tool for swift and accurate archery scoring for archers training individually. After each end, the archers can use their phone to take a picture of the target and this application should automatically extract the scores from the previous end. It processes photos of target face and extract relevant information including scores, positions of shots, and arrow groupings. Compared to traditional score keeping apps that only track numerical scores, it should record and extract more useful information from the images, such as the position of arrows, which are more important to archers who wants to improve their skills. The goal is to save time while affording the same benefits provided by the target plotting apps that require users to manually mark the positions of the arrows.

### Basic features
The app should allow users to enter the following informaton about their training session:
* Date, time of training session
* Number of arrows per end
* Target type
* Equipment specification
* Range information (indoors/outdoor, range length)
* Sight & stabilizer configuration

...and provide the following information
* Scores for each end and/or training session
* Visualization and statistics of training history
* Training suggestions based on performance, e.g. good/bad grouping, whether need to adjust the sight, anchor position, form analysis 

### Advanced features
* Multi-player tournament mode
* Standard rounds (World Archery, NFAA, Archery GB, etc)