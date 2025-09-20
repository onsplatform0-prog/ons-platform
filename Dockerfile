FROM python:3-alpine AS builder
 
WORKDIR /app
 
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY . .
RUN pip install -r requirements.txt

 
EXPOSE 7860
 
CMD ["python3", "app.py"]
# CMD ["gunicorn", "--bind" , ":8080", "--workers", "2", "app:app"]