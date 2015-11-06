import numpy as np
import sys
import subprocess as sp

input_dir = "./"
cmd1 = "ls "+input_dir+" |grep output_double.fits"
fits_files = sp.check_output(cmd1,shell=True)

files_list = fits_files.split()

for i in files_list:

    print i
    cmd2 = "ds9 -geometry 900x740 "+str(i)+" -scale limits 0.0 8.0 -zoom to fit -view colorbar no -saveimage png "+"./output_movie/"+str(i[:-5])+".png -exit"
    print cmd2
    sp.call(cmd2,shell=True)

output_video = "output.avi"
cmd3 = "cd ./output_movie/ && mencoder mf://*.png -mf w=800:h=600:fps=5:type=png -ovc raw -oac copy -o "+output_video
sp.call(cmd3,shell=True)
