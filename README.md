##  BINF 6309 Assignment 6 Multiple Sequence Alignment 
Author: Yao Chieh Yao


## Description
In assignment 6, we first used python3 and BioPython to translate 
NCBI data to amino acid sequences. Then, running Clustal Omega for  
multiple sequences alignment.


## Getting Started
* Hi, this is the documentation for assignment six of the bio-computational
  method course, BINF6309.

* Please go to NCBI protein search, and download all the APOE orthologs in 
  a nucleotide FASTA format.

* Write a python program to translate the nucleotide of each species to amino
  acids by the longest open reading frame. Please use the Biopython version 
  above 1.78 

* Then, we used the output amino acid FASTA for the Clustalo Omega program to
  do multiple sequences alignment, and generate an alignment file. 
 
Here is the link for all the assignment files: 
```
https://github.com/NU-Bioinformatics/module06-YaoChiehYao.git
```


## Method 
Clustal Omega is a fast and widely-used MSA. (Chowdhury et al.,2017) It can access 
via various interfaces such as the command line, python, or the web. (Similar to DAVID) 
For this assignment, our instructor has installed Clustalo software on the server, but 
please feel free to combine this method with the analysis tool you are using or find 
out more options by the help function.


## References
Chowdhury, Biswanath, and Gautam Garai. 2017. “A Review on Multiple Sequence Alignment
from the Perspective of Genetic Algorithm.” *Genomics* 109 (5): 419–31..
