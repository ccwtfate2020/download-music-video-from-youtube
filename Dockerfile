FROM python:3.10.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install python3-pip ffmpeg -y --no-install-recommends

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    # Note: we had to merge the two "pip install" package lists here, otherwise
    # the last "pip install" command in the OP may break dependency resolution…

#CMD ["python"]

