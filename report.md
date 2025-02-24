---
author: Anyan Huang, Yongcheng Huang, Yiming Chen, Philippe Henry,
title: "The browser energy efficiency revolution"
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

# Group 4 - The browser energy efficiency revolution: An empirical study of energy consumption from the perspective of user behavior


## Table of Contents

*   [Introduction](#introduction)
*   [Problem](#problem)
*   [Method](#method)
*   [Results](#results)
*   [Conclusion](#conclusion)
*   [References](#references)

# Introduction


When 3.7 billion browser users scroll through social media feeds, hidden energy consumption differences quietly alter the digital world's carbon footprint. This study, through an automated testing framework, achieves the following for the first time:

1. **Modeling Real User Behavior** (YouTube watching, Reddit browsing)
2. **Cross-Browser Energy Benchmarking** (Firefox 121 vs. Chrome 122)
3. **System-Level Energy Isolation Measurement Techniques** (MacOS15.3.1, Fedora, Windows11)
4. **Statistical Significance Validation**

## Research Questions

- Is there a statistically significant difference in energy efficiency between different browsers in typical user scenarios? 
- How do user behavior patterns amplify the energy impact of browser choice?
- Does the energy-saving benefit of browser/operating system migration strategies have scalable application value?

## Key Findings:

**TODO: Change this to the actual data**

Our experiments reveal that, in typical usage scenarios, **Chrome consumes xxxx less energy on average compared to Firefox**, leading to an annual CO₂ reduction of **xxxx per user**. 

If **xxxx of global Firefox users switched to Chrome**, the estimated annual energy savings would reach **xxxx million kWh**—enough to power **xxx households for an entire year**.



-------------------------------------------------------------------------------------------------------------------------------------------------------

# Assessing Real-World Impact

To make our findings more relevant, we will investigate user statistics to understand the number of Firefox users across different operating systems. By calculating potential energy savings based on the average energy consumption difference between the two browsers, we can provide actionable insights for users and organizations alike.

In our testing, we will focus on several software applications that are commonly used by individuals and organizations. The primary tools under test will include:

+ **Google Chrome**: A widely used web browser known for its speed and extensive feature set.

+ **Mozilla Firefox** : An open-source browser that emphasizes privacy and customization.

We will utilize the **Energibridge** tool for measuring energy consumption during our tests. This tool allows us to capture detailed energy usage data while running various browser tasks. By employing this software, we can ensure that our measurements are accurate and reflective of real-world usage scenarios.

# User-Centric Test Scenarios

To ensure our tests accurately represent real-world browser usage, we design **user-centric scenarios** that capture typical activities. This approach provides practical insights into energy consumption beyond purely technical measurements.

## Test Protocol

- **Baseline Task:** 60-second idle period (both Chrome and Firefox).  
- **Iterations:** 30 runs, **2 minutes per iteration** (60 seconds active, 60 seconds idle).  
- **Test Cases:**
  1. **Video Streaming (YouTube):** Measure energy usage during continuous video playback.  
  2. **Social Media Browsing (Reddit/Facebook):** Assess energy consumption while scrolling and interacting with content.  

## Testing Configuration

### Software Versions

| Component        | Version       |
|-----------------|--------------|
| Google Chrome   | 133.0.6943.99 |
| Mozilla Firefox | 135.0         |
| Energibridge    | v0.0.7        |

### Test Environment

- **Operating Systems:** macOS 15.3.1, Windows, Linux  
- **Hardware Constraints:** Standardized across all runs  

### Experimental Controls

#### **Zen Mode (Minimized System Interference)**  
To ensure consistency, we reduce system background activity as follows:  

- Close all non-essential applications.  
- Disable notifications.  
- Disconnect unnecessary peripherals (USB drives, external displays, etc.).  
- Stop background services (e.g., web servers, file-sharing tools).  
- Disable network connectivity if not required.  
- Prefer wired connections over wireless for stability.  

#### **Configuration Freezing (Eliminating Variability)**  
To maintain test consistency, we **fix and document** key settings:  

- **Display Configuration:** Lock brightness and resolution to a fixed value.  
- **Power Management:** Disable automatic brightness adjustment and dynamic power-saving features.  
- **Network Conditions:** Ensure stable network settings to prevent fluctuations in energy usage.  

By enforcing strict experimental controls, we **minimize variability** and ensure the reproducibility of our results.

# Testing Results

## Chrome

+ macos
+ windows
+ Linux

## FireFox

+ macos
+ Windows
+ Linux



# Conclusion

By focusing on user-centric scenarios and emphasizing the real-world impact of our findings, this project aims to provide valuable insights into the energy consumption of web browsers. Through our testing, we hope to encourage users to make informed decisions that contribute to a more sustainable digital environment.

