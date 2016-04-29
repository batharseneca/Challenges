use strict;
use warnings;
my $count = 1;
while (my $line = <DATA>) {
    my @output = my @words;
    my $row = my $col=0;    
    my $direction = "RIGHT";    
    while ($line =~ /(\w*)/g) {
        if ($1){
            if (@words) {
                my $holder = $1;
                $holder = substr($holder, 1, length($holder)-1);
                push @words, $holder;
            } else {
                push @words, $1;
            }
        }
    }    
    foreach my$word (@words) {
        if ($direction eq "RIGHT") {
            for (my $i=0; $i<length($word); $i++) {
                $output[$row][$col++] = substr($word, $i, 1);              
            }
            $direction = "DOWN";
            $row++;
            $col--;
        } else {
            for (my $i=0; $i<length($word); $i++) {
                for (my $g=$col-1; $g>-1; $g--) {
                    $output[$row][$g] = ".";
                }
                $output[$row++][$col] = substr($word, $i, 1);             
            }
            $direction = "RIGHT";
            $col++;
            $row--;
        }
    }  
    print "\n GRAPH => #" . $count++ . "\n\n";
    foreach (@output) {
        print @{$_}, "\n";
    }
    print "\n" . "-------------------------------"x5 ."\n" . "-------------------------------" x5 . "\n";    
    @output = ();
}
__DATA__
SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE 
ESSENCE EAR RUMP PALINDROME EXEMPLARY YARD DIRK KOMBAT TEMP PLUNGE ESTER REGRET TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS