from python:3.1.12
WORKDIR /app 
COPY requirements.txt .
run pip3 install -r requirements.txt
COPY . .
CMD pytest test_merge.py