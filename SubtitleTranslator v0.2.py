import os
import time
import googletrans
from googletrans import Translator

translator = Translator()

print("----- WELCOME TO SUBSTITLE TRANSLATOR v0.2 -----\nAuthor : MLHYLMZ\n")

#print(googletrans.LANGUAGES);

# FILENAME INPUT
fileName = input("\nWhat is your filename?\nExample : mysubstitle.srt\n\nFilename : ")

fileNameOpen = fileName[0:-4]+".txt"
print(fileNameOpen)
os.rename(fileName, fileName[0:-4]+".txt")
os.system('CLS')


# TRANSLATION DESTONATION LANGUAGE CHOICE
Dchoice = input("What is your destination language?\n\nArabic : 'ar' , Bulgarian : 'bg' , Danish : 'da' , *English : 'en' , French : 'fr' , German : 'de' , Greek : 'el' , Hindi : 'hi' , Indonesian : 'in' , Italian : 'it' , Japanese : 'ja' , Korean : 'ko' , Polish : 'pl' , Portuguese : 'pt' , Romanian : 'ro' , Russian : 'ru' , Spanish : 'es' , *Turkish : 'tr' , Ukrainian : 'uk'\n\nDestination language : ")
os.system('CLS')




# GOOGLE TRANSLATE FUNCTION
def cevir(data):
	asd= translator.translate(data ,dest=Dchoice)
	return asd.text

# FIRST FILE READ
f = open(fileNameOpen, "r")
lines = f.readlines()
f.close()

# LINES TO ARRAY
names = []
for line in lines:
	x = line[:-1]
	names.append(x)


# FILE WRITE
new_f = open(fileName[0:-4]+" Translated.txt","w+")

start_time = time.time()	
# TRANSLATE AND CHECKING
for i in range(len(names)):

	# Translation Progress
	per = i/len(names)*100
	perDivide = int(per / 2)
	perDivideMod = 50 - perDivide
	percent = "{:.2f}".format(per)


	print("\n  Translating...  \n\n  Progress %",percent,"  ",end = "")
	print("[",end="")
	for x in range(perDivide):
		print("#",end = "")
	for a in range(perDivideMod):
		print("-",end = "")
	print("]",end = "")



	# Checking Sentences
	if names[i].startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
		new_f.write(names[i]+"\n")

	elif names[i] == '':
		new_f.write(names[i]+"\n")

	else:
		out = cevir(names[i])
		names[i] = out
		new_f.write(names[i]+"\n")
	os.system('CLS')


new_f.close()
os.rename(fileName[0:-4]+".txt", fileName)
os.rename(fileName[0:-4]+" Translated.txt",fileName[0:-4]+"Translated.srt")
print("Translation finished in %s seconds.\nTranslated .srt file saved in the same directory." % (int(time.time() - start_time)))

