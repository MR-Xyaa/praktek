import os, sys

print ("\033[1;32mMasukan UserName&Password:)")
print ("\033[1;32mKalo Gak Tau Pm MR-Xyaa 083138613993")
print ("\033[1;32mAtau Kunjungi Github Gw github.com/MR-Xyaa")
username = 'MR'      
password = 'Xyaa'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mSabar Install Tools MR-Xyaa Dulu,Tunggu 30 Detik", 
			sys.exit()

		else:
			print "\n\033[1;36mSalah Passwordnya Asu !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSalah Username Nya Babi !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()