import os
current_dir = os.path.dirname(__file__)
relative_path = "file.py"
absolute = os.path.join(current_dir, relative_path)
print(absolute)
