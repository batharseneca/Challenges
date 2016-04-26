use strict;
use warnings;
# 0 = OFF       1 = ON
my $fileName = "lots_of_switches.txt";
my $size = $ARGV[0];
my $output = 0;

my @case;
for (my $i=0; $i<$size; $i++) {
    push @case, 0;
}

open my $input, $fileName or die "Could not open $fileName: $!";    
while (my $line = <$input>) {       
    chomp $line;  
    $line =~ /(\d*)[^\d](\d*)/;
    my $start = $1;
    my $end = $2;
    if ($start > $end) {
        my $holder = $start;
        $start = $end;
        $end = $holder;
    }
   
    for (my $i= $start; $i<$end+1; $i++) {
        if ($case[$i] == 0) {
            $case[$i] = 1;
        } else {
            $case[$i] = 0;
        }
    }   
} 
close $input;

foreach my$pos (@case) {
    $output += $pos;
}

print "Output: $output";



# $"="\n";




__DATA__
10
3 6
0 4
7 3
9 9

    0123456789
    ..........
3-6    ||||
    ...XXXX...
0-4 |||||
    XXX..XX...
7-3    |||||
    XXXXX..X..
9-9          |
    XXXXX..X.X