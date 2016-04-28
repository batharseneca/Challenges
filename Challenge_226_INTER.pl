###### perl solution

use strict;
# use warnings;

my @darray;
my @coord;
my @labels = ("a", "b", "c", "d", "e", "f", "g");
my @labelrows = (0,1,2,3,4,5,6);

my %out = (
    0 => 'A',
    1 => 'B',
    2 => 'C',
    3 => 'D',
    4 => 'E',
    5 => 'F',
    6 => 'G',
);

my $movenum = 1;
my $result;

for (my $i=0; $i<7; $i++) {
    for (my $x=0; $x<7; $x++ ) {
        $darray[$i][$x]=".";
    }    
}

while (my $line = <DATA>) {
    @coord = ();
    chomp ($line);
    $line =~ /(\w).*(\w)/;
    my $player1move = $1;
    my $player2move = $2;
    
    for (my $i =0; $i<scalar(@labels); $i++) {
        if (lc($player1move) eq $labels[$i]) {
            $player1move = $labelrows[$i];            
        }
        if ($player2move eq $labels[$i]) {
            $player2move = $labelrows[$i];            
        }
    }    
    for (my $h=6; $h>-1; $h--) {
        if ($darray[$h][$player1move] eq ".") {
            $darray[$h][$player1move] = "X";
            push @coord, $h;
            push @coord, $player1move;
            push @coord, "X";
            last;
        }
    }
    $result = CheckVictory(@coord);
    @coord = ();
    if ($result ne "NO") {
        print "$result \n";
        last;
    }    
    for (my $h=6; $h>-1; $h--) {
        if ($darray[$h][$player2move] eq ".") {
            $darray[$h][$player2move] = "O";
            push @coord, $h;
            push @coord, $player2move;
            push @coord, "O";
            last;
        }
    }
    $result = CheckVictory(@coord);
    if ($result ne "NO") {
        print "$result \n";
        last;
    }   
    $movenum++;   
}

sub CheckVictory {
    my $condition="NO";
    my $col = $_[1];
    my $row = $_[0];
    my $playeridentity = $_[2];
    my $proceed = 1;    
    for (my$s =0; $s<4; $s++) {
        if ($darray[$row][( ($col+3) - $s )] eq $playeridentity && $darray[$row][( ($col +2) - $s )] eq $playeridentity && $darray[$row][( ($col +1) - $s )] eq $playeridentity && $darray[$row][($col - $s)] eq $playeridentity) {
            $condition = "$playeridentity won at move $movenum with (-row $row:" . $out{($col+3-$s)} . " -row $row:" . $out{($col+2-$s)} . " -row $row:" . $out{($col+1-$s)} . " -row $row:" . $out{($col-$s)} . ")";
            $proceed = 0;
            last;
        }
    }    
    if ($proceed==1) {
        for (my$s =0; $s<4; $s++) {
            if ($darray[$row+3-$s][$col] eq $playeridentity && $darray[( ($row+2) - $s )][$col] eq $playeridentity && $darray[( ($row+1) - $s )][$col] eq $playeridentity && $darray[($row - $s)][$col] eq $playeridentity) {
                $condition = "$playeridentity won at move $movenum with (-row " . ($row+3-$s) . ":$col" . " -row " . ($row+2-$s) . ":$col" . " -row " . ($row+1-$s) . ":$col" . " -row " . ($row-$s) . ":$col)";
                $proceed = 0;
                last;
            }
        }
        if ($proceed==1) {
            for (my$s =0; $s<4; $s++) {
                if ($darray[( ($row+3) - $s )][( ($col+3) - $s )] eq $playeridentity && $darray[( ($row+2) - $s )][( ($col+2) - $s )] eq $playeridentity && $darray[( ($row+1) - $s )][( ($col+1) - $s )] eq $playeridentity && $darray[( $row - $s )][( $col - $s )] eq $playeridentity) {
                    $condition = "$playeridentity won at move $movenum with (-row " . ($row+3-$s) . ":" . ($col+3-$s) . " -row " . ($row+2-$s) . ":" . ($col+2-$s) . " -row " . ($row+1-$s) . ":" . ($col+1-$s) . " -row " . ($row-$s) . ":" . ($col-$s) . ")";
                    $proceed = 0;
                    last;
                }
            }
            if ($proceed==1) {
                for (my$s =0; $s<4; $s++) {
                    if ($darray[( ($row-3) + $s )][( ($col+3) - $s )] eq $playeridentity && $darray[( ($row-2) + $s )][( ($col+2) - $s )] eq $playeridentity && $darray[( ($row-1) + $s )][( ($col+1) - $s )] eq $playeridentity && $darray[( $row + $s )][( $col - $s )] eq $playeridentity) {
                        $condition = "$playeridentity won at move $movenum with (-row " . ($row-3+$s) . ":" . ($col+3-$s) . " -row " . ($row-2+$s) . ":" . ($col+2-$s) . " -row " . ($row-1+$s) . ":" . ($col+1-$s) . " -row " . ($row+$s) . ":" . ($col-$s) . ")";
                        $proceed = 0;
                        last;
                    }
                }
            }
        }
    }    
    return $condition;
}

foreach (@darray) {
    print @{$_}, "\n";
}


__DATA__
D  d
D  c    
C  c    
C  c
G  f
F  d
F  f
D  f
A  a
E  b
E  e
B  g
G  g
B  a