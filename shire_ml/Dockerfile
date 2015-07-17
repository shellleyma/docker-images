FROM wilburding/shire_base

ENV CRFPP_VERSION 0.58
RUN mkdir -p /usr/src/crfpp
WORKDIR /usr/src/crfpp
RUN wget ftp://ftp.fr.netbsd.org/pub/pkgsrc/distfiles/CRF++-${CRFPP_VERSION}.tar.gz \
        && tar -xf CRF++-${CRFPP_VERSION}.tar.gz \
        && cd CRF++-${CRFPP_VERSION} \
        && ./configure --prefix=/usr/local \
        && make \
        && make install \
        && ldconfig \
        && cd python \
        && python setup.py install \
        && rm -rf /usr/src/crfpp

WORKDIR /usr/src
RUN git clone https://github.com/lzhang10/maxent.git \
        && cd maxent \
        && ./configure --prefix=/usr/local \
        && make \
        && make install \
        && ldconfig \
        && cd python \
        && python setup.py install \
        && rm -rf /usr/src/maxent


WORKDIR /usr/src/app
