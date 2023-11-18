# FastAPI Text Classification API

This is a simple FastAPI application that serves as an API for text classification using a pre-trained model from the Transformers library. In this example, we use a sentiment analysis model, but you can easily modify it to use other text classification models.

Getting Started
===

Prerequisites
---

Make sure you have Python and pip installed on your machine. You will also need to install the required dependencies listed in the `requirements.txt` file.

    pip install -r requirements.txt

Running the Application
---

Run the FastAPI application using the following command:

    uvicorn app:app --reload

API Endpoints
---

`POST /predict/`

This endpoint is used for making predictions on the sentiment of a given text. The input should be provided in the request body as a JSON object with the text field.

Example:

    curl -X POST "http://127.0.0.1:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"text": "This is a great example."}'

Response:

    {
        "sentiment": "POSITIVE",
        "confidence": 0.9998656511306763
    }

Additional Information
---

* FastAPI Documentation: https://fastapi.tiangolo.com/
* Transformers Documentation: https://huggingface.co/transformers/


Collaborators
---

1. Maksim Nadezhdin
