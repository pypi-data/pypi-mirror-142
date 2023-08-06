"""
Parse string in to FileNamePart define in namer_types.
"""
import argparse
import logging
from pathlib import PurePath
import re
import sys
from typing import List
from namer.types import FileNameParts


def name_cleaner(name: str) -> str:
    """
    Given the name parts, following a date, but preceding the file extension, attempt to glean
    extra information and discard useless information for matching with the porndb.
    """
    # truncating cruft
    for size in ['2160p', '1080p', '720p', '4k',  '3840p']:
        name = re.sub(r"[\.\- ]"+size+r"[\.\- ]{0,1}.*", "", name)
    # remove trailing ".XXX."
    name = re.sub(r"[\.\- ]{0,1}XXX[\.\- ]{0,1}.*$", "", name)
    name = re.sub(r'\.', ' ', name)
    # Leave act/part in as a test.
    #match = re.search(r'(?P<name>.+)[\.\- ](?P<part>[p|P][a|A][r|R][t|T][\.\- ]{0,1}[0-9]+){0,1}' +
    #    r'(?P<act>[a|A][c|C][t|T][\.\- ]{0,1}[0-9]+){0,1}[\.\- ]*$',name)
    #act = None
    #if match:
    #    if match.group('act') is not None:
    #        act = match.group('act')
    #    if match.group('part') is not None:
    #        act = match.group('part')
    #    if act is not None:
    #        name = match.group('name')
    return name


def parse_file_name(filename: str) -> FileNameParts:
    """
    Given an input name of the form site-yy.mm.dd-some.name.part.1.XXX.2160p.mp4,
    parses out the relevant information in to a structure form.
    """
    file_name_parts = FileNameParts()
    file_name_parts.extension = PurePath(filename).suffix[1:]
    file_name_parts.name = PurePath(filename).stem
    match = re.search(r'(?P<site>[a-zA-Z0-9\.\-\ ]+[a-zA-Z0-9])[\.\- ]+(?P<year>[0-9]{2}(?:[0-9]{2})?)[\.\- ]+' +
                      r'(?P<month>[0-9]{2})[\.\- ]+(?P<day>[0-9]{2})[\.\- ]+' +
                      r'((?P<trans>[T|t][S|s])[\.\- ]+){0,1}(?P<name>.*)\.(?P<ext>[a-zA-Z0-9]{3,4})$',filename)
    if match:
        prefix = "20" if len(match.group('year'))==2 else ""
        file_name_parts.date = prefix+match.group('year')+"-"+match.group('month')+"-"+match.group('day')
        file_name_parts.name = name_cleaner(match.group('name'))
        #file_name_parts.name = name_act_tuple[0]
        #file_name_parts.act = name_act_tuple[1]
        file_name_parts.site = re.sub(r'[\.\-\ ]','',match.group('site'))
        trans = match.group('trans')
        file_name_parts.trans = (not trans is None) and (trans.strip().upper() == 'TS')
        file_name_parts.extension = match.group('ext')
        file_name_parts.source_file_name = filename
    else:
        logging.warning("Could not parse file name: %s", filename)
    return file_name_parts


def main(arglist: List[str]):
    """
    Attempt to parse a name.
    """
    description = ("You are using the file name parser of the Namer project.  " +
        "Expects a single input, and will output the contents of FileNameParts, which is the internal input " +
        "to the namer_metadatapi.py script. "+
        "Output will be the representation of that FileNameParts.\n")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-f", "--file", help="String to parse for name parts", required=True)
    args = parser.parse_args(arglist)
    print(parse_file_name(args.file))

if __name__ == "__main__":
    main(arglist=sys.argv[1:])
