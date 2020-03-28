# Alpine is smallest distribution of Linux, there is NO Bash
# python<name of the base image>: <tag of the image>
from python:rc-alpine3.10
# ENV and RUN is needed to set to the correct time zone
# An alpine based image you have to install the tzdata first
RUN apk add --no-cache tzdata
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install CherryPy
RUN pip install requests
COPY /deployments/test/test_app_service.py .
EXPOSE 8888
ENTRYPOINT ["python", "test_app_service.py"]