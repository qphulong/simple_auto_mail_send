# dev mode
uvicorn main:app --reload

# production mode
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info >> ./app.log 2>&1 &