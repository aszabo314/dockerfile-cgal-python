FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential cmake \
    libopencv-dev \
    libsuitesparse-dev \
    tar \
    git \
    vim \
    nano \
    libboost-all-dev libgmp10-dev \
    libmpfr-dev zlib1g-dev \
    libeigen3-dev libglew1.5-dev libipe-dev \
    libmpfi-dev libqglviewer-dev-qt5 \
    libinsighttoolkit4-dev libtbb-dev git \
    swig g++ \
    python-dev          \
    cimg-dev  \
    petsc-dev \
    tcl-dev \
    python3-numpy        \
    python3-scipy        \
    python3-sympy        \
    python3-matplotlib   \
    python3-pandas       \
    python3-sklearn      \
    libcgal-dev \
  && apt-get clean

RUN cd && git clone https://github.com/cgal/cgal-swig-bindings \
    && cd cgal-swig-bindings \
    && mkdir build \
    && cd build  \
    && cmake -DCGAL_DIR=/usr/lib/CGAL -DBUILD_PYTHON=ON -DBUILD_JAVA=OFF .. \
    && make -j 4
