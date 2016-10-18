input="[->+<]"
binout=""
for i in range(0,len(input)):
	if input[i]==">":
		binout+="1000"
	if input[i]=="<":
		binout+="1001"
	if input[i]=="+":
		binout+="1010"
	if input[i]=="-":
		binout+="1011"
	if input[i]==".":
		binout+="1100"
	if input[i]==",":
		binout+="1101"
	if input[i]=="[":
		binout+="1110"
	if input[i]=="]":
		binout+="1111"
print(int(binout,2))
print("")

for i in range(0, int(binout, 2)):
	print("_",end="")

