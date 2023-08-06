#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os,argparse
import collections
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser(description='summary barcode and cell merge')
parser.add_argument('-i','--indir', type=str, help='set the indir for analysis')
parser.add_argument('-n','--name',type=str, help='sample name')
args = parser.parse_args()
indir = args.indir
name = args.name

multi_barcodelist = []
multi_celllist = []
multibeads_filter_dict = {}
one_barcodedict = collections.OrderedDict()

with open(os.path.join(indir,'%s_combined_list.txt'%name),'r') as multi_beads:
    for line in multi_beads:
        line = line.strip()
        if line:
            multi_barcodelist.append(line.split('\t')[0])
            multi_celllist.append(line.split('\t')[-1])
            if int(line.split('\t')[-1].split('_N')[-1]) <= 9:
                multibeads_filter_dict.setdefault(line.split('\t')[-1],[]).append(line.split('\t')[0])

num = int(multi_celllist[-1].split('CELL')[-1].split('_')[0])
with open(os.path.join(indir,'beads_barcodes.txt'),'r') as allbarcode:
    for line in allbarcode:
        line = line.strip()
        if line not in multi_barcodelist:
            num += 1
            cellName = 'CELL'+str(num)+'_N1'
            one_barcodedict[line] = cellName

with open(os.path.join(indir,'%s_barcodeTranslate.txt'%name),'w') as barcode_cell:
    for k2,v2 in one_barcodedict.items():
        barcode_cell.write(f'{k2}\t{v2}'+'\n')
    for k1,v1 in multibeads_filter_dict.items():
        for v1terms in v1:
            barcode_cell.write(f'{v1terms}\t{k1}'+'\n')

raw_beads_stat = pd.read_table(os.path.join(indir,'beads_stat.txt'),sep = '\t')
barcodeTranslate = pd.read_table(os.path.join(indir,'%s_barcodeTranslate.txt'%name),sep = '\t',header=None)
barcodeTranslate.columns = ['BARCODE', 'CELL']
beads_stat = pd.merge(raw_beads_stat,barcodeTranslate,how = 'inner',on='BARCODE')
beads_stat = beads_stat.drop(['BARCODE','GN'], axis=1)
beads_stat = beads_stat.groupby("CELL").agg('sum')
beads_stat.to_csv(os.path.join(indir,'merge_cell.stat'),sep='\t')

barcodeTranslate['frequence'] = barcodeTranslate['CELL'].str.split('_N',expand=True)[1]
figtable = barcodeTranslate.frequence.value_counts()
figtable = figtable.reset_index(level=None, drop=False, name=None, inplace=False)
figtable['index'] = figtable['index'].astype(int)
figtable['Count'] = figtable.apply(lambda x: round(x['frequence']/x['index']), axis=1)
figtable.columns = ['Num', 'frequence','Count']
figtable['Num'] = figtable['Num'].astype(str)
cellnum = figtable['Count'].sum()
figtable['num_count'] = figtable["Num"].map(str) +'  '+figtable["Count"].map(str)

from plotnine import *

p = ggplot(figtable,aes(x='Num',y='Count',fill ='Num'))+ \
    geom_bar(stat='identity') + \
    scale_fill_brewer(type="qual", palette="Set2",labels =figtable['num_count']) + \
    xlab('Number of beads per droplet') + \
    ylab('CellCount') + \
    ggtitle('Total cell number: %s'%cellnum) + \
    theme(panel_background=element_rect(fill='white'),
        axis_line_x=element_line(color='black'),
        axis_line_y=element_line(color='black'),
        axis_text_x=element_text(color='black'),
        panel_border=element_blank(),
        legend_position=(0.8,0.7),
        figure_size=(4.58, 3.77),
        plot_title=element_text(ha='right')
        )

p.save(filename = '%s/cellNumber_merge.png'%indir)
p.save(filename = '%s/cellNumber_merge.pdf'%indir)
