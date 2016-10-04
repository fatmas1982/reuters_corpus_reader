from reuters_reader import rcv1
import sys
import ft
from pprint import pprint

#I'm showing off, admittedly.
pprint(
    ft.histo(
        ft.multidex(
            rcv1.reader(sys.argv[1]), "bip:topics:1.0")))


