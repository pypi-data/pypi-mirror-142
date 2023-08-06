import sys
import os
import time
from colored import fg
from helpers.organize import organize_junk
from helpers.ip_scan import scan_network
from helpers.port_scan import check_port
from helpers.find_cameras import find_cameras
from helpers.password_gen import gen_password
import multiprocessing as mp
import time
import socket


blue = fg("blue")
cyan = fg("cyan")


def main():
  arg1 = sys.argv[1]
#================================ORGANISE======================================
  if arg1 == "organise":
    option = sys.argv[2]
    if option != '':
      organize_junk()
    else:
      print("Please type `wize organise all`")
#=================================SCAN========================================     
  elif arg1 == "scan network":
    scan_network()
 #==============================================================================   
  elif arg1 == "scan":
    
    start = time.time()
    processes = []
    scan_range = range(80, 100)
    host = sys.argv[2]
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(len(scan_range)) as pool:
        outputs = pool_manager.Queue()
        for port in scan_range:
            processes.append(pool.apply_async(check_port, (host, port, outputs)))
        for process in processes:
            process.get()
        while not outputs.empty():
            print("Port {0} is open".format(outputs.get()))
        print("Completed scan in {0} seconds".format(time.time() - start))    
    scan_network()
#==============================================================================
  elif arg1 == "locate cameras":
    find_cameras()

  elif arg1 == "generate password":
    gen_password()()
    
  else:
    print(blue + "Invalid Argument")