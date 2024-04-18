import os
import shutil
import subprocess
from datetime import datetime

# Setup paths and file names.

notes_path = "C:\\Users\\mafaz\\Documents\\Notes"
today_path = os.path.join(notes_path, "Today")

date_text = datetime.today().strftime('%Y-%m-%d')

file_name = date_text + ".md"
file_heading = "# " + date_text + "\n"
today_file_path = os.path.join(today_path, file_name)

file_exists_in_today = os.path.exists(today_file_path)

vs_code_command = ["code", notes_path, today_file_path]

if not file_exists_in_today:
  # Move everything from Today up to Notes
  for item in os.listdir(today_path):
    source_item_path = os.path.join(today_path, item)
    destination_item_path = os.path.join(notes_path, item)
    shutil.move(source_item_path, destination_item_path)

  # Create the new file and write the starting data
  with open(today_file_path, "w") as file:
    file.write(file_heading)
    file.write("\n")
    file.write("- ")
  
# Open the file in VSCode
subprocess.run(vs_code_command, shell=True)