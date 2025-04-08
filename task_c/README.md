# Task C - Dockerize the Application and Run Multiple Instances

## Description

In this task, the app from Task B is containerized using Docker. 
Multiple instances of the app will run in separate containers. 
Each instance will return the result along with a node ID to indicate which container is providing the response.

## Objective

- Containerize the REST API app.
- Run at least two instances of the container.
- Each instance should return the node ID along with the results.

Example Output 

``json
{
  "id": "node-1",
  "result": [ "25200", "88200" ]
}


How to run 


### Step 1: Install Docker

Ensure Docker is installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

### Step 2: Build the Docker Image

In the root folder of Task C (`task_c`), build the Docker image:

# Step 4: Test the Containers

You can test the containers using curl. For example:

curl -X POST "http://127.0.0.1:8001/process" -H "Content-Type: text/plain" --data-binary @sample_input.txt
curl -X POST "http://127.0.0.1:8002/process" -H "Content-Type: text/plain" --data-binary @sample_input.txt

## Step 5: Stop the Containers

To stop the containers:

docker stop node-1 node-2

## Step 6: Clean Up

To remove the containers:

docker rm node-1 node-2

# Endpoints

    POST /process
    Accepts plain text input, processes it, and returns a JSON response with the result and the node ID.

# Requirements

    Docker

    Python 3.x

    FastAPI

    Uvicorn

# Files

    Dockerfile: Instructions for creating the Docker image.

    app.py: FastAPI app with endpoints.

    requirements.txt: Python dependencies.

    sample_input.txt: Example input for testing.


# To add this to your `README.md`:

1. Open your `task_c/README.md` file using `nano`:
   ```bash
   nano task_c/README.md

    Paste the formatted content above into the file.

    Save and exit by pressing Ctrl + X, then Y to confirm, and Enter to save the changes.
















docker rm node-1 node-2

# Endpoints

    POST /process
    Accepts plain text input, processes it, and returns a JSON response with the result and the node ID.

# Requirements

    Docker

    Python 3.x

    FastAPI

    Uvicorn

# Files

    Dockerfile: Instructions for creating the Docker image.

    app.py: FastAPI app with endpoints.

    requirements.txt: Python dependencies.





## Example Output

```json
{
  "id": "node-1",
  "result": [ "25200", "88200" ]
}



# Endpoints

    POST /process
    Accepts plain text input, processes it, and returns a JSON response with the result and the node ID.

# Requirements

    Docker

    Python 3.x

    FastAPI

    Uvicorn

# Files

    Dockerfile: Instructions for creating the Docker image.

    app.py: FastAPI app with endpoints.

    requirements.txt: Python dependencies.

    sample_input.txt: Example input for testing.


# To add this to your `README.md`:

1. Open your `task_c/README.md` file using `nano`:
   ```bash
   nano task_c/README.md

    Paste the formatted content above into the file.

    Save and exit by pressing Ctrl + X, then Y to confirm, and Enter to save the changes.
