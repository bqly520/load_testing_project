# Alpine is smallest distribution of Linux, even without Bash
# python<name of the base image>: <tag of the image>
from python:rc-alpine3.10
# ENV and RUN is needed to set to the correct time zone
# An alpine based image you have to install the tzdata first
RUN apk add --no-cache tzdata
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install CherryPy
COPY /deployments/app/web_service_app.py .
EXPOSE 7777
ENTRYPOINT ["python", "web_service_app.py"]