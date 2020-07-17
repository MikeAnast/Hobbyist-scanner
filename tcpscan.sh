
s="scanme.nmap.org"



tcp_scan(){
     nmap -sT -T4 $1 | awk '/(closed|open|filtered)/{print $1,$2,$3}'
 }

results=$(tcp_scan $s)

sqlite3 nmap.database "CREATE TABLE IF NOT EXISTS tcp_scan(host varchar(30),port varchar(30), state varchar(30), service varchar(30));"

declare -a tcp_array

tcp_array=($results)


for ((i=3; i < ${#tcp_array[@]}; i=i+3)); do
     #echo $i
    sqlite3 nmap.database "INSERT INTO tcp_scan VALUES('$s','${tcp_array[$i]}','${tcp_array[$i+1]}','${tcp_array[$i+2]}');"
    #echo ${tcp_array[$i]}
    #echo ${tcp_array[$i+1]}
    #echo ${tcp_array[$i+2]}
    #echo "-----------------"
 done




declare -a open_ports
for ((i=3; i < ${#tcp_array[@]}; i=i+3)); do
     #echo $i
    number=$(echo ${tcp_array[$i]} | grep -Eo '[0-9]+') 
    ${open_ports[i]}=${number}
    #echo ${tcp_array[$i]}
    #echo ${tcp_array[$i+1]}
    #echo ${tcp_array[$i+2]}
    #echo "-----------------"
done

echo open_ports