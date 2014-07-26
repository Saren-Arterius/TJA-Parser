#!/usr/bin/python3
from tja_info import *
from os.path import join
from sys import argv

if __name__ == "__main__":
    tja = TJAInfo(open(argv[1], encoding="shift-jis", errors="ignore").read())
    print(tja.headers)
    print(tja.simulate_results)
    for course, level in enumerate(tja.headers["LEVELS"]):
        if level is None:
            continue
        with open(join(TJAInfo.working_dir, "{0}-{1}.png".format(tja.headers["TITLE"], course)), "w+b") as donscore_png:
            donscore_png.write(tja.get_donscore_png(course).read())