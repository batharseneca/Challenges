#!\usr\bin\perl

#### PERL SOLUTION ####
use strict;
use warnings;

my $maxledsvoltage = sprintf("%.0f", (9 / 1.7));
my $maxledcurrent =

__DATA__

parallel same voltage ind current
serial ind voltage same current

We are going to use 9V batteries for our calculation. They suply a voltage of 9V (Volt) (big surprise there) and have a capacity from around 1200mAh (milliAmpere hour).
The lifetime of the battery can be calculate by deviding the capacity by the total Amperes we draw. E.g. 
If we have a 9V battery and we use a light that uses 600 mA, we can light the light for 2 hours (1200/600)
For our lights we'll use average leds, wich need an voltage of 1.7V and a current of 20mA to operate.

Since we have a 9V we can have a max of 5 leds connected in serial. 
But by placing circuits in parallel, we can have more than 5 leds in total, but then we'll drain the battery faster.
I'll split the challengs up in a few parts from here on.

Part 1
As input you'll be given the length in hours that the lights needs te be lit. You have give me the max number of led's we can have for that time

Input
1
Output
300

Explanation:
We can have 5 leds in serial, but then they'll take only a current of 20mA. 
The battery can give us 1200mA for 1 hour. So if we devide 1200 by 20 we get that we could have 60 times 5 leds.

Inputs
1
4
8
12
Outputs
300
75
35 (37 is also possible, but then we can't have 5 leds in serial for each parallel circuit)
25