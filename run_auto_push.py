import subprocess
from datetime import datetime

if True:
    subprocess.run(["bash", "/home/joaopaiva/Economic-News-Classifier-NLP-Model/auto_push.sh"])
else:
    print("Today is not Friday. No push was made.")