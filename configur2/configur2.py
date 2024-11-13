import os
import argparse

def get_commits(mas: list):
    hashes = []
    for i in range(len(mas)):
        if mas[i].split(' ')[0] == "commit":
            hashes.append({"hash": mas[i].split(' ')[1]})
            if mas[i+1].split(':')[0] == "Merge":
                hashes[-1]["type"] = "merge"
                hashes[-1]["merging"] = [mas[i+1].split(' ')[1], mas[i+1].split(' ')[2]]
            else:
                hashes[-1]["type"] = "commit"
                hashes[-1]["merging"] = []

    return hashes


mmd_file = "temp.mmd"
dir = os.getcwd()
parser = argparse.ArgumentParser(description='dependencies visualizer')
parser.add_argument("-r")
parser.add_argument("-o")
parser.add_argument("--vis")
args = parser.parse_args()
# path = "C:/Users/Ekaterina/PycharmProjects/konfigur1"
# of = f"{dir}\\output.png"
# vis = "C:/Users/Ekaterina/AppData/Roaming/nvm/v23.2.0/mmdc.cmd"
path = args.r    # "C:/Users/artem/source/repos/configur1"
of = args.o    # f"{dir}\\output.png"
vis = args.vis    # "C:/Users/artem/AppData/Roaming/nvm/v23.1.0/mmdc.cmd"
f = open(mmd_file, 'w')
f.write("flowchart TB\n")
text_raw_full = os.popen(f"git -C {path} --no-pager log").read()
text_split_full = text_raw_full.splitlines()
commits = get_commits(text_split_full)
commits.reverse()
for i in range(len(commits) - 1):
    if commits[i+1]["type"] == "commit":
        p1 = commits[i]["hash"][:7]
        p2 = commits[i+1]["hash"][:7]
        f.write(f"\t{p1} --> {p2}\n")

for i in range(len(commits)):
    if commits[i]["type"] == "merge":
        p1 = commits[i]["merging"][0]
        p2 = commits[i]["merging"][1]
        p3 = commits[i]["hash"][:7]
        f.write(f"\t{p1} --> {p3}\n")
        f.write(f"\t{p2} --> {p3}\n")

for i in range(len(commits)):
    p = commits[i]["hash"][:7]
    text = os.popen(f"git -C {path} ls-tree -r --name-only {p}").read()
    f.write(f"\t{p}({text})\n")

f.close()
out = os.popen(f"{vis} -c {dir}\\init.json -i {dir}\\temp.mmd -o {of}").read()
print(out)
#mmdc -i 'input.mmd' -o 'output.png'

# text_raw_nomerge = os.popen("git -C C:/Users/artem/fireshare --no-pager log --no-merges").read()
# text_split_nomerge = text_raw_nomerge.splitlines()
# commit_hashes_nomerge = get_commits(text_split_nomerge)
# text_raw_merge = os.popen("git -C C:/Users/artem/fireshare --no-pager log --merges").read()
# text_split_merge = text_raw_merge.splitlines()
# commit_hashes_merge = get_commits(text_split_merge)