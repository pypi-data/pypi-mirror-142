#!python3
# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for sharepointhealth
from .logs_check import Logs
import argparse
import sys

# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Return message
message = {
    'status': OK,
    'summary': 'Example summary',
    'perfdata': 'label1=0;;;; '  # 'label'=value[UOM];[warn];[crit];[min];[max] 
}

# For multiple perdata, ensure to add space after each perfdata
# message['perfdata'] = 'label1=x;;;; '
# message['perfdata'] += 'label2=x;;;; '

# Function to parse arguments
def parse_args(args):
    """
    Information extracted from: https://mkaz.com/2014/07/26/python-argparse-cookbook/
     https://docs.python.org/3/library/argparse.html
    :return: parse.parse_args(args) object
    You can use obj.option, example:
    options = parse_args(args)
    options.user # to read username
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, 
                                     description='nagios plugin to check a word in a log file')

    parser.add_argument('-fl', '--filelocation', dest='filelocation', nargs='?', default=None, const=None,
                        help='file to check \n')
    
    parser.add_argument('-wd', '--word_to_check', dest='word_to_check', nargs='?', default=None, const=None,
                        help='word to check \n')

    parser.add_argument('-ln', '--lines_number', dest='lines_number', nargs='?', default=20, type=int, const=None,
                        help='lines number \n')
                        
    parser.add_argument('-e', '--extra_args', dest='extra_args', nargs='?', default='', const=None,
                            help='extra args to add to curl, see curl manpage  \n')


    if not args:
        raise SystemExit(parser.print_help())

    return parser.parse_args(args)

# Function to execute cli commands
def cli_execution(options):
    """
    : param: options: arguments from parse.parse_args(args) (see parse_args function)
    """
    #variables
    auth_args = ''
    retrcode = OK

    #Lines to read
    N = 20
    
    if not options.filelocation:
            sys.exit('param file location is resquired when using logs check ')
    if not options.word_to_check:
            sys.exit('param word to check is resquired when using logs check ')

    logs_obj = Logs(options.filelocation, options.word_to_check, options.lines_number)	

    def check_data():
        # use new object class Logs
        retrcode, count, lines = logs_obj.check_logs()
        return retrcode, count, lines
    
    def format_message():
        return 'Count: {} '.format(count)

    def check(retrcode):
        if retrcode == 2:
            status = CRITICAL
            message['summary'] = 'CRITICAL: '
        else:
            status = OK
            message['summary'] = 'OK: '
        return status

    # Check logic starts here
    data_code, count, lines = check_data()
    message['status'] = check(data_code)
    # Add summary    
    message['summary'] += format_message()
    message['summary'] += str(lines)
    
 
    # Add perfdata
    message['perfdata'] = 'total count={};;1;; '.format(count)
    

    # Print the message
    print("{summary}|{perfdata}".format(
        summary=message.get('summary'),
        perfdata=message.get('perfdata')
    ))

    # Exit with status code
    raise SystemExit(message['status'])

# Argument parser
# https://docs.python.org/3.5/library/argparse.html

def main():
    """
    Main function
    """
    # Get options with argparse
    options = parse_args(sys.argv[1:])
    # Execute program functions passing the options collected
    cli_execution(options)


if __name__ == "__main__":
    main()
