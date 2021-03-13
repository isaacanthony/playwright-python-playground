FROM python:3.9
WORKDIR /src

# Install OS dependencies
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
  libwoff1 \
  libopus0 \
  libwebp6 \
  libwebpdemux2 \
  libenchant1c2a \
  libgudev-1.0-0 \
  libsecret-1-0 \
  libhyphen0 \
  libgdk-pixbuf2.0-0 \
  libegl1 \
  libnotify4 \
  libxslt1.1 \
  libevent-2.1-6 \
  libgles2 \
  libvpx5 \
  libnss3 \
  libxss1 \
  libasound2 \
  libdbus-glib-1-2

# Install playwright
RUN pip3 install playwright==1.9.2
RUN python3 -m playwright install

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
