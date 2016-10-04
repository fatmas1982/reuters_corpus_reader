# Reuters Corpus Reader

The corpus is available from Reuters and NIST: [http://trec.nist.gov/data/reuters/reuters.html]

## Use

Import a specific reader from a specific subcorpus. Takes path to the corpus as
an argument. See example.py for more detail.

Each iteration over the generator produces a dict that contains most of the 
content of the original XML. Pretty transparent.

### I want an API.

Ok, do this:

    class Reuters_API:
        def __init__(self,output_from_reader):
            self.vars().update(output_from_reader)
