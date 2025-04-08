# Task B - REST API for Duration Processing

## Description

This task wraps the logic from Task A in a Python-based REST API
using FastAPI. It accepts plain text input (same format as Task A),
calculates durations, and returns them as a sorted JSON array.

## Example

### Input (Plain Text)

07:00:00 14:30:00 08:00:00 17:30:00


### Output (JSON)

```json
[ "27000", "34200" ]

How to Run
Step 1: Install dependencies

cd task_b
pip install -r requirements.txt

Step 2: Run the API server

uvicorn app:app --reload

Step 3: Test the API

Send a POST request to /process:

curl -X POST "http://127.0.0.1:8000/process" \
  -H "Content-Type: text/plain" \
  --data-binary @sample_input.txt

Endpoints

    POST /process
    Takes plain text input, returns JSON response.

Requirements

    Python 3.x

    FastAPI

    Uvicorn

Files

    app.py - FastAPI app with endpoint

    sample_input.txt - Example input file

    requirements.txt - Python dependencies
