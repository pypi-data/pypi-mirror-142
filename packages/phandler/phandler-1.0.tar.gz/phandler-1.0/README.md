phandler is a package to fully control printing in Python. You can delete any line with just one command.

First of all, you need to create prints handler object that will handle all the prints:
>>> ph = phandler.prints_handler(False)   # <- Set argument to True if you want to ignore errors

Now, you can print something:
>>> ph.print('Hello world!')

If you want to delete any line, just use this command and specify target line number (counting from bottom):
>>> ph.delete_line(1)   # <- This will delete last printed line

You can use use inputs also:
>>> name = ph.input('Enter your name: ')   # <- Now, prompt and input value are removable with delete_line command

To clear saved prints you can use:
>>> ph.clear(True)   # <- Set argument to True if you want to clear all visible lines too