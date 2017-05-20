print "Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp). Return: The protein string encoded by s."

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

string = open('input.txt', 'r')
string = string.read()
messenger_rna = Seq(string, IUPAC.unambiguous_rna)

print messenger_rna.translate()
