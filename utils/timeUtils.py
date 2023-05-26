import sys
import threading


def repeatIt(watiSecs, fncToRun, repeat):
    ticket = threading.Event()
    ticket.daemon = True

    counter = 0
    while not ticket.wait(watiSecs):
        fncToRun()
        counter += 1

        if counter == repeat:
            sys.exit()
