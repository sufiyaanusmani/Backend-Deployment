# Backend
---

## To run locally (without Docker container)

1. Clone the repository: `git clone git@github.com:c137519edbb3/Backend.git .`
2. Navigate to the root folder of the project
3. Create virtual environmemnt: `python -m venv .venv`
4. Switch to virtual environment: `source .venv/scripts/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn api.main:app --reload`

## To run locally (with Docker container)

1. Clone the repository: `git clone git@github.com:c137519edbb3/Backend.git .`
2. Navigate to the root folder of the project
3. Run the container: `docker compose up --build`