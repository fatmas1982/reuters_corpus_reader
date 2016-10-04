from reuters_reader import rcv1
import sys
import ft
from pprint import pprint


docs = []
doc_counts = 0
docs_no_topic = 0
for doc in rcv1.reader(sys.argv[1]):
    doc_counts += 1
    if "bip:topics:1.0" in doc:
        docs.append(doc)
    else:
        docs_no_topic += 1

print "Total docs:", doc_counts
print "Docs w/o topic:", docs_no_topic

print "Counting topics..."
pprint(ft.histo(ft.multidex(docs, "bip:topics:1.0")))


