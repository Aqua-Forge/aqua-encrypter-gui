# -*- coding: utf-8 -*-
# Encryption/Decryption Algorithm

allowedAscii = 400

def encryptFile(filePath, encryptionPath, key):
	with open(filePath, "r", encoding="utf-8") as f: f1 = f.read()
	f2 = open(encryptionPath, "wb")
	i = 0
	for c in f1:
		numW = ord(c) + ord(key[i])
		if(numW>allowedAscii): numW -= allowedAscii+1
		w = chr(numW)
		f2.write(w.encode('utf-8'))
		if(i<len(key)-1): i += 1
		else: i=0
	f2.close()

def decryptFile(encryptionPath, filePath, key):
	with open(encryptionPath, "r", encoding="utf-8") as f: f1 = f.read()
	f2 = open(filePath, "wb")
	i = 0
	for c in f1:
		numW = ord(c) - ord(key[i])
		if(numW<0): numW += allowedAscii+1
		w = chr(numW)
		f2.write(w.encode('utf-8'))
		if(i<len(key)-1): i += 1
		else: i=0
	f2.close()

