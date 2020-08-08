#Author: Sagar Pandey


from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

def killprocess():
    process = subprocess.Popen(['ps', '-A'], stdout = subprocess.PIPE)
    out, err = p.communicate()

    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)
            
shot_date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

pic_id = "Shots"

trigger_command = ["--trigger-capture"]
download_command = ["--get-all-files"]

folder_name = shot_date + pic_id

#create a folder to save images say "images"

save_location = "home/s/Desktop/gphoto/images" + folder_name

def createSaveFolder():
    try:
            os.makedirs(save_location)
    except:
            print("Falied creating dir...already exists")
    os.chdir(save_location)

def captureImages():
    gp(trigger_command)
    sleep(5)
    gp(download_command)
    print("captured!!!")



killprocess()
createSaveFolder()
captureImages()
