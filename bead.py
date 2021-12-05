import xml.etree.ElementTree as et
import pandavro as pdx
import pandas as pd

def readfromxmltodict(path):
    tree = et.parse(path)
    root = tree.getroot()

    data = {}
    i = 0
    for child in root:
        data[i] = []
        for ch in child:
            data[i].append(ch.text)
        i+=1
    return data

dictData = readfromxmltodict("C:\\Users\\User\\Desktop\\Projekt III\\harmadikfeladat.xml")

OUTPUT_PATH="C:\\Users\\User\\Desktop\\Projekt III\\harmadikfeladatvege.avro"
pdx.to_avro(OUTPUT_PATH,pd.DataFrame.from_dict(dictData))
saved = pdx.read_avro(OUTPUT_PATH)
print(saved)


