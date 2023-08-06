"""Discover and lint all json files."""

import argparse
import json
import os
import sys
import typing

DiscoverReturnType = typing.Generator[str, None, None]


def parse_args() -> argparse.Namespace:
    """Parse some args."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root_dir",
        default=os.getcwd(),
        help="Directory to search for json files.",
        nargs="?",
    )
    parser.add_argument(
        "-e",
        "--extension",
        action="append",
        default=[".json"],
        dest="extensions",
        help="Extensions to treat as json files.",
    )
    parser.add_argument(
        "-i", "--ignore", action="append", default=[], help="Directories to ignore."
    )
    parser.add_argument(
        "--follow", action="store_true", help="Follow symlinks.", required=False
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print helpful output.",
        required=False,
    )
    return parser.parse_args()


def is_valid_json(file_path: str) -> bool:
    """Return True if the file is valid json. False otherwise."""
    try:
        with open(file_path) as fil:
            json.load(fil)
    except json.JSONDecodeError:
        return False
    else:
        return True


def directory_is_hidden(directory: str) -> bool:
    """Returns True if the directory is a "hidden" directory. False otherwise."""
    return directory.startswith(".")


def discover_files(
    root_dir: str, extensions: typing.List[str], ignore: typing.List[str], follow: bool
) -> DiscoverReturnType:
    """Discover files that we should lint."""
    for entry in os.scandir(path=root_dir):
        if entry.is_symlink():
            if not follow:
                continue
        if entry.is_dir():
            if entry.name not in ignore and not directory_is_hidden(entry.name):
                yield from discover_files(entry.path, extensions, ignore, follow)
        else:
            if any(entry.name.endswith(ext) for ext in extensions):
                yield entry.path


def main() -> None:
    """Main."""
    args = parse_args()
    invalid = []
    paths = discover_files(args.root_dir, args.extensions, args.ignore, args.follow)
    for path in paths:
        if args.verbose:
            print(f"Checking path {path}")
        if not is_valid_json(path):
            invalid.append(path)
    for path in invalid:
        print(f"File is not valid json: {path}")
    # Exit unclean for a non-empty list.
    sys.exit(invalid != [])
