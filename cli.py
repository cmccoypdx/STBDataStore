import argparse

parser = argparse.ArgumentParser(description='Import a new dataset or query the datastore')
parser.add_argument('-s', '--select', help='Specify columns to be selected')
parser.add_argument('-o', '--order', help='Specify order in which to display results')
parser.add_argument('-f', '--filter', help='Specify filter to use on results')
parser.add_argument('-i', '--import', help='Specify path of file to import')

def main():
  args = parser.parse_args()
  print(args)

if __name__ == '__main__':
  main()