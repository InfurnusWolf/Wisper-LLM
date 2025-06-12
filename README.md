# WISPER-LLM

**AI-Powered Audio Transcription and Text Processing with Whisper and LLM**

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Built with cutting-edge technologies: **OpenAI Whisper, Google Gemini, Python**

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

**Wisper-LLM** is an intelligent audio transcription and language processing tool that leverages **OpenAI's Whisper model** for speech recognition and **Google Gemini LLM** for advanced text processing and analysis. This tool automates the conversion of spoken audio into structured, machine-readable formats such as Excel files.

### Why Wisper-LLM?

- **Automatic Speech Recognition (ASR)**:  
  Uses OpenAI Whisper to accurately transcribe audio data to text.

- **Language Model Integration**:  
  Utilizes Google Gemini LLM to summarize, classify, and structure transcribed text.

- **Excel Output Generation**:  
  Processes transcribed and analyzed content into a readable and exportable Excel (.xlsx) file.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- **Python 3.11 or higher**
- **pip** (Python package manager)
- **OpenAI Whisper**
- **Google Generative AI SDK (`google-generativeai`)**
- **dotenv** for managing environment variables

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/InfurnusWolf/Wisper-LLM.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Wisper-LLM
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv wisper_env
    source wisper_env/bin/activate  # On Windows: wisper_env\Scripts\activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables:**

    Create a `.env` file and add your API keys:

    ```bash
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

---

## Usage

1. **Run the main script:**

    ```bash
    python main.py
    ```

2. **Provide required audio input files as specified.**

3. **The system will output transcription results and structured Excel files in the `/output` directory.**

---

## Features

- ✅ **Audio Transcription** using OpenAI Whisper
- ✅ **LLM-powered Text Processing** via Google Gemini
- ✅ **Excel File Generation** with structured output
- ✅ **Environment variable management** using `.env`
- ✅ **Easy customization** for different transcription and processing tasks

---

## Testing

To run tests (if applicable):

```bash
pytest
