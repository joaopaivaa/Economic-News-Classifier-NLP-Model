import subprocess
from datetime import datetime

if datetime.now().weekday() == 4:
    subprocess.run(["bash", "/home/joaopaiva/Economic-News-Classifier-NLP-Model/auto_push.sh"])
else:
    print("Today is not Friday. No push was made.")