#!/usr/bin/env python3
# translate_APOE.py
"""_summary_
This program takes two arguments, an input FASTA file,
converts the NCBI transcript sequence to an amino acid, and
gives an output file name to save as another FASTA file. 
"""
import re
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

if __name__ == "__main__":
    """Main Business Logic"""
    try:
        with open(sys.argv[1]) as infile:
            new_record = []
            for record in SeqIO.parse(infile, "fasta"):
                new_record.append(SeqRecord(
                    Seq(re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)',
                        str(record.seq.transcribe())).group()).translate(stop_symbol=''),
                    record.id,
                    record.name,
                    record.description))
    except IndexError:
        print("please provide FASTA filename, ex. APOE_refseq_transcript.fasta")
        sys.exit()
    except FileNotFoundError:
        print("please check if the input file is in the same folder")
        sys.exit()

    try:
        SeqIO.write(new_record, sys.argv[2], "fasta")
    except IndexError as err:
        print("please provide an output filename, ex. apoe_aa.fasta")
        sys.exit()
