input="trolololo"
bo=str(bin(len(input)))[2:]
out=""
for i in range (0,len(bo)//4):
	x=bo[4*i]+bo[4*i+1]+bo[4*i+2]+bo[4*i+3]
	if x=="1000":
		out+=">"
	if x=="1001":
		out+="<"
	if x=="1010":
		out+="+"
	if x=="1011":
		out+="-"
	if x=="1100":
		out+="."
	if x=="1101":
		out+=","
	if x=="1110":
		out+="["
	if x=="1111":
		out+="]"
print(out)	
