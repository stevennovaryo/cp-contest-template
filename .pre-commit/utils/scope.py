from constants.data import TAB_SIZE

def leading_space_count(s: str):
  return len(s) - len(s.lstrip())

def get_scope_depth(line: str):
  return leading_space_count(line) // TAB_SIZE

def is_scope_end(line: str, expected_scope_width: int):
  return (line.lstrip().rstrip() == '}' and get_scope_depth(line) == expected_scope_width)
