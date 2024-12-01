"""This code is bad on purpose!"""

from collections import defaultdict
from pathlib import Path

for file in Path(".").iterdir():
    print(file.stem)
