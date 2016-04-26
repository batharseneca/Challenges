#!/usr/bin/perl 
use strict;
use warnings;

my $ref2 = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [2, 7, 6, 9, 5, 1, 4, 3, 8], [3, 5, 7, 8, 1, 6, 4, 9, 2], [8, 1, 6, 7, 5, 3, 4, 9, 2]];

foreach my$input1(@{$ref2}) {
    $"=" , ";
    print "[ @{$input1} ]  => ", verify($input1), "\n";
}

sub verify {
    my @ar = @{$_[0]};   
    my $result="true";
    my $totalhoriz = 0;
    my $totalvert = 0;
    my $totaldiag = 0;
    for (my $i=0; $i<9; $i=$i+3) {
        for (my $x=0; $x<3; $x++) {
            $totalhoriz = $totalhoriz + $ar[$i+$x];
        }
        if ($totalhoriz != 15) {
            $result = "false";
            $totalhoriz = 0;
        } else {
            $totalhoriz = 0;
        }
    }
    for (my $i=0; $i<3; $i++) {
        $totalvert = $ar[$i] + $ar[$i+3] + $ar[$i+6];
        if ($totalvert != 15) {
            $result = "false";
            $totalvert = 0;
        } else {
            $totalvert = 0;
        }
    }
    if ( ($ar[0] + $ar[4] + $ar[8]) != 15 || ($ar[2] + $ar[4] + $ar[6]) != 15 ) {
        $result = "false";
    }
    return $result;
}
















# $n = (length(@ar) / 3);
# $checksum =  ($n*3 + $n) / 2;





# sub verify {
    # my @ar = @{$_[0]};
    # my $n = (length(@ar) / 3);
    # my $checksum =  ($n*3 + $n) / 2;
    
    
    # my $result="true";
    # my $totalhoriz = 0;
    # my $totalvert = 0;
    # my $totaldiag = 0;
    # for (my $i=0; $i<(length(@ar)); $i=$i+3) {
        # for (my $x=0; $x<3; $x++) {
            # $totalhoriz = $totalhoriz + $ar[$i+$x];
        # }
        # if ($totalhoriz != $checksum) {
            # $result = "false";
            # $totalhoriz = 0;
        # } else {
            # $totalhoriz = 0;
        # }
    # }
    # for (my $i=0; $i<3; $i++) {
        # for (my $x=0; $x<(length(@ar) / 3));)
    # }
    # for (my $i=0; $i<3; $i++) {
        # $totalvert = $ar[$i] + $ar[$i+3] + $ar[$i+6];
        # if ($totalvert != $checksum) {
            # $result = "false";
            # $totalvert = 0;
        # } else {
            # $totalvert = 0;
        # }
    # }
    # if ( ($ar[0] + $ar[4] + $ar[8]) != $checksum || ($ar[2] + $ar[4] + $ar[6]) != $checksum ) {
        # $result = "false";
    # }
    # return $result;
# }