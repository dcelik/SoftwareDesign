# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Deniz Celik

Skeleton provided by Paul Ruvolo
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
from load import *

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    dnainp = dna
    protein = ''
    if len(dnainp)<3:
        return "ERROR: The provided fragment is too short to contain any codons."
#    elif len(dnainp)%3 is not 0:
#        print "Warning: The provided DNA fragment does not contain an integer number of codons. Excess bases were leftout."
    while len(dnainp) >=3:
        cod = dnainp[:3]
        for i in codons:
            for j in i:
                if j == cod:
                    protein = protein + aa[codons.index(i)]
        dnainp = dnainp[3:]
    return protein
    
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    print "input: GTTGACAGTACGTACAGGGAA, "+"output: "+coding_strand_to_AA("GTTGACAGTACGTACAGGGAA")+", actual output: VDSTYRE"
    print "input: TTATTGCTTATTATCATG, "+"output: "+coding_strand_to_AA("TTATTGCTTATTATCATG")+", actual output: LLLIIM"
    print "input: TTTTTAATTATGGTTTCTCCTACTGCTTATTAACATCAAAATAAAGATGAATGTTGGCGTGGT, "+"output: "+coding_strand_to_AA("TTTTTAATTATGGTTTCTCCTACTGCTTATTAACATCAAAATAAAGATGAATGTTGGCGTGGT")+", actual output: FLIMVSPTAY|HQNKDECWRG"
    print "input: TT, " + "output: "+coding_strand_to_AA("TT")+", actual output: ERROR: The provided fragment is too short to contain any codons."

print "input: GTTGACAGTACGTACAGGGAA, "+"output: "+coding_strand_to_AA("GTTGACAGTACGTACAGGGAA")+", actual output: VDSTYRE"

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    dna = dna.replace('T','N')
    dna = dna.replace('A','T')
    dna = dna.replace('N','A')
    dna = dna.replace('C','N')
    dna = dna.replace('G','C')
    dna = dna.replace('N','G')
    dna = dna[::-1]
    return dna
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    print "input: GTTGACAGTACGTACAGGGAA, "+"output: "+ get_reverse_complement("GTTGACAGTACGTACAGGGAA") +", actual output: AAGGGACATGCATGACAGTTG"  
    print "input: TTATTGCTTATTATCATG, "+"output: "+get_reverse_complement("TTATTGCTTATTATCATG")+", actual output: GTACTATTATTCGTTATT"
    print "input: ATC, "+"output: "+get_reverse_complement("ATC")+", actual output: GAT"
    print "input: CTA, "+"output: "+get_reverse_complement("CTA")+", actual output: TAG"

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    if len(dna)<3:
        return dna
    if dna[:3]== "TAG" or dna[:3]=="TAA" or dna[:3]=="TGA" or len(dna)<3:
        return ""
    return dna[:3]+rest_of_ORF(dna[3:])

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    print "input: CTA, "+"output: "+rest_of_ORF("CTA")+", actual output: CTA"
    print "input: GTCACTTAGGGTTTT, "+"output: "+rest_of_ORF("GTCACTTAGGGTTTT")+", actual output: GTCACT"
    print "input: AAATTTTATAATGGGTGAAGTTAG, "+"output: "+rest_of_ORF("AAATTTTATAATGGGTGAAGTTAG")+", actual output: AAATTTTATAATGGG"
    print "input: TATATGGAGGATAATAGTTGATAATAG, "+"output: "+rest_of_ORF("TATATGGAGGATAATAGTTGATAATAG")+", actual output: TATATGGAGGATAATAGT"

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dnainp = dna
    orfs = []
    if len(dnainp)<3:
        orfs.append(dna)
    while len(dnainp)>=3:
        orfs.append(rest_of_ORF(dnainp))
        minuslen = len(rest_of_ORF(dnainp))+3
        dnainp = dnainp[minuslen:]
    y = [s for s in orfs if s!='']
    return y
    
        
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ans = find_all_ORFs_oneframe(dna)
    ans.extend(find_all_ORFs_oneframe(dna[1:]))
    ans.extend(find_all_ORFs_oneframe(dna[2:]))
    return ans
    
    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print "input: CTA, "+"output: "+ ",".join(find_all_ORFs("CTA"))+", actual output: CTA,TA,A"
    print "input: GTCACTTAGGGTTTT, "+"output: "+",".join(find_all_ORFs("GTCACTTAGGGTTTT"))+", actual output: GTCACT,GGTTTT,TCACTTAGGGTTTT,CACTTAGGGTTTT"
    print "input: AAATTTTATAATGGGTGAAGTTAG, "+"output: "+",".join(find_all_ORFs("AAATTTTATAATGGGTGAAGTTAG"))+", actual output: AAATTTTATAATGGG,AGT,AATTTTATAATGGGTGAAGTTAG,ATTTTA,TGGGTGAAGTTAG"
    print "input: TATATGGAGGATAATAGTTGATAATAG, "+"output: "+ ",".join(find_all_ORFs("TATATGGAGGATAATAGTTGATAATAG"))+", actual output: TATATGGAGGATAATAGT,ATATGGAGGATAATAGTTGATAATAG,TATGGAGGA,TTGATAATAG" 

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs(dna) + (find_all_ORFs(get_reverse_complement(dna)))
     
     
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    print "input: CTA, "+"output: "+ ",".join(find_all_ORFs_both_strands("CTA"))+", actual output: CTA,TA,A,AG,G"
    print "input: GTCACTTAGGGTTTT, "+"output: "+",".join(find_all_ORFs_both_strands("GTCACTTAGGGTTTT"))+", actual output: GTCACT,GGTTTT,TCACTTAGGGTTTT,CACTTAGGGTTTT,AAAACCCTAAGTGAC,AAACCC,GTGAC,AACCCTAAG"
    print "input: AAATTTTATAATGGGTGAAGTTAG, "+"output: "+",".join(find_all_ORFs_both_strands("AAATTTTATAATGGGTGAAGTTAG"))+", actual output: AAATTTTATAATGGG,AGT,AATTTTATAATGGGTGAAGTTAG,ATTTTA,TGGGTGAAGTTAG,CTAACTTCACCCATTATAAAATTT,CTTCACCCATTA,AATTT,AACTTCACCCATTATAAAATTT"
    print "input: TATATGGAGGATAATAGTTGATAATAG, "+"output: "+ ",".join(find_all_ORFs_both_strands("TATATGGAGGATAATAGTTGATAATAG"))+", actual output: TATATGGAGGATAATAGT,ATATGGAGGATAATAGTTGATAATAG,TATGGAGGA,TTGATAATAG,CTATTATCAACTATTATCCTCCATATA,TATTATCAACTATTATCCTCCATATA,ATTATCAACTATTATCCTCCATATA" 


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    orfs = find_all_ORFs_both_strands(dna)
    maxorf =orfs[1];
    for s in orfs:
        if len(s)>len(maxorf):
            maxorf=s
    return maxorf

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    dnal = list(dna)
    maxorf = 0
    for i in range(num_trials):
        shuffle(dnal)
        orf = len(longest_ORF(collapse(dnal)))
        if maxorf<orf:
            maxorf = orf
    return maxorf   

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    orfs = find_all_ORFs_both_strands(dna)
    orfs = [i for i in orfs if len(i)>threshold]
    orfs = [coding_strand_to_AA(i) for i in orfs]
    return orfs
    
sampledna = load_seq("./data/X73525.fa")
samplethresh = longest_ORF_noncoding(sampledna,1500)
print samplethresh
print gene_finder(sampledna, samplethresh)