"""Test utils."""
from os.path import join, dirname, abspath

ROOT = abspath(dirname(__file__))

DATA = join(ROOT, "data")

TEST = {
    "reference": join(DATA, "reference", "reference.fasta"),
    "bedfile": join(DATA, "bed", "test.bed.gz"),
    "normal": join(DATA, "normal", "normal.bam"),
    "tumor": join(DATA, "tumor", "tumor.bam"),
}
