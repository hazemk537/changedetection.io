import os

folder_path = '/home/up-user/Downloads/Projects/changedetection.io/changedetectionio'  # Replace with the actual folder path
text_to_add = 'import sys\nsys.path.append("changedetectionio")\n\n'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(text_to_add + content)