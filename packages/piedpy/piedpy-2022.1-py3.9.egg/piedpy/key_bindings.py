import logging

from quo.enums import EditingMode
from quo.filters import completion_is_selected
from quo.keys import Bind

_logger = logging.getLogger(__name__)


def mycli_bindings(piedpy):
    """Custom key bindings for piedpy)"""
    bind = Bind()

    @bind.add('f2')
    def _(event):
        """Enable/Disable SmartCompletion Mode."""
        _logger.debug('Detected F2 key.')
        piedpy.completer.smart_completion = not piedpy.completer.smart_completion

    @bind.add('f3')
    def _(event):
        """Enable/Disable Multiline Mode."""
        _logger.debug('Detected F3 key.')
        piedpy.multi_line = not piedpy.multi_line

    @bind.add('f4')
    def _(event):
        """Toggle between Vi and Emacs mode."""
        _logger.debug('Detected F4 key.')
        if piedpy.key_bindings == "vi":
            event.app.editing_mode = EditingMode.EMACS
            piedpy.key_bindings = "emacs"
        else:
            event.app.editing_mode = EditingMode.VI
            piedpy.key_bindings = "vi"

    @bind.add('tab')
    def _(event):
        """Force autocompletion at cursor."""
        _logger.debug('Detected <Tab> key.')
        b = event.app.current_buffer
        if b.complete_state:
            b.complete_next()
        else:
            b.start_completion(select_first=True)

    @bind.add('ctrl-space')
    def _(event):
        """
        Initialize autocompletion at cursor.

        If the autocompletion menu is not showing, display it with the
        appropriate completions for the context.

        If the menu is showing, select the next completion.
        """
        _logger.debug('Detected <C-Space> key.')

        b = event.app.current_buffer
        if b.complete_state:
            b.complete_next()
        else:
            b.start_completion(select_first=False)

    @bind.add('enter', filter=completion_is_selected)
    def _(event):
        """Makes the enter key work as the tab key only when showing the menu.

        In other words, don't execute query when enter is pressed in
        the completion dropdown menu, instead close the dropdown menu
        (accept current selection).

        """
        _logger.debug('Detected enter key.')

        event.current_buffer.complete_state = None
        b = event.app.current_buffer
        b.complete_state = None

    @bind.add('escape', 'enter')
    def _(event):
        """Introduces a line break in multi-line mode, or dispatches the
        command in single-line mode."""
        _logger.debug('Detected alt-enter key.')
        if piedpy.multi_line:
            event.app.current_buffer.validate_and_handle()
        else:
            event.app.current_buffer.insert_text('\n')

    return bind
