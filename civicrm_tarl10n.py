#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Robert Davidson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import functools, optparse, tarfile

def tcopy(itar, otar, options, filter=None):
    for ix, mem in enumerate(itar):
        if ix and filter :
            if not filter(options, mem):
                continue
        f = itar.extractfile(mem)
        mem.uid = mem.gid = 0
        mem.uname = options.owner
        mem.gname = options.group
        if mem.isdir():
            mem.mode = options.dir_perms
            otar.addfile(mem)
        elif mem.isfile():
            mem.mode = options.file_perms
            otar.addfile(mem, f)
        else:
            print "%s is neither file nor directory!" % (mem.name,)

def filter_names(options, tarinfo):
    for loc in options.country_code:
        if tarinfo.name.find(loc) >= 0:
            return True
    return False

parser = optparse.OptionParser()
parser.add_option('-i', '--input-civi-tarball')
parser.add_option('-l', '--input-l10n-tarball')
parser.add_option('-o', '--output-tarball')
parser.add_option('-u', '--owner', default='www-data', help="defaults to www-data")
parser.add_option('-g', '--group', default='www-data', help="defaults to www-data")
parser.add_option('-f', '--file-perms', default=0640, type=int, help="defaults to 0640 - note: octal")
parser.add_option('-d', '--dir-perms', default=0750, type=int, help="defaults to 0750 - note: octal")
parser.add_option('-c', '--country-code', action='append', help="multiple codes may be specified - e.g. -c en_GB -c fr_CA")
options, args = parser.parse_args()
#print options, args

ctar = tarfile.open(name=options.input_civi_tarball)
otar = tarfile.open(name=options.output_tarball, mode="w:gz")
tcopy(ctar, otar, options)
ctar.close()
ltar = tarfile.open(name=options.input_l10n_tarball)
tcopy(ltar, otar, options, filter_names)
ltar.close()
otar.close()
