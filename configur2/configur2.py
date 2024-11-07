'''import os
from typing import Dict
import xml.etree.ElementTree as ET


def get_configuration(configuration_file_path: str) -> Dict:
    data = {}
    root = ET.parse(configuration_file_path).getroot()
    for child in root:
        data[child.tag] = child.text
    return data


def get_dot(repository_path: str, branch_name: str) -> str:
    date_format = "format:'%Y-%m-%d %H:%M:%S'"
    format = "format:'%an %cd'"

    raw_log = os.popen(f"git -C {repository_path} --no-pager log "
                       f"--no-merges "
                       f"--date={date_format} "
                       f"--pretty={format} "
                       f"{branch_name}").read()

    lines = raw_log.splitlines()

    # Raw no-merges commits
    dot = "digraph G { \n"
    for i in range(0, len(lines) - 1):
        dot += f"\"{lines[i]}\"-> \"{lines[i + 1]}\"\n"

    # Merge commits

    # 7d377d3 f5a7e6b
    merge_hashes = os.popen(f"git -C {repository_path} --no-pager log "
                            f"--merges "
                            f"--pretty=format:'%p' "
                            f"{branch_name}").read()

    lines = merge_hashes.splitlines()
    for line in lines:
        h1, h2 = line.split()[0], line.split()[1]

        s1 = os.popen(f"git -C {repository_path} --no-pager show "
                      f"-s "
                       f"--date={date_format} "
                       f"--pretty={format} "
                      f"{h1}").read()
        s2 = os.popen(f"git -C {repository_path} --no-pager show "
                      f"-s "
                       f"--date={date_format} "
                       f"--pretty={format} "
                      f"{h2}").read()

        dot += f"\"{s1}\" -> \"{s2}\"\n"
    dot += "}"

    return dot


def write_result_file(result_file_path: str, dot: str):
    with open(result_file_path, 'w') as f:
        f.write(dot)


def convert_to_svg(result_file_path: str, visualizer_path):
    os.popen(f"{visualizer_path} {result_file_path} -Tsvg > {result_file_path.split('.')[0]}.svg")


def main():
    configuration = get_configuration("config.xml")

    visualizer_path = configuration["visualizer_path"]
    repository_path = configuration["repository_path"]
    result_file_path = configuration["result_file_path"]
    branch_name = configuration["branch_name"]

    dot = get_dot(repository_path, branch_name)
    write_result_file(result_file_path, dot)
    convert_to_svg(result_file_path, visualizer_path)

    print(dot)


if __name__ == '__main__':
    main()
'''

import os
import tomllib

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
path = "C:/Users/artem/source/repos/configur1"
dir = os.getcwd()
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
out = os.popen(f"mmdc -c {dir}\\init.json -i {dir}\\temp.mmd -o {dir}\\output.png").read()
print(out)
#mmdc -i 'input.mmd' -o 'output.png'

# text_raw_nomerge = os.popen("git -C C:/Users/artem/fireshare --no-pager log --no-merges").read()
# text_split_nomerge = text_raw_nomerge.splitlines()
# commit_hashes_nomerge = get_commits(text_split_nomerge)
# text_raw_merge = os.popen("git -C C:/Users/artem/fireshare --no-pager log --merges").read()
# text_split_merge = text_raw_merge.splitlines()
# commit_hashes_merge = get_commits(text_split_merge)