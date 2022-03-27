#! /system/bin/sh
#pakebash
R='\x1b[1;31m'

G='\x1b[1;32m'

B='\x1b[1;34m'

Y='\x1b[1;33m'

C='\x1b[1;36m'

D='\x1b[0m'

# Diatas adalah sekumpulan kode warna yang digunakan didalam script ini

function Percent(){

    message="$1" #($1) artinya untuk memasukan data ke parameter ke 1

    max=$2 #($2) untuk parameter ke 2 dan dan selanjutnya

    #make loop

    while true; do

        i=1

        #-le (less than) atau kurang dari

        #0 kurang dari maksimal (100)

        #maka pernyataan akan di jalankan dari angka 1-100

        while [ $i -le $max ]; do

            echo -ne "\r${G}[✓]${C} $message ${G}$i${D} %"

            #jika i nilainya sama dengan 100 atau batas maksimal maka artinya metode / fungsi Perce             >

            #Percent "Loading..." 100

            #akan terus di ulang

            if [ $i -eq 100 ]; then

                echo -ne "${G} [UDAH!]${D}\n"

            fi

            #naikan nilai variabel i sebesar 1

            #ini yang akan menjadi tulisan angka 1 sampai 100

            let i++

        done

    done

}

Percent "Loading..." 100
