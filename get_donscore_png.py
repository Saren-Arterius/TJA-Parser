#!/usr/bin/python3
from subprocess import call
from os.path import join, abspath
from sys import argv
from os import chdir, listdir, name as osname
from re import sub

tja_donscore_converter = "TJAConverter.exe"
donscore = "donscore.exe"


def clean_convert_txt(convert_txt):
    convert_txt = sub("#title .*", "#title song", convert_txt)
    convert_txt = sub("#difficulty .*", "#difficulty oni", convert_txt)
    return convert_txt


if __name__ == "__main__":

    chdir(argv[1])

    if osname == "nt":
        call([tja_donscore_converter, argv[2]])
    else:
        call(["wine", tja_donscore_converter, argv[2]])

    with open(join(argv[1], "convert.txt"), "r+", errors = "ignore") as tmp_convert_file:
        content = clean_convert_txt(tmp_convert_file.read())
        tmp_convert_file.seek(0)
        tmp_convert_file.write(content)
        tmp_convert_file.truncate()

    for i in range(10):
        if osname == "nt":
            call([abspath(donscore), abspath("convert.txt")])
        else:
            call(["xvfb-run", "-a", "wine", abspath(donscore), abspath("convert.txt")])
        if "convert.png" in listdir("."):
            break