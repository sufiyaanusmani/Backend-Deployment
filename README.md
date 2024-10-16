# Backend
---

## To run locally (without Docker container)

1. Clone the repository
2. Navigate to the root folder of the project
3. Create virtual environmemnt: `python -m venv .venv`
4. Switch to virtual environment: `source .venv/scripts/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn api.main:app --reload`