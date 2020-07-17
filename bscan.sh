#!/bin/bash


#read -p 'please enter the site: ' s
#read -p 'please enter the port: ' x
##################################################
####################Basic scan####################
##################################################

#s="hackthissite.org"
s="scanme.nmap.org"
#x=22

#scan function
basic_scan() {
     nmap $1 | awk '/(closed|open|filtered)/{print $1,$2,$3}'
    }

#keep values of the scan functon on this variable
var=$(basic_scan $s)


#create database
sqlite3 nmap.database "CREATE TABLE IF NOT EXISTS basic_scan(host varchar(30),port varchar(30), state varchar(30), service varchar(30));"

#create array to store the results of the scan
declare -a test_array

#store the results of the scan
test_array=($var)
#echo "the length is ${#test_array[@]}"
#echo ${test_array[@]}

#Store to the database the values of the open/filtered/closed ports
for ((i=0; i < ${#test_array[@]}; i=i+3)); do
    #echo $i
    sqlite3 nmap.database "INSERT INTO basic_scan VALUES('$s','${test_array[$i]}','${test_array[$i+1]}','${test_array[$i+2]}');"
    #echo ${test_array[$i]}
    #echo ${test_array[$i+1]}
    #echo ${test_array[$i+2]}
done

######################################################
########################TCP Scan######################
######################################################

#TCP scan function
tcp_scan(){
     nmap -sT -T4 $1 | awk '/(closed|open|filtered)/{print $1,$2,$3}'
 }

#results of tcp scanning
results=$(tcp_scan $s)

#create table for tcp scanning results
sqlite3 nmap.database "CREATE TABLE IF NOT EXISTS tcp_scan(host varchar(30),port varchar(30), state varchar(30), service varchar(30));"

#create an array
declare -a tcp_array

#write the results to that array
tcp_array=($results)

#store the results to the database table
for ((i=3; i < ${#tcp_array[@]}; i=i+3)); do
     #echo $i
    sqlite3 nmap.database "INSERT INTO tcp_scan VALUES('$s','${tcp_array[$i]}','${tcp_array[$i+1]}','${tcp_array[$i+2]}');"
    #echo ${tcp_array[$i]}
    #echo ${tcp_array[$i+1]}
    #echo ${tcp_array[$i+2]}
    #echo "-----------------"
done
























