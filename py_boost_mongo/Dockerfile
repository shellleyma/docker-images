# py_boost_mongo
FROM registry.guangzixuexi.com/thematrix/py_boost

ENV MONGO_CXX_DRIVER_VERSION 1.0.2

RUN pip install SCons
RUN mkdir -p /usr/src/mongo-cxx-driver
WORKDIR /usr/src/mongo-cxx-driver
RUN wget https://github.com/mongodb/mongo-cxx-driver/archive/legacy-1.0.2.tar.gz -O legacy.tar.gz \
	&& tar -xf legacy.tar.gz \
	&& cd mongo-cxx-driver-legacy-1.0.2 \
	&& scons --prefix=/usr/local --c++11=on install \
	&& ldconfig \
	&& rm -rf /usr/src/mongo-cxx-driver

RUN pip uninstall -y SCons && rm -rf /tmp/* /var/tmp/* /root/.cache/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
