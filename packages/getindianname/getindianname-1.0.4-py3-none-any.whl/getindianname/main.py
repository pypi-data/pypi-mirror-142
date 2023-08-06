import random, requests
from os.path import abspath, join, dirname

full_path = lambda filename: abspath(join(dirname(__file__), filename))

file = {
    'malename': full_path('malename.txt'),
    'femalename': full_path('femalename.txt'),
    'maletitle': full_path('maletitle.txt'),
	'femaletitle': full_path('femaletitle.txt'),
	'ver': full_path('version.txt'),
	'pyver': full_path('pyversion.txt'),
}

space =" "

with open(file["malename"]) as mn:
    msufix = mn.read().splitlines()

with open(file["femalename"]) as fn:
    fsufix = fn.read().splitlines()

with open(file["maletitle"]) as mt:
    mprefix = mt.read().splitlines()

with open(file["femaletitle"]) as fmt:
    fprefix = fmt.read().splitlines()

allname=fsufix+msufix
alltitle=mprefix+fprefix

def randname():
	name = random.choice(allname)+space+random.choice(alltitle)
	return name
	
def female():
	name = random.choice(fsufix)+space+random.choice(fprefix)
	return name
	
def male():
	name = random.choice(msufix)+space+random.choice(mprefix)
	return name

def chkupdate(): #for names
	try:
		oldv=open(file["ver"],"r")
		old = oldv.read()
		new = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/getindianname/nameversion").text
		if old==new:
			pass
		else:
			print("Updating Names...")
			update()
	except :
		pass

def pypicheck():
	try :
		oldpv=open(file["pyver"],"r")
		oldp = oldpv.read()
		newp = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/getindianname/pypiversion").text
		if oldp==newp:
			pass
		else:
			print("Update Available on Pypi\n\nPlease Update it.")
	except:
		pass
		
def update():
	try :
		mdata = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/assets/male_name").text
		mfile = open(file["malename"],"w")
		mfile.write(mdata)
		mfile.close()
	
		fdata = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/assets/female_name").text
		fmfile = open(file["femalename"],"w")
		fmfile.write(fdata)
		fmfile.close()
	
		mtdata = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/assets/male_title").text
		mtfile = open(file["maletitle"],"w")
		mtfile.write(mtdata)
		mtfile.close()
	
		ftdata = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/assets/female_title").text
		fmtfile = open(file["femaletitle"],"w")
		fmtfile.write(ftdata)
		fmtfile.close()

		newv = requests.get("https://raw.githubusercontent.com/techux/getindianname/main/getindianname/nameversion").text
		oldv = open(file["ver"],"w")
		oldv.write(newv)
		oldv.close()
		
	except:
		pass

chkupdate()
pypicheck()