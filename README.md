# RPI_PICO_THONNY_FROZEN_LIBRARIES_REMOTE_SERVER_BUILD
The aim of this project is to automate the process of building Raspberry Pi Pico micropython libraries into firmware, using a remote server for build while RPI and Thonny are on the Windows machine

So, the end result is:
In Thonny You have two additional buttons in the toolbar. One is "Upload to server" and another is "Build firmware on server". First one sends the library to the server where the firmware will be built in order to freeze it into the firmware, the second one builds the firmware and fully automatically downloads/uploads the firmware file from/to server AND then deploys it to raspberry pi pico. Convenient, isn't it?

![Screenshot of Thonny buttons.](README_FILES/thonny_buttons.png)

Now, let's get into the details.

## Process - under the hood

### Setup for this to work

* Windows machine, where Thonny lives and where the Raspberry Pi Pico is connected to
* Linux server (local, remote - whatever), where the firmware compilation will happen

Why not on one Windows machine, You'd probably ask. Actually I tried this, however the RPI firmware resist to be compiled so hard that it was way easier to do it on the remote Linux server.

### Process itself

So, the steps are as follows:

1. You create Your micropython library code - probably in Thonny, however maybe somewhere else.
2. Next, when this file is opened in Your Thonny editor (here it is important that it is Thonny :) ) You click on the "Upload to server" button. Please make sure that nothing is executed on RPI Pico and You have a shell down in Thonny waiting for the commands to be executed!
3. What happens next is the Thonny plugin "reupload_custom_firmware" executes a script "upload_pico.bat" with the current opened filename as a parameter
4. In this script the following happens:
   - the file determined by mentioned filename is scp'ed from Windows machine into Linux server
   - on the Linux server the script is executed ("copy_for_rebuild_pico.sh") which moves the files into the correct directory (this exists in order to give more control over what can be performed during the upload)
6. Next, the same upload may be done for other libraries which are aimed to be frozen in firmware.
7. When all of the libraries are uploaded, please make sure yet another time that nothing is executed on RPI Pico and You have a shell down in Thonny waiting for the commands to be executed!
8. Then You press the "Build firmware on server" button.
9. What happens next is the Thonny plugin "reupload_custom_firmware" executes a script "build_pico.bat"
10. In this script the following happens:
    - on the Linux server the script is executed ("rebuild_pico.sh") which builds the firmware into "firmware.uf2" file
    - the firmware file "firmware.uf2" is scp'ed from Linux server into Windows machine
12. Next, the plugin executes in the Thonny shell (the one at the bottom, mentioned before) the Python commands to reboot RPI Pico into the BOOTSEL mode. You don't need to press any buttons! All will be done by the plugin
13. After this, when the RPI Pico is rebooted, the plugin executes picotool which uploads the firmware file received earlier into RPI Pico
14. After the upload, RPI Pico will reboot automatically. The plugin will wait for a couple of seconds while this happens
15. Then the plugin will restart Thonny's backend, which is equivalent to pressing the "Stop/Restart backend" button
16. You have the RPI Pico with the firmware which encompasses Your libraries as frozen in the firmware. Enjoy!

## How to make this work?

_This section will be written a little bit later. Now it is work in progress_

Scheme:

* Windows machine
  * Setup SSH
  * Setup Picotool
    * Setup MSYS2
    * Build picotool
    * Install WINUSB driver using zadig
  * Copy-paste scripts into desired location. Setup config file.
  * Dowload Thonny repository
  * Copy-paste plugin "reupload_custom_firmware" into desired location. Setup config file.
  * Build Thonny with the plugin
* Linux server
  * upload copy and build scripts into the server
  * git clone the micropython repo into desired directory
  * upload the build_automatically script
  * upload the scripts config file and setup it
  * install missing packages for building the micropython
  * verify if build is executed correctly
