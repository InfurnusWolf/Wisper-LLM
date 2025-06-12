# TRIPPLANNER-CREWAI

**Transforming Travel Planning with Intelligent Precision**

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Built with the tools and technologies: **CrewAI, Python**

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

---

## Overview

**TripPlanner-CrewAI** is an AI-powered travel planning system that automates the creation of personalized and comprehensive trip itineraries. It orchestrates specialized AI agents to generate optimal routes, logistics, destination insights, and tailored trip-based outputs, delivering a seamless travel experience.

### Why TripPlanner-CrewAI?

This project aims to streamline and personalize travel planning through intelligent automation. The core features include:

- **Route & Logistics Optimization**:  
  Uses AI to craft efficient travel routes and manage logistics.

- **Multi-Agent Coordination**:  
  Integrates specialized AI models for detailed insights and recommendations.

- **Custom Itinerary Generation**:  
  Produces tailored travel plans based on user preferences.

- **Seamless Itinerary Saving**:  
  Stores detailed plans for easy access and future reference.

- **Enhanced User Experience**:  
  Delivers personalized trip and destination insights to elevate travel planning.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language**: Python
- **Package Manager**: Conda

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SrivibhavMalathkar/TripPlanner-CrewAI.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd TripPlanner-CrewAI
    ```

3. **Create and activate a conda environment:**

    ```bash
    conda create --name trip_env python=3.11
    conda activate trip_env
    ```

4. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Run the main script:**

    ```bash
    python trip_planner.py
    ```

2. **Provide inputs when prompted:**

   - Start Date
   - End Date
   - Budget (in INR ₹)
   
   The AI agents will process these inputs to generate a customized travel itinerary.

3. **Output:**

   - The final itinerary will be generated in JSON format for easy frontend consumption and can also be saved for future use.

---

## Testing

1. **Activate the environment:**

    ```bash
    conda activate trip_env
    ```

2. **Run tests (if applicable):**

    ```bash
    pytest
    ```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- Python community contributors
