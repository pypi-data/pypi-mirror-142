import os,sys
import time
import logging
import sys
from datetime import timedelta
from subprocess import check_call

def str_mkdir(arg):
    if not os.path.exists(arg):
        os.system('mkdir -p %s'%arg)

def change_ld_path():
    python_path = os.environ.get("_")
    os.environ['LD_LIBRARY_PATH'] = '/'.join(str(python_path).split('/')[0:-2]) + '/lib'

def rm_temp(*args):
    for i in args:
        os.remove(i)

def start_print_cmd(arg):
    print(arg)
    check_call(arg,shell=True)

def logging_call(popenargs,name,dir):
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    logfile = '%s/log/%s.%s.txt'%(dir,name,today)
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level = logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter
        file_handler = logging.FileHandler(logfile,encoding="utf8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    logger.info('Promgram start...')
    logger.info(popenargs)
    start = time.time()
    check_call(popenargs,shell=True)
    logger.info('Promgram end...')
    end = time.time()
    used = timedelta(seconds=end - start)
    logger.info('Program time used: %s', used)
    logger.info('\n')   

def judgeFilexits(*args):
    for input_files in args:
        for input_file in input_files.split(','):
            if not os.path.exists(input_file): 
                print(" ------------------------------------------------") 
                print("Error: Cannot find input file or dir %s."%(str(input_file))) 
                print(" ------------------------------------------------") 
                sys.exit()
            else:
                pass