#!/usr/bin/env python3

# This script is a standalone utility to strip solution blocks from Jupyter notebooks.
# It is intended to be used in projects where installing the full 'jphtools' library is not desired.
#
# Requirements:
# - nbformat: You can install it via pip:
#   pip install nbformat
#
# Usage:
# python strip_notebook_solutions.py
#
# This script reads "workshop-complete.ipynb" and writes the student version to "workshop.ipynb".

# This script will strip sections of cells between
# '# BEGIN_SOLUTION' & '# END_SOLUTION' and
# replace it with '# ADD YOUR CODE HERE'
# to produce student-friendly versions of Jupyter notebooks
import nbformat
import re


def strip_solutions_from_notebook(input_path, output_path):
    """
    Removes solution blocks from a Jupyter notebook and writes the result to output_path.
    Solution blocks are marked by '# BEGIN_SOLUTION' and '# END_SOLUTION'.
    """
    with open(input_path, "r") as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.source = re.sub(
                r"# BEGIN_SOLUTION.*?# END_SOLUTION",
                "# ADD YOUR CODE HERE",
                cell.source,
                flags=re.DOTALL,
            )

    with open(output_path, "w") as f:
        nbformat.write(nb, f)


def main():
    input_path = "workshop-complete.ipynb"
    output_path = "workshop.ipynb"
    strip_solutions_from_notebook(input_path, output_path)
    print(f"Successfully created {output_path} from {input_path}")


if __name__ == "__main__":
    main()
