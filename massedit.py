import os

for i in os.listdir('finalout'):
	name = i
	name_out = i#.replace(' ', '_out_')
	com = 'sox "finalout/' + name + '" "final_with_fades/' + name_out + '" fade 1 180 1'
	print(com)
	os.system(com)
