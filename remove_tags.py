import codecs
import glob
import re # for charactors matching

files = glob.glob("./path/*")

for file in files:
    print(file) # for debug    
  
    with open(file,encoding='utf-8') as g:
        data_lines = g.read()

    reg_obj = re.compile(r"<[^>]*?>")
    
    data_lines = reg_obj.sub("",data_lines)    
    data_lines = data_lines.replace("\n","") # eliminate line feed code
    
    re_file = file.replace('path','path_re2') # change directory for save doc
    re_file = re_file.replace('.xml','.txt')
    
    with codecs.open(re_file, 'w', 'utf-8') as f:
        f.write(data_lines)
