#!/usr/bin/python3

import argparse, subprocess
import os.path
import math
import ascii

def normalize(value, max):
    return math.ceil((value / max) * 10)

def arguments():
    parser = argparse.ArgumentParser(description="Find out git habits.")
    parser.add_argument("repo", type=str, help="Repository directory")
    parser.add_argument("committer", type=str, help="Limit the log to this regex, same as git log --committer")
    parser.add_argument("--merges", dest="merges", action="store_true", help="Consider merging habits")
    return parser.parse_args()

def printer(renderer, dataset):
    renderer.render(dataset)

def main():
    args = arguments()
    gitdir = '{0}/{1}'.format(args.repo, ".git")

    if not os.path.exists(gitdir):
        print("{0} does not exists".format(gitdir))
        exit(-1)

    command = "git --git-dir {0} log --committer={1} --pretty=\"%cd\" |" \
              "cut -d' ' -f4 | " \
              "cut -d: -f1 | " \
              "sort -n | " \
              "uniq -c".format(gitdir, args.committer)
    out = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

    datalist = []
    sum = 0
    max = 0
    for row in out.splitlines():
        terms = row.decode().lstrip().split(' ')
        t = (float(terms[0]), int(terms[1]))
        datalist.append(t)
        sum += t[0]
        max = t[0] if t[0] > max else max

    normalized = [(normalize(elm[0], max), elm[1]) for elm in datalist]
    printer(ascii.AsciiRenderer(), normalized)

#    print(normalized,max)

if __name__ == '__main__':
    main()
