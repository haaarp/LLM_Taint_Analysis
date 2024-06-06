import argparse
import taint_specification
import aosp_crawler
import gps_crawler  


parser = argparse.ArgumentParser('DocFlow main')
parser.add_argument('-op', '--operation', help="select the operation",
                    choices=['specification','search','classifier','sem_classifier']) 
parser.add_argument('-i','--input', help="file input path",required=False)
parser.add_argument('-o', '--output', help="file output path",required=False)
parser.add_argument('-cr','--crawler', help='' , 
                    choices=['aosp','libraries'],required=False)
parser.add_argument('-pr','--preprocessing', help='generates method representations',
                    choices=['FA','FB','FC','FD','FE','FF'],required=False)



if __name__ == "__main__":

    args = parser.parse_args()

    if args.operation is not None:
        if args.operation == 'specification':
            if input.endswith('.csv'):
                taint_specification.generate_taint_spec(args.input,args.output)
            else:
                print('Please enter a csv file an input')
        elif args.operation in ('search','classifier','sem_classifier'):
            print (f'Please look at the scripts in /core/ for {args.operation}') 
    elif args.crawler is not None:
        print('Please look at the script /core/core_utils.py for preprocessing')
    elif args.preprocessing is not None:
        print('Please look at the script /core/core_utils.py for preprocessing')

    print('DocFlow terminated')

            
