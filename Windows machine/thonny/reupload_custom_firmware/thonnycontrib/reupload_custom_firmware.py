from thonny import get_workbench, get_shell, get_runner
from thonny.shell import ShellView
from tkinter.messagebox import showinfo
from thonny.running import Runner

from os import system as sys_command, path as sys_path
from time import sleep as do_sleep

from json import load as json_file_load

def read_config():
    script_dir = sys_path.dirname(__file__)
    rel_path = "config.json"
    f = open(sys_path.join(script_dir, rel_path))
    config = json_file_load(f)
    f.close()
    return config

def upl():
    config = read_config()
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if not editor:
        showinfo("Upload failed", "Cannot access editor for some reason, thus cannot upload file.")
        return
    filename = editor.get_filename(True)
    if not filename:
        showinfo("Upload failed", "Cannot get filename from editor, thus cannot upload file.")
        return
    sys_command(('{} "{} {}"' if(config['platform'] == 'windows') else '{} {} {}').format("cmd /c" if(config['platform'] == 'windows') else "/bin/sh",config['local']['upload_script_location'],filename))
    shell = get_shell()
    shell.print_error("[REMOTE UPLOAD] Upload done.\n")
    

def bld():
    config = read_config()
    sys_command('{} "{}"'.format("cmd /c" if(config['platform'] == 'windows') else "/bin/sh",config['local']['build_script_location']))
    shell = get_shell()
    shell.print_error("[REMOTE BUILD] Build done.\n")
    runner = get_runner()
    shell.print_error("[REMOTE BUILD] Remote build done. Reboot into bootloader...\n")
    shell.submit_magic_command("import machine;machine.bootloader()")
    sys_command(('{} "{} load -x "{}""' if(config['platform'] == 'windows') else '{} {} load -x {}').format("cmd /c" if(config['platform'] == 'windows') else "/bin/sh", config['local']['picotool_location'], config['local']['firmware_location']))
    shell.print_error("[REMOTE BUILD] Firmware upload done.")
    do_sleep(3)
    runner.restart_backend(clean=True)

def load_plugin():
    get_workbench().add_command(command_id="upload_to_server",
                                menu_name="run",
                                command_label="Upload to server",
                                caption="Upload to server",
                                handler=upl,
                                image="save-file_Linux_2x.png",
                                include_in_toolbar=True)
    get_workbench().add_command(command_id="build_on_server",
                                menu_name="run",
                                command_label="Build firmware on server",
                                caption="Build firmware on server",
                                handler=bld,
                                image="step-over_2x.png",
                                include_in_toolbar=True)