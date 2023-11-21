# Image Analysis Tool

## Overview

This Image Analysis Tool is a Python-based application that combines Optical Character Recognition (OCR), image description using Azure Computer Vision, and sentiment analysis using TextBlob. It allows users to upload images, extract text, describe the content of the images, and analyze the sentiment of the extracted text.

## Features

- **OCR**: Extracts text from uploaded images using EasyOCR.
- **Image Description**: Describes images using Azure's Computer Vision API.
- **Sentiment Analysis**: Analyzes the sentiment of the extracted text using TextBlob.

## Project Structure

The project is organized into the following main components:

- `app.py`: The main application script with GUI using Tkinter.
- `ocr.py`: Module for OCR functionality.
- `image_description.py`: Module for image description using Azure Computer Vision.
- `sentiment_analysis.py`: Module for sentiment analysis using TextBlob.
- `testing/`: Contains unit tests for each module.

## Installation

Clone the repository:
```bash
git clone https://github.com/jwwils/Image-Describe
```
## Install required dependencies:

```bash

pip install -r requirements.txt
```
## Usage

Run the app.py script to start the application:

```bash

python app.py
```
## Testing

To run the unit tests, navigate to the testing directory and execute the test scripts:

```bash

python -m testing.test_ocr
python -m testing.test_image_describe
python -m testing.test_sentiment_analysis
```
## Configuration

  Ensure that config.json is set up with your Azure Computer Vision API key and endpoint.
  For OCR, the EasyOCR library is used, which may require additional dependencies for image processing.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

