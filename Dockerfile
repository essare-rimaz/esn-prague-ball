FROM python:3.9
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY main.py style.css /app/
EXPOSE 8080
CMD ["streamlit", "run", "/app/main.py", "--server.port", "8080"]
