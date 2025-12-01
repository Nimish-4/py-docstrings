import libcst as cst
import re
from pathlib import Path
from docstrings.cst import FunctionAndClassVisitor


def test_function_docstring():
    function_str = """def calculate(a, b):
    return a+b"""

    module = cst.parse_module(function_str)
    visitor = FunctionAndClassVisitor(file_path=None)
    modified_module = module.visit(visitor)

    result_loc = Path("docstrings/tests/testfiles/result_1.py")
    result_code = result_loc.read_text(encoding="utf-8")

    lines_modified = modified_module.code.split("\n")
    lines_result = result_code.split("\n")

    # either lines consist of whitespaces, or they match exactly
    for i in range(len(lines_modified)):
        assert (
            re.match(r"\s+", lines_modified[i])
            or re.match(r"\s+", lines_result[i])
            or lines_modified[i] == lines_result[i]
        )

def test_class_docstring():
    class_str = """class xyz:
    def __init__(self, a, b):
        \"""Initialize `a` and `b`\"""
        self.a = a
        self.b = b
    
    def calculate(self):
        \"""Calculate the sum of `a` and `b`\"""
        return self.a + self.b"""

    module = cst.parse_module(class_str)
    visitor = FunctionAndClassVisitor(file_path=None)
    modified_module = module.visit(visitor)

    result_loc = Path("docstrings/tests/testfiles/result_2.py")
    result_code = result_loc.read_text(encoding="utf-8")

    lines_modified = modified_module.code.split("\n")
    lines_result = result_code.split("\n")

    for i in range(len(lines_modified)):
        assert (
            re.match(r"\s+", lines_modified[i])
            or re.match(r"\s+", lines_result[i])
            or lines_modified[i] == lines_result[i]
        )

def test_mixed_docstring():
    mixed_str = """import math

class xyz:
  def __init__(self, a, b):
        
        self.a = a
        self.b = b
    
  def calculate_log(self):
        \"""Return sum of logarithms of `a` and `b`\"""
        def log(x):
            return math.log(x)

        return log(self.a) + log(self.b)"""

    module = cst.parse_module(mixed_str)
    visitor = FunctionAndClassVisitor(file_path=None)
    modified_module = module.visit(visitor)

    result_loc = Path("docstrings/tests/testfiles/result_3.py")
    result_code = result_loc.read_text(encoding="utf-8")

    lines_modified = modified_module.code.split("\n")
    lines_result = result_code.split("\n")

    for i in range(len(lines_modified)):
        assert (
            re.match(r"\s+", lines_modified[i])
            or re.match(r"\s+", lines_result[i])
            or lines_modified[i] == lines_result[i]
        )
