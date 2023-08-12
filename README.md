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
