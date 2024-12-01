"""This code is bad on purpose!"""

from pathlib import Path
from collections import defaultdict   

for file in Path('.').iterdir():
    print(file.stem)



    
