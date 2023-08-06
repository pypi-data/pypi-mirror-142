#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os,glob,argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument('-i','--indir', metavar='FILE', type=str,default=os.getcwd())
args = parser.parse_args()
indir = args.indir
html_list = glob.glob('%s/*/04.report/*.html'%(indir))
result = os.path.join(indir,'result')
os.system('mkdir -p %s/result'%indir)
sample_list = []
metrics_list = []
for html in html_list:
    sample = html.split('/')[-1].split('_')[0]
    sample_list.append(sample)
    metrics_list.append('%s/%s/output/metrics_summary.xls'%(indir,sample))
    os.system('cp %s/%s/04.report/*.html %s/result'%(indir,sample,indir))
metrics = pd.read_table("%s"%metrics_list[0],sep="\t",index_col=0)
for i in range(1,len(metrics_list)):
    file_name = metrics_list[i]
    data = pd.read_table("%s"%file_name,sep="\t",index_col=0)
    metrics=pd.concat([metrics,data],axis=1)
metrics.to_csv("%s/result/metrics_summary.xls"%indir,sep='\t',index=0)