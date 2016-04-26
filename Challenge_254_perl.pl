#!\usr\bin\perl

#### PERL SOLUTION ####
use strict;
use warnings;

my $output="";
my $input = 'gsrh rh zm vcznkov lu gsv zgyzhs xrksvi';

my @straight = ("a".."z");
my @reverse = reverse(@straight);
my @CAPstraight = ("A".."Z");
my @CAPreverse = reverse(@CAPstraight);

for (my $i= 0; $i<length($input); $i++) {
    my $complete = 0;
    my $char = substr($input,$i,1);
    for (my $k =0; $k<scalar(@straight); $k++) {  
        if ($straight[$k] eq $char) {
            $output .= $reverse[$k];            
            $complete = 1;
            last;
        } 
        elsif ($CAPstraight[$k] eq $char) {
            $output .= $CAPreverse[$k];            
            $complete = 1;
            last;
        }
    }
    if ($complete == 0) {
        $output .=$char;
    }   
}

print "\n$output\n";

__DATA__
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: ZYXWVUTSRQPONMLKJIHGFEDCBA

INPUT:
foobar
wizard
/r/dailyprogrammer
gsrh rh zm vcznkov lu gsv zgyzhs xrksvi

OUTPUT:
ullyzi
draziw
/i/wzrobkiltiznnvi
this is an example of the atbash cipher

BONUS:
Preserve case.
