from __future__ import annotations

import argparse
import os
import re
import sys
from typing import IO
from typing import Sequence

from constants.data import TAB_SIZE
from utils.scope import get_scope_depth, is_scope_end
from utils.error import ErrorHandler, UnsupportedCaseStructure

TEST_GROUP_BEGIN_REGEX = r'  void TestGroup[0-9]*\(\) \{.*'
CASE_FUNCTION_REGEX = r'[ ]*CASE\(.*'
CASE_NUMERATION_REGEX = r'^\s*//[ ]*([Cc]ase){0,1}[ ]*\([0-9]*(\-[0-9]*){0,1}\).*'
CASE_NUMERATION_NO_COMMENTS_REGEX = r'^\s*//[ ]*([Cc]ase){0,1}[ ]*\([0-9]*(\-[0-9]*){0,1}\)'
CASE_INSIDE_SCOPE_REGEX = r'.*\{\s*(CASE\(.*\);)\s*\}.*'


error = ErrorHandler();

def enumerate_case(start_case: int, end_case: int, scope_depth: int, comment: str) -> str:
  leading_spaces_cnt = TAB_SIZE * (scope_depth + 1)
  comment = comment.rstrip()
  if start_case != end_case:
    return ' ' * leading_spaces_cnt + f'// Case ({start_case}-{end_case}){comment}\n'
  else:
    return ' ' * leading_spaces_cnt + f'// Case ({start_case}){comment}\n'

def handle_check_case_block(lines: Sequence[str], start_line_num: int, scope_depth: int):
  cur_line_num = start_line_num
  new_case = 0

  while True:
    cur_line = lines[cur_line_num]

    # if it is CASE function
    if re.match(CASE_FUNCTION_REGEX, cur_line):
      cur_line_num += 1
      new_case += 1

      # this CASE is one scope deeper than we expected
      if get_scope_depth(cur_line) != scope_depth+1:
        error.raise_error(UnsupportedCaseStructure("There are CASE(s) inside another scope, could've been a loop. Operation aborted!"))
    
    # if line is empty or closing bracket of test group, we break
    elif is_scope_end(cur_line, scope_depth) or cur_line.isspace():
      break

    # we assume that it as the part of CASE function. too lazy to code language automata for this
    else:
      cur_line_num += 1
  
  return cur_line_num, new_case

def handle_get_existing_comment(line: str) -> str:
  if not re.match(CASE_NUMERATION_REGEX, line):
    return False, ''

  # case_numeration_span[0] should be zero
  case_numeration_len = re.match(CASE_NUMERATION_NO_COMMENTS_REGEX, line).span()[1]
  comment = line[case_numeration_len:]

  return True, comment


def fix_file(file_obj: IO[str]) -> int:
  try:
    lines = file_obj.readlines()
    result_lines: Sequence[str] = []

    case_counter = 0
    max_iterated_line = -1
    added_line_exist = False
    new_case = 0
    inside_test_group = False
    scope_depth = None

    for line_num, line in enumerate(lines):

      # we are in test group scope, resetting values
      if re.match(TEST_GROUP_BEGIN_REGEX, line):
        case_counter = 1
        inside_test_group = True
        scope_depth = get_scope_depth(line)
      
      # test group scope ends
      elif is_scope_end(line, scope_depth):
        inside_test_group = False
        scope_depth = None

      elif re.match(CASE_FUNCTION_REGEX, line) and line_num >= max_iterated_line:
        if not inside_test_group:
          error.raise_error(UnsupportedCaseStructure("There are CASE(s) not in testGroup function. Operation aborted!"))

        max_iterated_line, new_case = handle_check_case_block(lines, line_num, scope_depth)

        commentExisted, comment = handle_get_existing_comment(lines[line_num-1])

        # check added line
        added_line = enumerate_case(case_counter, case_counter+new_case-1, scope_depth, comment)
        if added_line != lines[line_num-1]:
          added_line_exist = True

        if commentExisted:
          result_lines[-1] = added_line
          print(added_line)
          print(line)
        else:
          result_lines.append(added_line)
    
        case_counter += new_case
    
      result_lines.append(line)
    # if we need to update
    if added_line_exist:
      return 1, ''.join(result_lines)
    else:
      return 0, ''

  except UnsupportedCaseStructure as e:
    print(e)
    return 0, ''

  except Exception as e:
    print('Something is wrong:\n', e)
    print(sys.exc_info()[2])
    raise e


def main(argv: Sequence[str] | None = None) -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument('filenames', nargs='*', help='Filenames to fix')
  args = parser.parse_args(argv)

  ret_code = 0

  for filename in args.filenames:
    read_file_obj = open(filename, 'r+')

    error.init_fix_file(filename)
    is_error, result = fix_file(read_file_obj)

    # if we need to rewrite the file
    if result:
      print(f'Fixing {filename}')
      open(filename, 'w').write(result)

    read_file_obj.close()
    ret_code |= is_error

  return ret_code


if __name__ == '__main__':
  raise SystemExit(main())
