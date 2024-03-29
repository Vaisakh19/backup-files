import os
import shutil
import datetime
import schedule
import time
src_dir="C:/Users/USER/Videos/Captures" #collect files from source directory
dest_dir="D:/leetcode" #destination for copying files
def copy_folder(src,dest):
  today=datetime.date.today()
  destination=os.path.join(dest,str(today)) #join the destination with the date and time of the day
  try:
    shutil.copytree(src,destination)
    print(f"Folder copied to {destination}")
  except FileExistsError:
    print(f"Folder already exists in {destination}")
def s(): #function created to copy the files and frequent calls
  copy_folder(src_dir,dest_dir)
schedule.every().day.at("18:30").do(s)   #scheduled call set by the programmer to backup the files
while True:
  schedule.run.pending()
  time.sleep(60)    