import sys

from quo import confirm, prompt
from quo.errors import Abort
from quo.types import ParamType
from .parseutils import is_destructive


class ConfirmBoolParamType(ParamType):
    name = 'confirmation'

    def convert(self, value, param, ctx):
        if isinstance(value, bool):
            return bool(value)
        value = value.lower()
        if value in ('yes', 'y'):
            return True
        elif value in ('no', 'n'):
            return False
        self.fail('%s is not a valid boolean' % value, param, ctx)

    def __repr__(self):
        return 'BOOL'


BOOLEAN_TYPE = ConfirmBoolParamType()


def confirm_destructive_query(queries):
    """Check if the query is destructive and prompts the user to confirm.

    Returns:
    * None if the query is non-destructive or we can't prompt the user.
    * True if the query is destructive and the user wants to proceed.
    * False if the query is destructive and the user doesn't want to proceed.

    """
    prompt_text = ("You're about to run a destructive command.\n"
                   "Do you want to proceed? (y/n)")
    if is_destructive(queries) and sys.stdin.isatty():
        return prompt(prompt_text, type=BOOLEAN_TYPE)


def confirm(*args, **kwargs):
    """Prompt for confirmation (yes/no) and handle any abort exceptions."""
    try:
        return confirm(*args, **kwargs)
    except Abort:
        return False


def prompt(*args, **kwargs):
    """Prompt the user for input and handle any abort exceptions."""
    try:
        return prompt(*args, **kwargs)
    except Abort:
        return False
