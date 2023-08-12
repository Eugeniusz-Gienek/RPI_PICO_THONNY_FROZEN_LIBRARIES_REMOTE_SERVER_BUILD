#!/bin/sh
cd "$(dirname "$0")"
. ./pico.config
for var in "$@"
do
    echo -n Copying $var into modules dir...
    cp $uploaded_files_dir$var $rpi_firmware_modules_dir
    echo [ OK ]
done