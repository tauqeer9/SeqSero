#!/usr/bin/env python

############################################################################
# Copyright (c) 2014-2015 University of Georgia
# All Rights Reserved
############################################################################

import argparse,os,sys,time,random

def check_deps(*tools):
  for exe in tools:
    print "Checking if '"+exe+"' is installed...",
    ec = os.system("which "+exe+" 1>/dev/null 2>/dev/null")
    if ec == 0:
      print "OK"
    else:
      print "COULD NOT FIND - PLEASE INSTALL"
      exit(2);

def main():
  parser = argparse.ArgumentParser(usage='SeqSero.py -m <data_type> -i <input_data> [-d outdir] [-b <BWA_algorithm>]\n\nDevelopers: Shaokang Zhang (zskzsk@uga.edu) and Xiangyu Deng (xdeng@uga.edu)\n\nContact: seqsero@gmail.com')
  parser.add_argument('-V', action='version', version='%(prog)s 1.0.1')
  parser.add_argument("-m", choices=['1','2','3', '4'],help="<int>: '1'(pair-end reads, interleaved),'2'(pair-end reads, seperated),'3'(single-end reads), '4'(assembly)")
  parser.add_argument("-i", nargs="+", help="<string>: path/to/input_data")
  parser.add_argument("-b",choices=['sam','mem','nanopore'],default="sam",help="<string>: 'sam'(bwa samse/sampe), 'mem'(bwa mem), default=sam")
  parser.add_argument("-d",help="<string>: output directory name, if not set, the output directory would be 'SeqSero_result_'+time stamp+one random number")
  args=parser.parse_args()
  dirpath = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
  if len(sys.argv)==1:
    os.system(dirpath+"/SeqSero.py -h")
  else:
    check_deps('bwa', 'samtools', 'isPcr', 'blastn', 'makeblastdb', 'fastq-dump')
    request_id = time.strftime("%m_%d_%Y_%H_%M_%S", time.localtime())
    request_id += str(random.randint(1, 10000000))
    make_dir=args.d
    if make_dir is None:
      make_dir="SeqSero_result_"+request_id
    os.system("mkdir -p "+make_dir)
    os.system("cp -rf "+dirpath+"/database "+make_dir)
    mode_choice=args.m
    mapping_mode=args.b
    dataset=args.i
    if mode_choice=="1":
      print dataset[0]
      os.system("cp "+dataset[0]+" "+make_dir)
      os.chdir(make_dir)
      os.system("python2.7 "+dirpath+"/libs/run_auto_All_for_web_multi_revise.py "+dataset[0].split("/")[-1]+" "+mapping_mode+" 1")
      print "\n\n\nResult:\n"
      os.system("cat Seqsero_result.txt")
      os.system("rm "+dataset[0].split("/")[-1])
    elif mode_choice=="2":
      os.system("cp "+dataset[0]+" "+make_dir)
      os.system("cp "+dataset[1]+" "+make_dir)
      fnameA=dataset[0].split("/")[-1]
      fnameB=dataset[1].split("/")[-1]
      os.chdir(make_dir)
      print "check fastq id and make them in accordance with each other...please wait..."
      os.system("python2.7 "+dirpath+"/libs/run_auto_All_for_web_multi_revise.py "+fnameA+" "+mapping_mode+" "+fnameB+" 2")
      print "\n\n\nResult:\n"
      os.system("cat Seqsero_result.txt")
    elif mode_choice=="3":
      os.system("cp "+dataset[0]+" "+make_dir)
      os.chdir(make_dir)
      os.system("python2.7 "+dirpath+"/libs/run_auto_All_for_web_multi_revise.py "+dataset[0].split("/")[-1]+" "+mapping_mode+" 3")
      print "\n\n\nResult:\n"
      os.system("cat Seqsero_result.txt")
    elif mode_choice=="4":
      os.system("cp "+dataset[0]+" "+make_dir)
      os.chdir(make_dir)
      os.system("python2.7 "+dirpath+"/libs/run_auto_All_for_assemblies.py "+dataset[0].split("/")[-1])
      print "\n\n\nResult:\n"
      os.system("cat Seqsero_result.txt")

if __name__ == '__main__':
  main()
