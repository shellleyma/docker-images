# py_boost
FROM python:2.7
MAINTAINER wilbur "wilbur@kuailexue.com"

RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

ENV BOOST_VERSION 1.58.0
ENV BOOST_WITH_PYTHON 1

RUN mkdir -p /usr/src/boost
WORKDIR /usr/src/boost
RUN wget http://downloads.sourceforge.net/project/boost/boost/1.58.0/boost_1_58_0.tar.bz2 -O boost.tar.bz2 \
	&& tar -xf boost.tar.bz2 \
	&& rm -f boost.tar.bz2 \
	&& cd boost_1_58_0 \
	&& ./bootstrap.sh --with-python=/usr/local/bin/python \
	&& ./b2 -j"$(nproc)" cxxflags="-std=c++11" variant=release link=shared runtime-link=shared threading=multi --prefix=/usr/local install \
	&& ldconfig \
	&& rm -rf /usr/src/boost
