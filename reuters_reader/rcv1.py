import os
import xml.etree.ElementTree as ET

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
        for f in files:
            print D,"/", f
            data_path = os.sep.join([dir_path, f])
            raw_data = open(data_path).read()
            xml_parse = ET.fromstring(raw_data)

            def get_text(tag): 
                stuff = xml_parse.find(tag)
                if stuff: return stuff.text
                else: return None

            text = "\n\n".join([p.text for p in xml_parse.findall(".//p")])
            title = get_text("title")
            headline = get_text("headline")
            byline = get_text("byline")
            dateline = get_text("dateline")
            lang = xml_parse.attrib["xml:lang"]
            
            code_classes = [c.attrib["class"] 
                                for c in xml_parse.findall(".//codes")]
            codes = {cc: [c.attrib["code"] for c in 
                            xml_parse.findall(".//codes[@class='%s']/code"%cc)]
                        for cc in code_classes}
            dcs = {d.attrib["element"]: d.attrib["value"] 
                            for d in xml_parse.findall(".//dc")}
            
            #assemble output
            output = {"text": text,
                      "title": title,
                      "headline": headline,
                      "byline": byline,
                      "dateline": dateline,
                      "lang": lang,
                      "corpus_path": corpus_path,
                      "corpus_subdirectory": D,
                      "corpus_filename": f,
                      }

            # merge and flatten the other big hashmaps
            output.update(codes.items())
            output.update(dcs.items())

            yield output

            
