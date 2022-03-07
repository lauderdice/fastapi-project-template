# Template for a FastAPI-based project 
https://fastapi.tiangolo.com

start command
    
    gunicorn app.main:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --bind 0.0.0.0:8888
 


# Docker build

in top level directory

    docker build . -t application