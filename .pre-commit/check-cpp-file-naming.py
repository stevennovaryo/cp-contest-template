#!/usr/bin/env python

import re
import sys

# Define the file types that you want to check
FILE_TYPES = [".cpp", ".py", ".java"]

# === Regexes ===
SOLUTION_FILE_REGEX = r"^solution.*"

COMPLEXITY_REGEX = r"(-[a-z]([a-z]|\(|\)|\^|[0-9])*){0,1}"
FILE_TYPES_REGEX = r"\.(cpp|py|java)"

SOLUTION_FORMAT_REGEX = r"^solution(-[a-z0-9][a-z0-9]*){0,}" + COMPLEXITY_REGEX + FILE_TYPES_REGEX
# ===============


class COLOR:
  RED = "\033[1;31m"
  WHITE = "\033[1;37m"
  GREEN = "\033[1;32m"

  RED_BG = "\033[1;41m"

  FAILED = WHITE + RED_BG

  RESET = "\033[0m"


checkAllGood = True


def checkSolutionFile(files_to_check):
  checkPassed = True
  global checkAllGood

  for file_to_check in files_to_check:
    file_name_to_check = file_to_check.split("/")[-1]

    if re.match(SOLUTION_FILE_REGEX, file_name_to_check):
      if not re.match(SOLUTION_FORMAT_REGEX, file_name_to_check):
        checkPassed = False
        checkAllGood = False
        print(
          f"\t{COLOR.RED}FAILED{COLOR.RESET}: {COLOR.GREEN}{file_to_check}{COLOR.RESET} format is incorrect!"
        )

  # if not checkPassed:
  #   print(
  #  f'Solution name should match appropriate solution file name format.\n' +
  #  'In which, file should:\n' +
  #  '- start with "solution-" followed by strings of lowercase latin alphabets or numbers,\n' +
  #  '- separated by "-", and\n' +
  #  '- ended by the complexity if the author desire to include it.\n'
  #   )


def main(argv):
  # Get the list of files that are about to be committed
  files_to_check = [f for f in argv if f.endswith(tuple(FILE_TYPES))]
  if not files_to_check:
    return 0

  checkSolutionFile(files_to_check)

  if checkAllGood:
    return 0
  else:
    return 1


if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
