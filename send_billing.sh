--------BEGIN send_billing.sh --------

#!/bin/bash

# Script to send a jcl job to the mainframe on a nightly basis
# This script gets yesterday's date in a DDmmddyy format an example is
# TU031114   Tuesday March 11 2014

# First we get yesterdays date as this script runs at just a bit after midnight
# The date command can give us almost what we need. We still need to change the day (say Tue) to TU and this is done via the sed options


JCLDATE=`date -d yesterday +%a%m%d%y | sed -e s/Sun/SU/ -e s/Mon/MO/ -e s/Tue/TU/ -e s/Wed/WE/ -e s/Thu/TH/ -e s/Fri/FI/ -e s/Sat/SA/`


# Now we have JCLDATE in the correct format.
echo $JCLDATE

# Here is where the magic happens. We need to create the jcl that is then sent to the mainframe via a jes submit ftp command


echo "//MN24HR62 JOB (10787,2),'RBOC W22',CLASS=V,MSGCLASS=V,">>MN24HR62.jcl
echo "// USER=NDMUSER,NOTIFY=CHIAFP1">>MN24HR62.jcl
echo "//*">>MN24HR62.jcl
echo "//*">>MN24HR62.jcl
echo "/*JOBPARM CARDS=999999,SYSAFF=LOMB">>MN24HR62.jcl
echo "//MN24HR62 EXEC PROC=MN24HR62,">>MN24HR62.jcl
echo "//          DAYDATE=`date -d yesterday +%a%m%d%y | sed -e s/Sun/SU/ -e s/Mon/MO/ -e s/Tue/TU/ -e s/Wed/WE/ -e s/Thu/TH/ -e s/Fri/FI/ -e s/Sat/SA/`,BILNAME=DAILY">>MN24HR62.jcl
echo "//">>MN24HR62.jcl


# OK now we have JCLJOB and we need to get it to the mainframe. A simple ftps should do the trick
lftp -d -e "site filetype=jes;put -a MN24HR62.jcl -o 'MN24HR62.jcl';quit" xmh.experiannet.net
if [[ $? -ne 0 ]]
        then
        echo "The nightly send biling script (send_billing.sh) had a problem"| mailx -s "Problems sending nightly billing to mainframe from `hostname`" CEMServerEmail@experian.com, cembatchsupport@experian.com

fi
mv MN24HR62.jcl MN24HR62.jcl-sent

--------END send_billing.sh --------
