import os

def reader(corpus_path):
    corpus_path, dirs, files = os.walk(corpus_path).next()
    if "rcv1" in dirs:
        corpus_path = os.sep.join([corpus_path,"rcv1"])
        #otherwise assuming we're already in rcv1. 
        #just want to make the behavior robust here.
        # you can pass either a Reuters corpus dir with RCV1 or RCV1 itself
        # Don't care which.

    corpus_path, dirs, files = os.walk(corpus_path).next()
    for D in dirs:
        dir_path = os.sep.join([corpus_path,D])
        dir_path, dirs, files = os.walk(dir_path).next()
        
