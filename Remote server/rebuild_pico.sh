#!/bin/sh
cd "$(dirname "$0")"
. ./pico.config
echo "Starting build process..."
sh -C $firmware_builder_script
echo "Build process complete."