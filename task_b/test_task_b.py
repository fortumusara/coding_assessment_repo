from fastapi.testclient import TestClient
from task_b.app import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

# Test valid input (testing the compute-timestamp-differences endpoint)
def test_process_valid_input():
    # Example valid input with timestamps
    sample_input = "2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"
    
    response = client.post("/compute-timestamp-differences", json={"input_text": sample_input})
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the result is a list
    assert len(response.json()) == 2  # There should be 2 results for the 2 timestamp differences

# Test invalid input (testing invalid timestamp format)
def test_process_invalid_input():
    # Example invalid input
    invalid_input = "invalid time range"
    
    response = client.post("/compute-timestamp-differences", json={"input_text": invalid_input})
    
    # Expect a 422 (Unprocessable Entity) or 400 (Bad Request) error depending on your validation
    assert response.status_code == 422 or response.status_code == 400
