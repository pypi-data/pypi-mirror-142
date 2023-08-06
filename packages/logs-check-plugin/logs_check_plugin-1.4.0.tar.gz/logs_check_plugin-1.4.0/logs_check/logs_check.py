#
# documentation:
# https://www.geeksforgeeks.org/python-reading-last-n-lines-of-a-file/

import requests
import json
import os

# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

class Logs:
    def __init__(self, filelocation, word_to_check, lines_n=20):
        
        #initial
        self.filelocation = filelocation
        self.word_to_check = word_to_check
        self.lines_n = lines_n
    
    def check_logs(self):

        #variables
        retrcode = OK
        lines = []
        fetched_tail_lines = []
        count = 0
        N = self.lines_n
        # buffer size
        bufsize = 8192

        # calculating size of file in bytes
        fsize = os.stat(self.filelocation).st_size
    
        iter = 0

        with open(self.filelocation) as f:

            if bufsize > fsize:                                   
                # adjusting buffer size according to size of file
                bufsize = fsize-1
                # list to store last N lines
                fetched_lines = []
                

                while True:
                    iter += 1
                    
                    # moving cursor to  the last Nth line of file
                    f.seek(fsize-bufsize * iter)
                
                    # storing each line in list upto end of file
                    fetched_lines.extend(f.readlines())                                       
                    
                    # halting the program when size of list is equal or greater to the number of lines requested or when we reach end of file
                    if len(fetched_lines) >= N or f.tell() == 0:
                        fetched_tail_lines = fetched_lines[-N:]
                        break

        for x in fetched_tail_lines:
            if self.word_to_check not in x:
                pass
            else:                
                lines.append(x)
                retrcode = CRITICAL
                count += 1

        return retrcode, count, lines
