FROM python:3
WORKDIR /AlgoTrade
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./launcher.py" ]