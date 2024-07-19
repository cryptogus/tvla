from cwtvla.ktp import FixedVRandomText, verify_AES
import numpy as np
import pandas as pd

N = 10000
key_len = 16
ktp = FixedVRandomText(key_len)

fixedKeyList = []
fixedPtList = []
randomKeyList = []
randomPtList = []

for i in range(N):
	key, text = ktp.next_group_A() # Fixed Data
	fixedKeyList.append(key.hex())
	fixedPtList.append(text.hex())

	key, text = ktp.next_group_B() # Random Data
	randomKeyList.append(key.hex())
	randomPtList.append(text.hex())

fixedSet = {"Key":fixedKeyList, "Plaintext":fixedPtList}
fixedDf = pd.DataFrame(fixedSet)
fixedDf.to_csv("Case1FixedTextDataSet.csv")

randomSet = {"Key":randomKeyList, "Plaintext":randomPtList}
randomDf = pd.DataFrame(randomSet)
randomDf.to_csv("Case1RandomTextDataSet.csv")
