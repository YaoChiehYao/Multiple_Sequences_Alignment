#!/usr/bin/env bash

# input the apoe_aa.fasta file (in fasta format)
# output the alignment to apoe_alignment.fasta (in fasta format)
# otherwise use default settings/parameters

clustalo -i apoe_aa.fasta -o apoe_alignment.fasta -v


