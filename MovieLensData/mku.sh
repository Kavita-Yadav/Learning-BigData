#!/bin/sh

# The purpose of this file is to generate all the u data sets from u.data.(i.e u1.base, u1.test.....u5.base, u5.test; ua.base, ua.test and ub.base, ub.test)

# used trap to remove temporary files at signals 1, 2 & 15. 1- clean tidyup, 2- Interrupt, 15- Terminate.
# tmp.$$ - helps to generate unique filename with current running process id.
# $i extract the value hold by i variable
# $i \* 20000 means i multiplied with 20000
# head - [option][filename]…[filename]
# head -`expr $i \* 20000` u.data means head will read i to 20000 lines from file u.data
# tail [option]  [filename]…[filename]
# tail -20000 > tmp.$$ means tail read last 20000 lines from tmp.$$ file
# head -`expr $i \* 20000` u.data | tail -20000 > tmp.$$ means head will retrive first i to 20000 lines from file u.data and saved that into tmp.SS file and then tail will retrieve last 20000 line from 
# output of the head command stored in tmp file.

# The -k option specifies the characters to sort by. We can sort this in many ways; currently it is sorted numerically, by the serial number (the first column). We can also sort by the second or third column.
# -k 1, 1n means sort by first column and 1n column.
# -k 2, 2n means sort by second column and 2n column and store result in u$i.test file
# allbut.pl is perl script file and ua/ub name prefix of the file.

trap `rm -f tmp.$$; exit 1` 1 2 15

for i in 1 2 3 4 5
do
	head -`expr $i \* 20000` u.data | tail -20000 > tmp.$$
	sort -t"	" -k 1,1n -k 2,2n tmp.$$ > u$i.test
	head -`expr \( $i - 1 \) \* 20000` u.data > tmp.$$
	tail -`expr \( 5 - $i \) \* 20000` u.data >> tmp.$$
	sort -t"	" -k 1,1n -k 2,2n tmp.$$ > u$i.base
done

allbut.pl ua 1 10 100000 u.data
sort -t"	" -k 1,1n -k 2,2n ua.base > tmp.$$
mv tmp.$$ ua.base
sort -t"	" -k 1,1n -k 2,2n ua.test > tmp.$$
mv tmp.$$ ua.test

allbut.pl ub 11 20 100000 u.data
sort -t"	" -k 1,1n -k 2,2n ub.base > tmp.$$
mv tmp.$$ ub.base
sort -t"	" -k 1,1n -k 2,2n ub.test > tmp.$$
mv tmp.$$ ub.test

