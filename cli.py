import argparse
import json
import ast
import os

parser = argparse.ArgumentParser(description='Import a new dataset or query the datastore')
parser.add_argument('-s', '--select', help='Specify columns to be selected')
parser.add_argument('-o', '--order', help='Specify order in which to display results')
parser.add_argument('-f', '--filter', help='Specify filter to use on results')
parser.add_argument('-u', '--upload', help='Specify path of file to upload')

def main():
  args = parser.parse_args()
  if (args.upload):
    if (os.path.isfile('./RecordSet.txt')):
      with open('./RecordSet.txt', 'r') as rs:
        recordSet = eval(rs.read())
    else:
      recordSet = {}
    try:
      with open(args.upload, 'r') as newRecordSet:
        records = newRecordSet.read().strip().split('\n')
        records.pop(0)
    except FileNotFoundError:
      print('Invalid file path')
  else:
    print('no file')
  try:
    for record in records:
      recordDetails = record.split('|')
      recordID = recordDetails[0] + recordDetails[1] + recordDetails[2]
      recordSet[recordID] = {
          'stb': recordDetails[0],
          'title': recordDetails[1],
          'provider': recordDetails[2],
          'date': recordDetails[3],
          'rev': recordDetails[4],
          'view_time': recordDetails[5]
      }
  except:
    print('Input file improperly formatted')
  with open('./RecordSet.txt', 'w') as rs:
    rs.write(str(recordSet))

if __name__ == '__main__':
  main()
