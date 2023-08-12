#!/bin/sh
cd "$(dirname "$0")"
cd mpy-cross
make clean
make
cd ..
cd ports/rp2
make submodules -j4
make -j4 BOARD=PICO_W