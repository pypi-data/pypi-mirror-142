import os
from .utils import rm_temp, str_mkdir,logging_call,judgeFilexits,change_path,python_path
from DNBC4tools.__init__ import _root_dir

class Data:
    def __init__(self, args):
        self.cDNAr1 = args.cDNAfastq1
        self.cDNAr2 = args.cDNAfastq2
        self.oligor1 = args.oligofastq1
        self.oligor2 = args.oligofastq2
        self.thread = args.thread
        self.name = args.name
        self.lowqual = args.lowqual
        self.cDNAconfig = args.cDNAconfig
        self.oligoconfig = args.oligoconfig
        self.outdir = os.path.join(args.outdir,args.name)
        self.starindex = args.starIndexDir
        self.gtf = args.gtf
        self.include_introns = args.include_introns
        self.no_bgifilter = args.no_bgifilter

    def run(self):
        judgeFilexits(self.cDNAr1,self.cDNAr2,self.oligor1,self.oligor2,self.cDNAconfig,self.oligoconfig,self.starindex,self.gtf)
        str_mkdir('%s/01.data'%self.outdir)
        str_mkdir('%s/log'%self.outdir)
        change_path()
        new_python = python_path()

        scRNA_parse_cmd = ['%s %s/tools/scRNA_parser.py --cDNAfastq1 %s --cDNAfastq2 %s --oligofastq1 %s --oligofastq2 %s --thread %s --name %s --cDNAconfig %s --oligoconfig %s --lowqual %s --outdir %s'
            %(new_python,_root_dir,self.cDNAr1,self.cDNAr2,self.oligor1,self.oligor2,self.thread,self.name,self.cDNAconfig,self.oligoconfig,self.lowqual,self.outdir)]
        if self.no_bgifilter:
            scRNA_parse_cmd += ['--no_bgifilter']
        star_cmd = '%s/soft/STAR --limitOutSJcollapsed 4000000 --outStd SAM --outSAMunmapped Within --runThreadN %s --genomeDir %s --readFilesIn %s/01.data/%s.cDNA_reads.fq --outFileNamePrefix  %s/01.data/ 1> %s/01.data/aln.sam'\
            %(_root_dir,self.thread,self.starindex,self.outdir,self.name,self.outdir,self.outdir)
        PISA_sam2bam_cmd = '%s/soft/PISA sam2bam -adjust-mapq -gtf %s -o %s/01.data/aln.bam -report %s/01.data/alignment_report.csv %s/01.data/aln.sam'\
            %(_root_dir,self.gtf,self.outdir,self.outdir,self.outdir)
        PISA_anno_cmd = ['%s/soft/PISA anno -gtf %s -o %s/01.data/anno.bam -report %s/01.data/anno_report.csv %s/01.data/aln.bam'
            %(_root_dir,self.gtf,self.outdir,self.outdir,self.outdir)]
        if self.include_introns:
            PISA_anno_cmd += ['-intron']
        PISA_corr_cmd = '%s/soft/PISA corr -tag UR -new-tag UB -tags-block CB,GN -@ %s -o %s/01.data/%s.final.bam %s/01.data/anno.bam'\
            %(_root_dir,self.thread,self.outdir,self.name,self.outdir)

        scRNA_parse_cmd = ' '.join(scRNA_parse_cmd)
        logging_call(scRNA_parse_cmd,'data',self.outdir)
        logging_call(star_cmd,'data',self.outdir)
        logging_call(PISA_sam2bam_cmd,'data',self.outdir)
        PISA_anno_cmd = ' '.join(PISA_anno_cmd)
        logging_call(PISA_anno_cmd,'data',self.outdir)
        logging_call(PISA_corr_cmd,'data',self.outdir)
        rm_temp('%s/01.data/aln.sam'%self.outdir,'%s/01.data/aln.bam'%self.outdir,
        '%s/01.data/anno.bam'%self.outdir)


def data(args):
    Data(args).run()

def parse_data(parser):
    parser.add_argument(
        '--name',
        help='sample name', 
        type=str
        )
    parser.add_argument(
        '--outdir',
        help='output dir, default is current directory', 
        default=os.getcwd()
        )
    parser.add_argument(
        '--cDNAfastq1',
        help='cDNAR1 fastq file, Multiple files are separated by comma.', 
        required=True
        )
    parser.add_argument(
        '--cDNAfastq2',
        help='cDNAR2 fastq file, Multiple files are separated by comma.', 
        required=True
        )
    parser.add_argument(
        '--cDNAconfig',
        help='whitelist file in JSON format for cDNA fastq,The value of cell barcode is an array in the JSON, \
        consist of one or more segments in one or both reads.',
        default='%s/config/DNBelabC4_scRNA_beads_readStructure.json'%_root_dir
        )
    parser.add_argument(
        '--oligofastq1',
        help='oligoR1 fastq file, Multiple files are separated by comma.',
        required=True
        )
    parser.add_argument(
        '--oligofastq2',
        help='oligoR2 fastq file, Multiple files are separated by comma.',
        required=True
        )
    parser.add_argument(
        '--oligoconfig',
        help='whitelist file in JSON format for oligo fastq',
        default='%s/config/DNBelabC4_scRNA_oligo_readStructure.json'%_root_dir
        )
    parser.add_argument(
        '--thread',
        type=int, 
        default=4,
        help='Analysis threads.'
        )
    parser.add_argument(
        '--starIndexDir',
        type=str, 
        help='star index dir'
        )
    parser.add_argument(
        '--gtf',
        type=str, 
        help='gtf file'
        )
    parser.add_argument(
        '--no_bgifilter',
        action='store_true',
        help='No process bgiseq filter.'
        )
    parser.add_argument(
        '--lowqual',
        help='Drop reads if average sequencing quality below this value.',
        type=int,
        default=4
        )
    parser.add_argument(
        '--include_introns', 
        action='store_true',
        help='Include intronic reads in count.'
        )
    return parser
