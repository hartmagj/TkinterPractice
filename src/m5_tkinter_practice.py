"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Grant Hartman.
"""  # d: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # d: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()
    # ------------------------------------------------------------------
    # d: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()

    # ------------------------------------------------------------------
    # d: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    hello = ttk.Button(frame1, text='click this button')
    hello.grid()

    # ------------------------------------------------------------------
    # d: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    hello['command'] = lambda: print_boi()

    # ------------------------------------------------------------------
    # d: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    box = ttk.Entry(frame1)
    box.grid()

    hibi = ttk.Button(frame1, text='annie are you ok?')
    hibi['command'] = lambda: print_hg(box)
    hibi.grid()

    # ------------------------------------------------------------------
    # d: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    box2 = ttk.Entry(frame1)
    box2.grid()
    printer = ttk.Button(frame1, text='print the string a certain amount')
    printer.grid()
    printer['command'] = lambda: print_input(box, box2)
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    def print_boi():
        print('hey')

    def print_hg(entry):
        contents = entry.get()
        if contents == 'ok':
            print('Hello')
        else:
            print('Goodbye')

    def print_input(entry, num):
        contents = entry.get()
        n = int(num.get())

        for k in range(n):
            print(contents)

    root.mainloop()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
