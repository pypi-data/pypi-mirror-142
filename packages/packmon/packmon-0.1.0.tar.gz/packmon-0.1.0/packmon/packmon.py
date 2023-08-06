# encode: utf-8
"""
Packmon : Packages Monitoring to increase quality and kill obsolescence
Author : Mindiell
License : APGLv3+
Package : https://pypi.org/project/packmon/
"""

import argparse
from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import zip_longest
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.request import Request, urlopen


VERSION = "0.1.0"
BOT_URL = "https://framagit.org/Mindiell/packmon/-/blob/develop/bot.md"
PYPI_STATUS = {
    "Development Status :: 1 - Planning": "planning",
    "Development Status :: 2 - Pre-Alpha": "pre-alpha",
    "Development Status :: 3 - Alpha": "alpha",
    "Development Status :: 4 - Beta": "beta",
    "Development Status :: 5 - Production/Stable": "stable",
    "Development Status :: 6 - Mature": "mature",
    "Development Status :: 7 - Inactive": "inactive",
}
PYPI_LICENSE = {
    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication": "",
    "License :: CeCILL-B Free Software License Agreement (CECILL-B)": "",
    "License :: CeCILL-C Free Software License Agreement (CECILL-C)": "",
    "License :: DFSG approved" : "DFSG approved",
    "License :: Eiffel Forum License (EFL)" : "Eiffel Forum License (EFL)",
    "License :: Free For Educational Use" : "Free For Educational Use",
    "License :: Free For Home Use" : "Free For Home Use",
    "License :: Free To Use But Restricted" : "Free To Use But Restricted",
    "License :: Free for non-commercial use" : "Free for non-commercial use",
    "License :: Freely Distributable" : "Freely Distributable",
    "License :: Freeware" : "Freeware",
    "License :: GUST Font License 1.0" : "GUST Font License 1.0",
    "License :: GUST Font License 2006-09-30" : "GUST Font License 2006-09-30",
    "License :: Netscape Public License (NPL)" : "Netscape Public License (NPL)",
    "License :: Nokia Open Source License (NOKOS)" : "Nokia Open Source License (NOKOS)",
    "License :: OSI Approved" : "OSI Approved",
    "License :: OSI Approved :: Academic Free License (AFL)" : "Academic Free License (AFL)",
    "License :: OSI Approved :: Apache Software License" : "Apache Software License",
    "License :: OSI Approved :: Apple Public Source License" : "Apple Public Source License",
    "License :: OSI Approved :: Artistic License" : "Artistic License",
    "License :: OSI Approved :: Attribution Assurance License" : "Attribution Assurance License",
    "License :: OSI Approved :: BSD License" : "BSD License",
    "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)" : "Boost Software License 1.0 (BSL-1.0)",
    "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)" : "CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
    "License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)" : "Common Development and Distribution License 1.0 (CDDL-1.0)",
    "License :: OSI Approved :: Common Public License" : "Common Public License",
    "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)" : "Eclipse Public License 1.0 (EPL-1.0)",
    "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)" : "Eclipse Public License 2.0 (EPL-2.0)",
    "License :: OSI Approved :: Eiffel Forum License" : "Eiffel Forum License",
    "License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)" : "European Union Public Licence 1.0 (EUPL 1.0)",
    "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)" : "European Union Public Licence 1.1 (EUPL 1.1)",
    "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)" : "European Union Public Licence 1.2 (EUPL 1.2)",
    "License :: OSI Approved :: GNU Affero General Public License v3" : "GNU Affero General Public License v3",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)" : "GNU Affero General Public License v3 or later (AGPLv3+)",
    "License :: OSI Approved :: GNU Free Documentation License (FDL)" : "GNU Free Documentation License (FDL)",
    "License :: OSI Approved :: GNU General Public License (GPL)" : "GNU General Public License (GPL)",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)" : "GNU General Public License v2 (GPLv2)",
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)" : "GNU General Public License v2 or later (GPLv2+)",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)" : "GNU General Public License v3 (GPLv3)",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)" : "GNU General Public License v3 or later (GPLv3+)",
    "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)" : "GNU Lesser General Public License v2 (LGPLv2)",
    "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)" : "GNU Lesser General Public License v2 or later (LGPLv2+)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)" : "GNU Lesser General Public License v3 (LGPLv3)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)" : "GNU Lesser General Public License v3 or later (LGPLv3+)",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)" : "GNU Library or Lesser General Public License (LGPL)",
    "License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)" : "Historical Permission Notice and Disclaimer (HPND)",
    "License :: OSI Approved :: IBM Public License" : "IBM Public License",
    "License :: OSI Approved :: ISC License (ISCL)" : "ISC License (ISCL)",
    "License :: OSI Approved :: Intel Open Source License" : "Intel Open Source License",
    "License :: OSI Approved :: Jabber Open Source License" : "Jabber Open Source License",
    "License :: OSI Approved :: MIT License" : "MIT License",
    "License :: OSI Approved :: MIT No Attribution License (MIT-0)" : "MIT No Attribution License (MIT-0)",
    "License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)" : "MITRE Collaborative Virtual Workspace License (CVW)",
    "License :: OSI Approved :: MirOS License (MirOS)" : "MirOS License (MirOS)",
    "License :: OSI Approved :: Motosoto License" : "Motosoto License",
    "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)" : "Mozilla Public License 1.0 (MPL)",
    "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)" : "Mozilla Public License 1.1 (MPL 1.1)",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)" : "Mozilla Public License 2.0 (MPL 2.0)",
    "License :: OSI Approved :: Nethack General Public License" : "Nethack General Public License",
    "License :: OSI Approved :: Nokia Open Source License" : "Nokia Open Source License",
    "License :: OSI Approved :: Open Group Test Suite License" : "Open Group Test Suite License",
    "License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)" : "Open Software License 3.0 (OSL-3.0)",
    "License :: OSI Approved :: PostgreSQL License" : "PostgreSQL License",
    "License :: OSI Approved :: Python License (CNRI Python License)" : "Python License (CNRI Python License)",
    "License :: OSI Approved :: Python Software Foundation License" : "Python Software Foundation License",
    "License :: OSI Approved :: Qt Public License (QPL)" : "Qt Public License (QPL)",
    "License :: OSI Approved :: Ricoh Source Code Public License" : "Ricoh Source Code Public License",
    "License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)" : "SIL Open Font License 1.1 (OFL-1.1)",
    "License :: OSI Approved :: Sleepycat License" : "Sleepycat License",
    "License :: OSI Approved :: Sun Industry Standards Source License (SISSL)" : "Sun Industry Standards Source License (SISSL)",
    "License :: OSI Approved :: Sun Public License" : "Sun Public License",
    "License :: OSI Approved :: The Unlicense (Unlicense)" : "The Unlicense (Unlicense)",
    "License :: OSI Approved :: Universal Permissive License (UPL)" : "Universal Permissive License (UPL)",
    "License :: OSI Approved :: University of Illinois/NCSA Open Source License" : "University of Illinois/NCSA Open Source License",
    "License :: OSI Approved :: Vovida Software License 1.0" : "Vovida Software License 1.0",
    "License :: OSI Approved :: W3C License" : "W3C License",
    "License :: OSI Approved :: X.Net License" : "X.Net License",
    "License :: OSI Approved :: Zope Public License" : "Zope Public License",
    "License :: OSI Approved :: zlib/libpng License" : "zlib/libpng License",
    "License :: Other/Proprietary License" : "Other/Proprietary License",
    "License :: Public Domain" : "Public Domain",
    "License :: Repoze Public License" : "Repoze Public License",
}


class Package:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.status = kwargs.get("status", "Unknown")
        self.license = kwargs.get("license", "Unknown")
        self.vulnerabilities_raw = kwargs.get("vulnerabilities", 0)
        self.version = kwargs.get("version", "Unknown")
        self.last_version= kwargs.get("last_version", "Unknown")
        self.last_update = kwargs.get("last_update", datetime.today())
        self.update_limit = kwargs.get("update_limit", datetime.today())

    @property
    def vulnerabilities(self):
        return str(self.vulnerabilities_raw)

    @property
    def last_update_human(self):
        return datetime.strftime(self.last_update, "%Y-%m-%d")

    @property
    def status_level(self):
        if self.status in ("planning", "pre-alpha", "alpha", "inactive"):
            return "\033[1m\033[31m"
        elif self.status in ("", "beta"):
            return "\033[1m\033[33m"
        return ""

    @property
    def version_level(self):
        if self.version != self.last_version:
            versions = re.split(r"[.-]", self.version)[:-1]
            last_versions = re.split(r"[.-]", self.last_version)[:-1]
            for version, last_version in zip_longest(versions, last_versions):
                if version != last_version:
                    return "\033[1m\033[31m"
            return "\033[1m\033[33m"
        return ""

    @property
    def update_level(self):
        if self.last_update < self.update_limit:
            return "\033[1m\033[33m"
        return ""

    @property
    def vulnerabilities_level(self):
        if self.vulnerabilities_raw == 0:
            return "\033[92m"
        return "\033[1m\033[31m"

    def to_json(self):
        return {
            "name": self.name,
            "status": self.status,
            "license": self.license,
            "vulnerabilities": self.vulnerabilities_raw,
            "last_version": self.last_version,
            "last_update": datetime.strftime(self.last_update, "%Y-%m-%dT%H:%M:%S"),
        }


def update(requirements, days, no_cache):
    update_limit = datetime.now() - timedelta(days=days)

    # Managing .packmon folder into user's folder for caching
    home_path = Path.home().joinpath(".packmon")
    os.makedirs(home_path, exist_ok=True)
    cache_file = os.path.join(home_path, "packages.json")

    # Loading cached packages
    if not no_cache:
        try:
            with open(cache_file) as file_handler:
                cache_packages = json.load(file_handler)
        except FileNotFoundError:
            cache_packages = []
    else:
        cache_packages = []

    packages = []
    size = len(requirements)
    for idx, requirement in enumerate(requirements):
        try:
            if len(requirement.strip()) == 0 or requirement.strip()[0] == "#":
                continue
            print(f"\r{idx+1}/{size}", end="", file=sys.stderr, flush=True)
            result = re.match(
                "(?P<name>[^>~=<]+)((?P<condition>[>~=<]+)(?P<version>[^; ]+))?.*$",
                requirement,
            )
            name = result.group("name")
            version = result.group("version") or "unkown"
            # Search in cache, if not present use the internet
            for package in cache_packages:
                if name == package["name"]:
                    packages.append(Package(
                        name=package["name"],
                        status=package["status"],
                        license=package["license"],
                        vulnerabilities=package["vulnerabilities"],
                        version=version,
                        last_version=package["last_version"],
                        last_update=datetime.strptime(
                            package["last_update"],
                            "%Y-%m-%dT%H:%M:%S",
                        ),
                        update_limit=update_limit,
                    ))
                    break
            else:
                datas = None
                request = Request(
                    f"https://pypi.org/pypi/{name}/json",
                    headers={"User-Agent": f"packmon/{VERSION} ({BOT_URL})"}
                )
                result = urlopen(request)
                if result.status == 200:
                    datas = json.loads(result.read())
                    for classifier in datas["info"]["classifiers"]:
                        if classifier in PYPI_STATUS:
                            status = PYPI_STATUS[classifier]
                        if classifier in PYPI_LICENSE:
                            license = PYPI_LICENSE[classifier]
                    vulnerabilities = len(datas.get("vulnerabilities", []))
                    last_version = sorted(
                        [v for v in datas["releases"] if len(datas["releases"][v]) > 0],
                        key=lambda x: datetime.strptime(
                            datas["releases"][x][0]["upload_time"], "%Y-%m-%dT%H:%M:%S"
                        ),
                    )[-1]
                    last_update = datas["releases"][last_version][0]["upload_time"]
                packages.append(Package(
                    name=name,
                    status=status,
                    license=license,
                    vulnerabilities=vulnerabilities,
                    version=version,
                    last_version=last_version,
                    last_update=datetime.strptime(last_update, "%Y-%m-%dT%H:%M:%S"),
                    update_limit=update_limit,
                ))
                # Little pause in order not to spam pypi
                time.sleep(0.2)
        except Exception as e:
            print(
                f"Error while trying to find informations on {name}"
                f" with version {version}",
                file=sys.stderr,
            )
            print(e, file=sys.stderr)
            continue
    print()

    # Caching packages
    cache_modified = False
    for package in packages:
        for cache_package in cache_packages:
            if package.name == cache_package["name"]:
                break
        else:
            cache_packages.append(package.to_json())
            cache_modified = True
    if cache_modified:
        with open(cache_file, "wt") as file_handler:
            json.dump(cache_packages, file_handler, indent=2)

    return packages


def output(components, color=True):
    if color:
        HEADER = "\033[96m"
        NORMAL = "\033[0m"
    else:
        HEADER = ""
        NORMAL = ""

    # Computing columns sizes
    @dataclass
    class Header:
        slug: str
        name: str
        size: int
        min_size: int
        reduced: bool
    terminal_width = os.get_terminal_size().columns
    headers = [
        Header("name", "name", 5, 5, False),
        Header("status", "status", 7, 7, False),
        Header("license", "license", 8, 8, False),
        Header("version", "version", 8, 8, False),
        Header("last_version", "last version", 13, 13, False),
        Header("last_update_human", "last update", 12, 12, False),
        Header("vulnerabilities", "vulnerabilities", 15, 15, False),
    ]
    for header in headers:
        for component in components:
            if len(getattr(component, header.slug)) >= header.size:
                header.size = len(getattr(component, header.slug)) + 1
    while sum([h.size for h in headers]) > terminal_width:
        # Reduce largest column, but not too much
        difference = min(sum([h.size for h in headers]) - terminal_width, 10)
        largest = [h.size for h in headers].index(max([h.size for h in headers]))
        if headers[largest].size - difference > headers[largest].min_size:
            headers[largest].size -= difference
            headers[largest].reduced = True

    # Printing values
    def display_value(value, header, level=""):
        if header.reduced and len(value) > header.size - 1:
            result = value[:header.size-2] + "\u2026"
        else:
            result = value
        return level + result + " " * (header.size - len(result)) + NORMAL

    os.system("")
    line = HEADER
    for header in headers:
        line += header.name + " " * (header.size - len(header.name))
    print(line + NORMAL)
    for comp in components:
        line = display_value(comp.name, headers[0])
        line += display_value(comp.status, headers[1], comp.status_level if color else "")
        line += display_value(comp.license, headers[2])
        line += display_value(comp.version, headers[3], comp.version_level if color else "")
        line += display_value(comp.last_version, headers[4])
        line += display_value(comp.last_update_human, headers[5], comp.update_level if color else "")
        line += display_value(comp.vulnerabilities, headers[6], comp.vulnerabilities_level if color else "")
        print(line)


def main():
    parser = argparse.ArgumentParser(description="Analyse requirements FILE(s).")
    # version
    parser.add_argument(
        "--version",
        action="store_const",
        const=True,
        default=False,
        help="output version information and exit",
    )
    # clear cache
    parser.add_argument(
        "--clear-cache",
        action="store_const",
        const=True,
        default=False,
        help="delete cache file and exit",
    )
    # requirement file
    parser.add_argument(
        "FILE",
        nargs="*",
        help="files to analyse; if no file given, read standard input",
    )
    # colorize output
    parser.add_argument(
        "--no-color",
        action="store_const",
        const=True,
        default=False,
        help="output is displayed without ANSI escapes colors",
    )
    # delay (in days)
    parser.add_argument(
        "--delay",
        default=360,
        type=int,
        help=(
            "delay, in days, after which last release is considered obsolete "
            "(default to 360)"
        ),
    )
    # no cache
    parser.add_argument(
        "--no-cache",
        action="store_const",
        const=True,
        default=False,
        help="does not use cache (each package needs a request to pypi to retrieve its "
            "informations)",
    )
    args = parser.parse_args()
    if args.version:
        print(f"Version {VERSION}")
    if args.clear_cache:
        # Clear cache
        home_path = Path.home().joinpath(".packmon")
        os.makedirs(home_path, exist_ok=True)
        cache_file = os.path.join(home_path, "packages.json")
        try:
            os.remove(cache_file)
        except FileNotFoundError:
            # No cache present
            pass
    else:
        requirements = []
        if len(args.FILE) == 0:
            line = input()
            try:
                while line != "":
                    if len(line.strip()) != 0 and line.strip()[0] != "#":
                        requirements.append(line)
                    line = input()
            except EOFError:
                pass
        else:
            for filename in args.FILE:
                with open(filename) as file_handler:
                    for line in file_handler.read().splitlines():
                        if len(line.strip()) != 0 and line.strip()[0] != "#":
                            requirements.extend([line])

        output(update(requirements, args.delay, args.no_cache), not args.no_color)
