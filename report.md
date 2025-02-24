---
author: Anyan Huang, 
title: "Title of the template blog"
image: "../img/p1_measuring_software/gX_template/cover.png"
date: 03/03/2022
summary: |-
  abstract Lorem ipsum dolor sit amet, consectetur adipisicing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
  reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
  pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
  culpa qui officia deserunt mollit anim id est laborum.
---

+ **Add your name here**
+ **Change the summary**
+ **Contrive a new title of the blog**
+ **Find a good cover(generate one using diffusion by giving the summary?)**

# Group 4 - The impact of OS on energy consumption

## Table of Contents

*   [Introduction](#introduction)
*   [Problem](#problem)
*   [Method](#method)
*   [Results](#results)
*   [Conclusion](#conclusion)
*   [References](#references)

# Introduction

In today's digital age, web browsers are essential tools for accessing information, connecting with others, and consuming content. However, as we become increasingly aware of our environmental footprint, it is crucial to examine not only the performance of these browsers but also their energy consumption. This project aims to explore and compare the energy consumption of two popular web browsers: Google Chrome and Mozilla Firefox.

The primary motivation behind this experiment is to understand the energy-saving impact of users switching between Firefox and Chrome. For instance, if our results indicate that Chrome is more energy-efficient than Firefox on Linux, we can estimate the total energy savings if all Linux Firefox users switch to Chrome. This shift could lead to significant reductions in energy consumption, contributing to a more sustainable digital environment.

**(Research qestions need to be added here)**

This article is divided into two main parts: 1) how to set up energy measurements with minimum bias, and 2) how to analyse and take scientific conclusions from your energy measurements.
Read on so that we can get your paper accepted in the best scientific conference.

-------------------------------------------------------------------------------------------------------------------------------------------------------

# Assessing Real-World Impact

To make our findings more relevant, we will investigate user statistics to understand the number of Firefox users across different operating systems. By calculating potential energy savings based on the average energy consumption difference between the two browsers, we can provide actionable insights for users and organizations alike.

In our testing, we will focus on several software applications that are commonly used by individuals and organizations. The primary tools under test will include:

+ **Google Chrome**: A widely used web browser known for its speed and extensive feature set.

+ **Mozilla Firefox** : An open-source browser that emphasizes privacy and customization.

We will utilize the **Energibridge** tool for measuring energy consumption during our tests. This tool allows us to capture detailed energy usage data while running various browser tasks. By employing this software, we can ensure that our measurements are accurate and reflective of real-world usage scenarios.

# User-Centric Test Scenarios

To ensure our tests reflect everyday browser usage, we will design user-centric test scenarios that mimic common activities. This approach will help us gather data that is not only technical but also relatable to the average user.



## Proposed Testing Tasks
All tests follow the same pipeline with the aim to collect reliable energy data. One iteration conists of 60s of running a process with a 60 cooldown period directly after terminating the process, with the aim of preventing tail energy consumption from affecting the next process.

+ Warm Up: 5 iterations of sleep/wait (depending on OS).
+ Main Test:

  + 30 Iterations per browser. (60 iterations total)
  + Browsers are randomly shuffled to try to mitigate unwanted biases.


### Baseline Test
A baseline test is conducted on each machine used for subsequent testing, serving as a calibration step. This test consists of 30 iterations of sleep/wait instead of executing a browser test. By analyzing these results, we can better normalize the outputs of the following tests, allowing us to focus primarily on the power consumption of browsers.

For a details regarding this implementation refer to: [Baseline Script](https://github.com/D4vidHuang/SSE_EnergyMeasurement/blob/linux_test/linux_scripts/auto_sleep_script.sh)


### Reddit Test
The Reddit test replicates a user scrolling (DOOMSCROLLINGGGG) on each browser. Bellow the function implemented in Python utilizing the Selenium library.

```python
    def browse_reddit(duration_seconds=60):
    driver = webdriver.Firefox()  # geckodriver is assumed to be in PATH

    try:
        driver.get("https://www.reddit.com")

        time.sleep(5)  # Initial wait

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait briefly between scrolls

    finally:
        driver.quit()
```
### Youtube Test

1. Streaming Videos (YouTube): Measure energy consumption while streaming videos on YouTube, a common activity for many users.
2. Browsing Social Media (Facebook): Assess energy usage while browsing social media platforms like Reddit, where users often spend significant time.

# Testing Setup

+ Versions of Softwares under Test

  | Softwares/Tools | Version       |
  | --------------- | ------------- |
  | Google Chrome   | 133.0.6943.99 |
  | Mozilla Firefox | 135.0         |
  | Energibridge    | v0.0.7        |

## Testing environment:

### Linux
Machine: ASUS Zenbook 14 UX3405MA

  + Processor: Intel® Core™ Ultra 9 185H × 22
  + Memory: 32.0 GiB

Operating System: Fedora Linux 41 (Workstation Edition)

  + Kernel Version: Linux 6.12.15-200.fc41.x86_64
  + Windowing System: Wayland

### MacOS
MacOS 15.3.1


  **Note:** _TODO: Specify System completely_


### Windows
 Windows

  **Note:** _TODO: Specify System completely_

## Environment Setup



+ Zen mode: 

  The first thing we need to make sure of is that the only thing running in our system is the software we want to measure. Unfortunately, this is impossible in practice – our system will always have other tasks and things that it will run at the same time. Still, we must at least minimise all these competing tasks:

  - all applications should be closed, notifications should be turned off;
  - only the required hardware should be connected (avoid USB drives, external disks, external displays, etc.);
  - turn off notifications;
  - remove any unnecessary services running in the background (e.g., web server, file sharing, etc.);
  - if you do not need an internet or intranet connection, switch off your network;
  - prefer cable over wireless – the energy consumption from a cable connection is more stable than from a wireless connection.

+ Freeze your settings: 

  It is not possible to shut off the unnecessary things that run in our system. Still, we need to at least make sure that they will behave the same across all sets of experiments. Thus, we must fix and report some configuration settings. One good example is the brightness and resolution of your screen – report the exact value and make sure it stays the same throughout the experiment. Another common mistake is to keep the automatic brightness adjustment on – this is, for example, an awful source of errors when measuring energy efficiency in mobile apps.

+ 

# Testing Results

## Chrome

### MacOS
### Windows
### Linux



## FireFox

+ macos
+ Windows
+ Linux



# Conclusion

By focusing on user-centric scenarios and emphasizing the real-world impact of our findings, this project aims to provide valuable insights into the energy consumption of web browsers. Through our testing, we hope to encourage users to make informed decisions that contribute to a more sustainable digital environment.

