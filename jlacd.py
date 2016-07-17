#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
選定図書総目録CD-ROMのデータ変換ツール
"""

__copyright__ = "Copyright (C) 2015 CALIL Inc."
__author__ = "Ryuuji Yoshimoto <ryuuji@calil.jp>"

import click

import re


@click.command()
@click.argument('input', type=click.File('r'), metavar=u'<ファイル名>')
def convert_jla(input):
    """選定図書総目録CD-ROMのデータ変換"""
    data = input.read()
    items = re.findall(r'00000000([^\x00]+)', data)
    for item in items:
        lines = re.split(u"\$A", item.decode("cp932", "replace"))

        index = 0  # ISBN Index
        if lines[2] == u"JP$B00000000":
            index = 1
        elif lines[3] == u"JP$B00000000":
            index = 2
        if index == 0:
            isbn = ""
        else:
            isbn = lines[1]
        isbn = re.sub('\$M([^\$]+)', r'', isbn)
        title = lines[4 + index]
        if not re.search(u"\$", lines[5 + index]):
            title += " [" + lines[5 + index] + "]"
            publisher_ = lines[6 + index]
        else:
            if not re.search(u"\$F", lines[5 + index]):
                publisher_ = lines[5 + index]
            else:
                publisher_ = lines[6 + index]
        authors = re.findall('\$F([^\$]+)', title)
        author = ",".join(authors)
        title = re.sub('\$F([^\$]+)', r'', title)
        title = re.sub('\$B([^\$]+)', r' \1', title)
        publisher = ",".join(re.findall('\$B([^\$]+)', publisher_))
        year = ",".join(re.findall('\$D([^\$]+)', publisher_))
        if year == "":
            year = ",".join(re.findall('\$D([^\$]+)', title))
        title = re.sub('\$D([^\$]+)', r' \1', title)
        id_ = re.split(" ", lines[3 + index])[1]
        print (id_ + "\t" + isbn + "\t" + title + "\t" + author + "\t" + publisher + "\t" + year).encode("utf-8")


if __name__ == '__main__':
    convert_jla()
