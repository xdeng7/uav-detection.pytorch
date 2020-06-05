

infile='VisDrone2019-DET-val/val.txt'
outfile='visdrone_val.txt'

with open(outfile,'w') as w:
	with open(infile,'r') as r:
		filelist=r.readlines()
	for line in filelist:
		new_line=line.split('.')[0]
		w.write(new_line+'\n')


