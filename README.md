## How To Run Project

## step:1 Create and activate a virtual environment

cd your-fastapi-project
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate


## step:2 Install the project dependencies
pip install -r requirements.txt

## step:3 Run the FastAPI application using Uvicorn
uvicorn run_server:app --host 127.0.0.1 --port 8080 --reload

