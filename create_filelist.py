import os 

data_path='data/VisDrone_devkit2019/VisDrone2019-DET-test/images'
txt_path='data/visdrone_test.txt'


with open(txt_path, 'w') as g:
	for f in os.listdir(data_path):
	    if f.endswith('.jpg'):
	    	g.write(f.split('.')[0]+'\n')
