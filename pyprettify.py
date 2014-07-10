# -*- coding: utf-8 -*-

import os
import sys

import click
from bs4 import BeautifulSoup as bs

@click.command()
@click.argument('infiles', type=click.File('r'), nargs=-1)
@click.option('--suffix', default='_prettified',
              help='filename after file basename')
@click.option('--encoding', default='utf-8',
              help='encoding you want to use when writing prettified files')
def cli(infiles, suffix, encoding):
    """
    This script prettifies HTML or XML files.
    """
    files = [infile for infile in infiles
                if os.path.splitext(infile.name)[1] in ['.html', '.xml']]
    for infile in infiles:
        soup = bs(infile.read())

        (basename, ext) = os.path.splitext(infile.name)
        outfile = basename + suffix + ext

        with open(outfile, 'w') as f:
            if sys.version_info < (3, 0, 0):
                f.write(soup.prettify().encode(encoding))
            else:
                f.write(soup.prettify())
