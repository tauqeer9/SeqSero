# SeqSero

Salmonella serotyping from genome sequencing data

# Introduction

SeqSero is a pipeline for Salmonella serotype determination from raw
sequencing reads or genome assemblies.  A web app is available at
http://www.denglab.info/SeqSero

# Dependencies

1. [Python 2.7](https://www.python.org/download/releases/2.7/)
2. [Biopython 1.65](http://biopython.org/wiki/Download)
2. [BWA](https://github.com/lh3/bwa)
3. [SAMtools](https://github.com/samtools/samtools)
4. [BLAST+](ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
5. [SRA Toolkit](http://ncbi.github.io/sra-tools/)
6. [isPcr](http://hgwdev.cse.ucsc.edu/~kent/exe/linux/)

# Executing the code

```
usage: SeqSero.py -m <data_type> -i <input_data> [-b <BWA_algorithm>]

  -m {1,2,3,4}          <int>: '1'(pair-end reads, interleaved),'2'(pair-end
                        reads, seperated),'3'(single-end reads), '4'(assembly)
  -i I [I ...]          <string>: path/to/input_data
  -b {sam,mem,nanopore}
                        <string>: 'sam'(bwa samse/sampe), 'mem'(bwa mem),
                        default=sam
  -d D                  <string>: output directory name, if not set, the
                        output directory would be 'SeqSero_result_'+time
                        stamp+one random number
```

# Output

Upon executing the command, a directory named
`SeqSero_result_<time_you_run_SeqSero>`
(or the name you specified via `-d` option) will be created.
Your result will be stored in `Seqsero_result.txt` in that directory

# Licence

[GNU General Public Licence 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

# Citation

Zhang S, Yin Y, Jones MB, Zhang Z, Deatherage Kaiser BL, Dinsmore BA,
Fitzgerald C, Fields PI, Deng X.
_Salmonella serotype determination utilizing high-throughput genome sequencing data_
**J Clin Micro.** 2015 May;53(5):1685-92.
[PMID:25762776](http://jcm.asm.org/content/early/2015/03/05/JCM.00323-15)

