import argparse,os
from multiprocessing import Pool
import subprocess
from DNBC4tools.__init__ import _root_dir

parser = argparse.ArgumentParser(description='sequencing saturation')
parser.add_argument('--name',help='sample name', type=str)
parser.add_argument('--outdir',help='output dir, default is current directory', default=os.getcwd())
parser.add_argument('--cDNAfastq1',help='cDNAR1 fastq file, Multiple files are separated by comma.', required=True)
parser.add_argument('--cDNAfastq2',help='cDNAR2 fastq file, Multiple files are separated by comma.', required=True)
parser.add_argument('--cDNAconfig',
    help='whitelist file in JSON format for cDNA fastq,The value of cell barcode is an array in the JSON, \
    consist of one or more segments in one or both reads.',
    default='%s/config/DNBelabC4_scRNA_beads_readStructure.json'%_root_dir)
parser.add_argument('--oligofastq1',help='oligoR1 fastq file, Multiple files are separated by comma.',required=True)
parser.add_argument('--oligofastq2',help='oligoR2 fastq file, Multiple files are separated by comma.',required=True)
parser.add_argument('--oligoconfig',
    help='whitelist file in JSON format for oligo fastq',
    default='%s/config/DNBelabC4_scRNA_oligo_readStructure.json'%_root_dir)
parser.add_argument('--thread',type=int, default=4,help='Analysis threads.')
parser.add_argument('--no_bgifilter',action='store_true',help='No process bgiseq filter.')
parser.add_argument('--lowqual',
    help='Drop reads if average sequencing quality below this value.',type=int,default=4)
args = parser.parse_args()


def scRNA_parse_cDNA(): 
    scRNA_parse_cmd = ['%s/soft/scRNA_parse'%_root_dir,'-t', str(args.thread),'-q', str(args.lowqual)]
    if  not args.no_bgifilter:
        scRNA_parse_cmd += ['-f','-dropN']
    scRNA_parse_cDNA_cmd = scRNA_parse_cmd + [
        '-config',args.cDNAconfig,
        '-cbdis','%s/01.data/%s.cDNA_barcode_counts_raw.txt'%(args.outdir,args.name),
        '-1','%s/01.data/%s.cDNA_reads.fq'%(args.outdir,args.name),
        '-report','%s/01.data/cDNA_sequencing_report.csv'%args.outdir,
        args.cDNAfastq1,args.cDNAfastq2
        ]
    scRNA_parse_cDNA_cmd = ' '.join(scRNA_parse_cDNA_cmd)
    return scRNA_parse_cDNA_cmd

    
def scRNA_parse_oligo():
    scRNA_parse_cmd = ['%s/soft/scRNA_parse'%_root_dir,'-t', str(args.thread),'-q', str(args.lowqual)]
    if  not args.no_bgifilter:
        scRNA_parse_cmd += ['-f','-dropN']
    scRNA_parse_oligo_cmd = scRNA_parse_cmd + [
        '-config',args.oligoconfig,
        '-cbdis','%s/01.data/%s.Index_barcode_counts_raw.txt'%(args.outdir,args.name),
        '-1','%s/01.data/%s.Index_reads.fq'%(args.outdir,args.name),
        '-report','%s/01.data/Index_sequencing_report.csv'%args.outdir,
        args.oligofastq1,args.oligofastq2
        ]
    scRNA_parse_oligo_cmd = ' '.join(scRNA_parse_oligo_cmd)
    return scRNA_parse_oligo_cmd

def subrun(i):
    subprocess.run(i,shell=True,check=True)

if __name__ == '__main__':
    scRNA_parse_cDNA_cmd = scRNA_parse_cDNA()
    scRNA_parse_oligo_cmd = scRNA_parse_oligo()
    mission = [scRNA_parse_cDNA_cmd,scRNA_parse_oligo_cmd]
    pool = Pool(2)
    for i in mission:
        pool.apply_async(subrun,(i,))
    pool.close()
    pool.join()


