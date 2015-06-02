#!/usr/bin/perl
use strict;
use warnings;

#needs command line pdftotext and pdfinfo (part of xpdf/poppler-utils) 
#extracts text from PDFs in current directory and writes to text files
#works on all PDFs in the directory unless filename(s) specified

my @pdfs = @ARGV; 
unless (scalar @pdfs) {
    opendir (DIR, "./") or die "Cannot open directory: $!";
    @pdfs = readdir(DIR);
    closedir(DIR);
    @pdfs = sort @pdfs;
}
@pdfs = grep (/\.pdf$/, @pdfs);

foreach my $file (@pdfs) {
    my @extracted;

    #find page count
    my $pagecount;
    my $cmd = "pdfinfo $file";    
    my @pdfinfo = `$cmd`;    
    chomp @pdfinfo;
    my @pagelines = grep (/^Pages:/, @pdfinfo);
    my $pageline = shift @pagelines;
    $pageline =~ /^Pages:\s*(\d*)/ or die "Didn't find page count! $!\n";
    $pagecount = $1;

    #cover page column 1
    push (@extracted, &getcolumn($file,1,54,351,162,432));
    #cover page column 2
    push (@extracted, &getcolumn($file,1,225,351,162,432));
    #cover page column 3
    push (@extracted, &getcolumn($file,1,396,351,162,432));
    
    #page 2 to end
    for (my $page = 2; $page <= $pagecount; $page++) {
	#column 1
	push (@extracted, &getcolumn($file,$page,54,63,162,720));
	#column 2
	push (@extracted, &getcolumn($file,$page,225,63,162,720));
	#column 3
	push (@extracted, &getcolumn($file,$page,396,63,162,720));
    }#page 2 to end

    #output extracted lines to file
    (my $outfile = $file) =~ s/\.pdf/\.txt/;
    open (OUT, "> $outfile") or die "$!\n";
    foreach (@extracted) {print OUT;}
    close (OUT);

}#pdf extraction


sub getcolumn {
    my $file = shift;
    my $page = shift;
    my $x = shift;
    my $y = shift;
    my $width = shift;
    my $height = shift;

    unlink("tempfile");
    system ("pdftotext",
	    "-enc", "UTF-8",
	    "-f", "$page", "-l", "$page",
	    "-x", "$x", "-y", "$y",
	    "-W", "$width", "-H", "$height",
	    "-nopgbrk",
	    "$file", "tempfile");
    open (TMP, "tempfile") or die "$!\n";
    my @tmp = <TMP>;
    close (TMP);
    return @tmp;
}



    






