"""JinjaTemplateSingleStatementRule.py - Rule class to check if only a single
                                         jinja statement is present on each
                                         line.
"""
import re
import jinja2
from j2lint.linter.rule import Rule
from j2lint.utils import get_jinja_statements


class JinjaTemplateSingleStatementRule(Rule):
    """Rule class to check if only a single jinja statement is present on each
       line.
    """
    id = 'S7'
    short_description = 'single-statement-per-line'
    description = "Jinja statements should be on separate lines"
    severity = 'MEDIUM'

    def check(self, file, line):
        """Checks if the given line matches the error regex

        Args:
            file (string): file path
            line (string): a single line from the file

        Returns:
            Object: Returns True if error is found else False
        """
        if len(get_jinja_statements(line)) > 1:
            return True
        return False
