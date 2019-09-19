-------- BEGIN ftp_batch_profile_id_and_name.sh-------
#!/bin/bash
#
# SCRIPT_NAME:  ftp_batch_profile_id_and_name
#
#    STEP01: Get a list of all the batch profile id's along with the company name
#    STEP02: FTP the file to the mainframe
#

FTP_REPORT=/home/cem/scripts/logs/ftp.batch_profile_content
LOG=/home/cem/scripts/logs/ftp_batch_profile_id_and_name.log
ORACLE_HOME=/oracle/product/11202

export ORACLE_HOME

echo `date` -- Starting /home/cem/scripts/ftp_batch_profile_id_and_name > $LOG


/oracle/product/11202/bin/sqlplus batchman/mec2batch@mvpr @/home/cem/scripts/sql/batch_profile_id_and_name quit
echo "epsv4"                                                                          > $FTP_REPORT
echo "site LRECL=140"                                                                >> $FTP_REPORT
echo "site RECFM=FB"                                                                 >> $FTP_REPORT
echo "put -a /customer/billing/batch_profile_id_and_name.dat -o  \"'CHIUNX1.BATCH.PROFID.CONAME'\"" >> $FTP_REPORT
echo "quit"                                                                                         >> $FTP_REPORT

  lftp  xmh.experiannet.net < $FTP_REPORT 1>>$LOG 2>>$LOG

  # RETURN_CODE=$(cat $LOG | grep -c "Transfer completed successfully")
  RETURN_CODE=$(cat $LOG | grep -c "bytes transferred")

  if [[ $RETURN_CODE -eq 0 ]]
  then
     echo "Transfer was complete" >>$LOG
  else
     echo "Transfer was NOT complete" >> $LOG
     echo "////////////////////////////////////////////////////////////////////////////////" >> $LOG
     echo "// In the event that you have received this Email an error has occurred which //" >> $LOG
     echo "//       requires you to investigate job ftp_batch_profile_id_and_name.       //" >> $LOG
     echo "////////////////////////////////////////////////////////////////////////////////" >> $LOG
     /home/cem/scripts/perl_mail.pl "Mike.Nicholson@experian.com" "CEMServerEmail@experian.com" "ftp_batch_profile_id_and_name was NOT complete." $LOG

  fi

exit 0
-------- END ftp_batch_profile_id_and_name.sh-------
