#!/usr/bin/perl
use strict;
use warnings;

#needs command line pdftotext (part of xpdf/poppler-utils) 
#extracts text from files in ./pdf directory and writes to ./text directory

my $pdfdir = './pdf/';
my $textdir = './text/';



opendir (DIR, $pdfdir) or die $!;
my @pdfs = readdir(DIR);
closedir(DIR);
@pdfs = sort @pdfs;
@pdfs = grep (/\.pdf/, @pdfs);


foreach (@pdfs) {
    



}#pdfs





