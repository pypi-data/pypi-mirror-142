"""

This module provides different io functions

"""

import glob
import os
from typing import List


def read_file(filename: str) -> str:
    """Read file

    Nothing special

    Args:
      filename (str): File to read

    Returns:
      str: content of file
    """

    try:
        with open(filename, "r", encoding='utf8') as file_object:
            # Append 'hello' at the end of file
            content = file_object.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
        content = ""
    return content


def write_file(filename: str, content: str):
    """Write file

    Args:
      filename (string): File to write
      content (string): content which will be written to file

    Returns:
      None: nothing
    """
    with open(filename, "w", encoding='utf8') as file_object:
        file_object.write(content)


def get_all_files_from_folder(folder: str, extension: str = "") -> List[str]:
    """ Get all files from a folder

    Args:
      folder (string): folder
      extension (string): extension e.g. .md

    Returns:
      List[str]: filename of files in folder
    """
    list_of_files_full = glob.glob(str(folder + "/*" + extension))
    list_of_files = []
    for filename_full in list_of_files_full:
        filename = os.path.basename(filename_full)
        list_of_files.append(filename)
    return list_of_files


def get_all_folders_from_folder(start_folder: str) -> List[str]:
    """ Get all folders from a folder

    Args:
      start_folder (string): folder

    Returns:
      List[str]: name of folders in folder

    Raises:
        StopIteration: An error occurred accessing the smalltable.
    """
    try:
        folders = next(os.walk(start_folder))[1]
        print(folders)
    except StopIteration:
        folders = []
        print(f"folder {start_folder} not found")

    return folders
