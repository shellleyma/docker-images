FROM wilburding/py_boost

RUN apt-get update && apt-get install -y \
	libenchant-dev \
	libfreetype6-dev \
	libjpeg-dev \
	libpng12-dev \
	liblapack-dev \
	libopenblas-dev \
	gfortran
# libenchant-dev will pull back system python
# liblapack-dev/libopenblas-dev/gfortran for scipy

COPY pip_req.txt /usr/src/
RUN pip install -r /usr/src/pip_req.txt

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

VOLUME ['/usr/src/app', '/var/log']

CMD ["python"]
