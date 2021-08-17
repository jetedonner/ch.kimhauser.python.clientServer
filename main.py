import sys, getopt
import os
#import os.system

# This is a sample Python script.
authorName = "JeteDonner"
appVersion = "0.0.1"
appDate = "2021-08-17"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')


def print_help():
    print(f'Client-Server python script by {authorName}\nVersion: {appVersion}, {appDate}\n')
    print(f'Usage: ')
    print(f'-help, -h\t\t\tDisplay this help text')
    print(f'-server, -s\t\tStart the server')
    print(f'-client, -c\t\tStart the server')
# Press the green button in the gutter to run the script.

def main(argv):
   # try:
   opts, args = getopt.getopt(argv,"h:s:c:")
   # except getopt.GetoptError:
   #   print_help()
   #   sys.exit(2)
   for opt, arg in opts:
      if opt == '--help':
         #print(f'test.py -i <inputfile> -o <outputfile>')
         print_help()
         sys.exit()
      elif opt == '-s':
          host = arg[0:]
          port = argv[2]

          cur_dir = os.path.abspath(".")
          print(f'{cur_dir}/app-server.py {host} {port}')
          os.system(f'{cur_dir}/app-server.py {host} {port}')
      # elif opt in ("-i", "--ifile"):
      #    inputfile = arg
      # elif opt in ("-o", "--ofile"):
      #    outputfile = arg
   # print(f'Input file is "', inputfile)
   # print(f'Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])

# if __name__ == '__main__':
#     print_hi('PyCharm')
#     print(f'Number of arguments:', len(sys.argv), 'arguments.')
#     print(f'Argument List:', str(sys.argv))
#     if len(sys.argv) >= 2:
#         if :


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
