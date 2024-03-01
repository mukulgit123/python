from library.GeneratePersonData import GeneratePersonData
from library.CreateCSV import CreateCSV
import argparse as ap

def main():
    '''This is the main function'''
    argParser = ap.ArgumentParser()
    argParser.add_argument('-f' , '--filename', type=str, help='The name of the file to be created')
    argParser.add_argument( '-r', '--recordcount', type=int, help='The number of records to be created')
    args = argParser.parse_args()
    filename = args.filename
    recordcount = args.recordcount

    try:
        person = GeneratePersonData()
        CreateCSV(person, filename, recordcount)
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()