# Flask App

This is a basic Flask application with a modular structure.

## Features
- Home and About pages
- Basic HTML templating
- CSS styling
- Unit tests for routes

## Setup

1. Clone the repository:
```
git clone <repo-url>
cd flask-app
```
2.Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3.Run the application:

```
python run.py

```
4.Open in your browser:
```
http://127.0.0.1:5000

```


## Steps to Run the Application in Docker
1. Build the Docker Image
```
docker build -t flask-app .
```
2. Run the Docker Container

```
docker run -p 5000:5000 flask-app
```
### Using docker-compose (Recommended) Build and run the container 
```
docker-compose up --build
```
Access the App Open your browser and go to http://127.0.0.1:5000/.

Stop the Container Use Ctrl+C in the terminal or stop the service with:
```
docker-compose down
```
