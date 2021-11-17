#!/usr/bin/perl
#itol2sql takes itol formatted text file for domains and puts into vizphiz mysql database
#
#usage:
#tab2sql.pl <itol file>

use strict;
use DBI;
my $accession;
my $isoform;

open INFILE, "<$ARGV[0]" or die $!;
while (<INFILE>) {

	print "$_";

}
