import os, sys, random, time, getpass, requests
from time import sleep
from time import sleep as waktu
from random import randint
from os import system, name
username = 'MR'
password = 'Xyaa'
version = 'SIA GELO'
buffer_size = 898989
expired = ['19', '02', '2022']
ip = requests.get('https://api.ipify.org').text
pesing = '\033[0m- Created By Asep-IT Ganz\n- Email vakumhacker@gmail.com ( \033[32mTools Kedaluarsa \033[0m)\n'

def kontol(ngaceng):
    for peli in ngaceng + '\n':
        sys.stdout.write(peli)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0001)

sys.stdout.write('\x1b[1;35m\x1b]2; Script Ini Ada Expired By Asepit\x07')


 
def c(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 10)


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)



def login():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if tanggal >= exp:
        print (('\n').join(['' + pesing + '']))
        print (('\n').join(['- Sctipt Anda Kedaluarsa.. \n- Hubungin Jika Ingin Membeli Tols Lagi']))
        sys.exit()
    else:
    	kontol()

def kontol():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl = saat_ini.strftime('%d')
    bln = saat_ini.strftime('%m')
    thn = saat_ini.strftime('%Y')
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if float(tanggal) + 1 == float(exp):
        masuk()
    else:
    	silet()
        sys.exit()


def masuk():
	os.system('clear')
	print ('\033[0m- Created By Asep-IT Ganz\n- Email vakumhacker@gmail.com ( \033[32mLogin Private \033[0m)\n')
	print '\033[0m- Ip Kamu : ' + ip + ' '
	print ('- Expired : \033[32mAktif 19-02-2022\033[0m -\033[31m Brakhir 20-02-2022 \033[0m')
	print''
	uname = raw_input('- Username : ')
	if uname == username:
		pw = getpass.getpass('- password : ')
		if pw == password:
			print ('- Password SucsesFully ')
			os.system('sleep 0.9')
			os.system('cd tes && bash tol.sh')
		else:
			print ('- Password Salah Anjing ')
			exit()
login()
