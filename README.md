---
title: OCRQuest
emoji: 🔥
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# OCRQuest

# OCR and Keyword Search Web Application

## Overview
This project is a web-based prototype that performs Optical Character Recognition (OCR) on an uploaded image containing text in Hindi and English. The application also implements a basic keyword search functionality based on the extracted text.

## Virtual Environment setup
Setup virtual environment using "python -m venv ocr-env"
and activated using "ocr-env\Scripts\activate"

## How can we run locally
Implement ocr and gradio(for user interface) in a python file(here I have app.py) save file and run it. We can run file using terminal by "python app.py" command. Gradio will launch the application and provide a local URL where we can test it in our browser.

## Deployment Process
- I have deployed this application on Hugging Face Spaces.
- To deploy on Hugging Face Spaces:
- 1.Create a repository on Hugging Face under the Spaces tab.
- 2.Add app.py file and requirements.txt file that lists all dependencies
- 3.Push the repository to Hugging Face, and it will automatically deploy the application.

## Features
- Upload an image in JPEG, PNG, or other common formats.
- Extract text from the uploaded image using EasyOCR.
- Search for a keyword in the extracted text.
- Display the extracted text and highlight keyword occurrences.

## Technologies Used
- Python
- EasyOCR
- Gradio
- Huggingface Transformers
- PyTorch
- PIL (Python Imaging Library)

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sprakhil/OCR_Project
