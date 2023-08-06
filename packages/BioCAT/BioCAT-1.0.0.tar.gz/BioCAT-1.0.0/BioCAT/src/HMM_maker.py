import argparse
import os
import logging
from pandas import read_csv
from subprocess import call
from os import listdir, mkdir

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

def HMM_make(path, output, cpu):
    """
    Firatly, function generate fasta file with all possible sequences of AMP-binding domain
    and alighn its on hmm profile.

    Parameters
    ----------
    path : str
        Path to HMM profiles
    output : str
        Path to output directory for Hmmer output
    cpu : int
        Number of threads used.
    """

    hmms = os.path.dirname(os.path.abspath(__file__)) + '/../HMM/Bacteria_HMM'

    table = read_csv(path + '/table.tsv', sep='\t')
    #making work directory to fasta files
    substrates = []
        
    hmm_out = '{}/HMM_results/'.format(output)
    try:
        
        mkdir('{}'.format(hmm_out))
        
    except:
        
        a_logger.debug('Exist!')
        
    a_logger.debug('Generation of fasta files ...')
    headers = []
    with open('{}/nrps_domains.fasta'.format(path), 'w') as fasta:
        for ind in table[table['Domain name'].str.contains('AMP-binding')].index:
            
            ID = table['ID'][ind]
            DOMAIN = table['Domain name'][ind]
            TRANSLATE = table['Sequence'][ind]        

            if '>{}'.format(DOMAIN) in headers:
                continue

            fasta.write('>{}\n{}\n'.format(DOMAIN, 
                                           TRANSLATE))

            headers.append('>{}'.format(DOMAIN))

    a_logger.debug('fasta files have been generated successfully!')
    a_logger.debug("Calculating sequences' specificity using HMMs ...")
    hmms_s = listdir(hmms)

    for sub in hmms_s:
        
        substrate = sub.split('_')[1][: -4]
        # Call hmmsearch
        call('hmmsearch -Z 1000 --cpu {} {}/{} {}/nrps_domains.fasta > {}/{}.out'.format(cpu,
                                                                                        hmms,
                                                                                        sub,
                                                                                        path, 
                                                                                        hmm_out, 
                                                                                        substrate), shell=True)

    a_logger.debug('The search has been done successfully!')
