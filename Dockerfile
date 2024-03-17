# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python web server script to the container
COPY web_server.py .

# Install the required dependencies - seems not needed as already included with python3
#RUN pip install http.server

# Expose the port on which the web server listens
EXPOSE 8000

# Run the Python web server script when the container starts
CMD ["python3", "web_server.py"]