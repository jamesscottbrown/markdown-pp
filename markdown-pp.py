#!/usr/bin/env python

# Copyright (C) 2010 John Reese
# Licensed under the MIT license

import sys
import MarkdownPP
import argparse

description = "Preprocessor for Markdown files." \

parser = argparse.ArgumentParser(description=description)
parser.add_argument('FILENAME', help='Input file name')
parser.add_argument("-o", "--output", help="Output file name." \
    + " If no output file is specified, writes output to stdout.")
parser.add_argument('-e', '--exclude',\
 help='List of modules to exclude, separated by commas. ' \
 +'Available modules: ' + ", ".join(MarkdownPP.modules.keys()))
args = parser.parse_args()


mdpp = open(args.FILENAME, "r")
if args.output:
	md = open(args.output, "w")
else:
	md = sys.stdout

modules = MarkdownPP.modules.keys();

if args.exclude:
	for module in args.exclude.split(','):
		if module in modules:
			modules.remove(module)
		else:
			print "Cannot exclude ", module, " - no such module"
 
MarkdownPP.MarkdownPP(input=mdpp, output=md, modules=modules)

mdpp.close()
md.close()
