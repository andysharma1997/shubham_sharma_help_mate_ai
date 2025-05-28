# Use the official slim Python 3.10 image
FROM python:3.10-slim

LABEL org.opencontainers.image.source="https://github.com/andysharma1997/shubham_sharma_travel_assistant"

COPY . /opt

WORKDIR /opt

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt


# Expose the port Streamlit runs on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
