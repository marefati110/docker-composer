import argparse
import sys

from collections import OrderedDict


ignoreEvn = ['PATH']

ignoreLables = [
    "com.docker.compose.container-number",
    "com.docker.compose.config-hash",
    "com.docker.compose.oneoff",
    "com.docker.compose.project",
    "com.docker.compose.project.config_files",
    "com.docker.compose.project.working_dir",
    "com.docker.compose.service",
    'com.docker.compose.config-hash',
    "com.docker.compose.version",
]

serviceOrder = [
    'image',
    'container_name',
    'command',
    'restart,'
    'networks',
    'labels',
    'logging',
    'environment',
    'ports',
    'volumes'
]


def customOrder(data: dict, items: list):

    new_data = OrderedDict()

    for i in items:
        try:
            new_data[i] = data[i]
        except:
            pass


    for j in data.keys():
        if j not in items:
            new_data[j] = data[j]

    return new_data


def find(source: dict, path: str):

    splited_path = path.split('.')

    d = source.copy()

    for key in splited_path:
        try:
            d = d[key]
        except:
            return None

    return d


def find_and_set(source: dict, source_path: str, dest: dict, dest_path: str):

    splited_dest_path = dest_path.split('.')

    found = find(source, source_path)

    if found == None:
        return False

    counter = 1
    for key in splited_dest_path:

        if counter == len(splited_dest_path):
            dest[key] = found
        else:
            dest[key] = {}
            dest = dest[key]

        counter += 1

    return True
