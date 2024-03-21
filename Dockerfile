FROM python:3.11-alpine
WORKDIR /home/FSub
COPY . ./
RUN pip install -r requirements.txt
CMD ["python", "-m", "FSub"]