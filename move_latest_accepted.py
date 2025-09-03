import os
import shutil

submissions_dir = '/home/user/apps/leetcode-solutions/leetcode-export/submissions'
python3_dir = '/home/user/apps/leetcode-solutions/python3'

if not os.path.exists(submissions_dir):
    print(f"Error: submissions directory '{submissions_dir}' does not exist.")
    exit(1)

if not os.path.exists(python3_dir):
    os.makedirs(python3_dir)

for submission in os.listdir(submissions_dir):
    sub_path = os.path.join(submissions_dir, submission)
    if not os.path.isdir(sub_path):
        continue

    py_files = [
        f for f in os.listdir(sub_path)
        if f.endswith('.py')
    ]
    py_files.reverse()
    accepted_files = []
    for py_file in py_files:
        file_path = os.path.join(sub_path, py_file)
        if "Accepted" in file_path:
            dest_path = os.path.join(python3_dir, os.path.basename(submission + ".py"))
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} to {dest_path}")
            break


