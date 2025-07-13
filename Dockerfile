# Use official slim Python image with 3.10
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files to container
COPY . /app

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Streamlit uses
EXPOSE 7860

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
