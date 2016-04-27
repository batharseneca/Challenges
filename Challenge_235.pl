###### perl solution

use strict;
use warnings;
my $fileName = "235_input.txt";

my $count =1;

open my $input, $fileName or die "Could not open $fileName: $!";    
while (my $line = <$input>) {   
    chomp ($line);
    my @innerCheck_f = ();
    my @innerCheck_s = ();
    my @valid_f = ();
    my @valid_s = ();
    
    if ($line =~/^(\d)/) {
        my $inputNum = $1;
        next;
    }
    $line =~ /^\((\d*),(\d*)\)/;
    my $firstnum = $1;
    my $secondnum = $2;
    
    for (my $i=2; $i<$firstnum+1; $i++) {
        my $check = $firstnum % $i; 
        if ($check == 0) {
            for (my $x=$i-1; $x>1; $x--) {
                my $innercheck = $i % $x;
                if ($innercheck == 0) {
                    push @innerCheck_f, $x;
                    last;                    
                }
            }
            if (@innerCheck_f) {
                @innerCheck_f = ();
                next;
            } else {
                push @valid_f, $i;
            }
        }        
    }
    for (my $i=2; $i<$secondnum+1; $i++) {
        my $check2 = $secondnum % $i;
        if ($check2 == 0) {
            for (my $x=$i-1; $x>1; $x--) {
                my $innercheck2 = $i % $x;
                if ($innercheck2 == 0) {
                    push @innerCheck_s, $x;
                    last;                    
                }
            }
            if (@innerCheck_s) {
                @innerCheck_s = ();
                next;
            } else {
                push @valid_s, $i;
            }
        }        
    }
    my $sum_f =0;
    my $sum_s =0;
    foreach (@valid_f) {
        $sum_f = $sum_f + $_;
    }
    foreach (@valid_s) {
        $sum_s = $sum_s + $_;
    }
       
    my $result;
    if ($sum_f == $sum_s) {
        $result = "VALID";
    } else {
        $result = "NOT VALID";
    }
    
    print "$line $result\n\n";
    
}