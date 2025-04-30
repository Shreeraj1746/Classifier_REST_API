# Named Entity Classifier REST API

A Flask-based REST API for identifying named entities in text using maximum entropy classification.

## Overview

This service provides a RESTful endpoint that classifies named entities in text. It uses a pre-trained maximum entropy classifier to identify entity types in the provided text.

## Features

- RESTful API endpoint for named entity classification
- Web interface for interactive testing
- Trained on wiki gold data
- Returns predictions for each token in the input text

## Project Structure

- `maxent_nec/`: Main application directory
  - `app.py`: Flask application entry point
  - `classify.py`: Classification logic
  - `features.py`: Feature extraction for NLP tasks
  - `classifiers/`: Directory containing trained model
    - `wiki_gold_me_classifier.p`: Pre-trained maximum entropy classifier
  - `templates/`: HTML templates for web interface
  - `static/`: Static assets (CSS, JavaScript, etc.)
- `load_test/`: Load testing scripts
  - `locustfile.py`: Locust configuration for load testing

## Requirements

- Python 3.x
- Flask
- NLTK
- Pickle
- Locust (for load testing)

## API Usage

### GET /classify

Classifies named entities in the provided text.

**Parameters:**
- `text`: The text to classify (required)

**Example Request:**
```
GET /classify?text=Jim Morrison was the lead singer of the band The Doors and lived in California.
```

**Example Response:**
```json
{
  "Jim": "PERSON",
  "Morrison": "PERSON",
  "was": "O",
  "the": "O",
  "lead": "O",
  "singer": "O",
  "of": "O",
  "the": "O",
  "band": "O",
  "The": "O",
  "Doors": "ORGANIZATION",
  "and": "O",
  "lived": "O",
  "in": "O",
  "California": "LOCATION",
  ".": "O"
}
```

## Setup and Running

1. Clone the repository
2. Install the dependencies
3. Run the Flask application:
   ```
   cd maxent_nec
   python app.py
   ```
4. Access the web interface at http://localhost:5000
5. Use the API at http://localhost:5000/classify?text=your text here

## Load Testing

To run load tests using Locust:

1. Install Locust: `pip install locust`
2. Navigate to the load_test directory
3. Run: `locust --host=http://localhost:5000`
4. Open the Locust web interface at http://localhost:8089
