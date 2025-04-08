# Coding Assessment Repository

This repository contains the complete solution for the multi-part coding assessment consisting of:

- **Task A**: Parsing plain text input and extracting call durations.
- **Task B**: Building a REST API service in Python/Rust to accept Task A input and return the processed result.
- **Task C**: Dockerizing the app to run multiple service instances, each with its own node ID.
- **Task 2**: Processing IPDR data from an Excel sheet to identify audio and video calls, generate statistics, and output call-level details.

---

## Repository Structure

##coding_assessment_repo/
##├── README.md  <-- Main project README
##├── task_a/
##│   ├── main.py
##│   ├── README.md
##├── task_b/
##│   ├── app.py
##│   ├── requirements.txt
##│   ├── README.md
##├── task_c/
##│   ├── app.py
##│   ├── Dockerfile
##│   ├── docker-compose.yml
##│   ├── README.md
##├── task_2/
##│   ├── data/
│   │   └── sample_ipdr.xlsx
│   ├── output/
│   │   └── (will store generated CSVs or visualizations)
│   ├── analyze_calls.py
│   ├── README.md
└── shared/
    └── utils.py (for any reusable functions)

---

## How to Run

Each task folder includes a `README.md` file with specific instructions. Start with `task_a`, then build on it as you move through `task_b` and `task_c`. Finally, see `task_2` for the IPDR call classification problem.

---

## Technologies Used

- **Python 3.11+**
- **FastAPI**
- **Docker**
- **Pandas / OpenPyXL**
- **Shell scripting / Git / REST APIs**

---

## Author

Fortune – [GitHub Profile](https://github.com/fortumusara)

---

## License

MIT License. See individual folders for more information.
