import glob
import os.path

print "PDF References"
print "=============="
print 
for root,dirs,files in os.walk('.'):
    for f in files:
        name,ext = os.path.splitext(f)
        full = os.path.abspath(root+'/'+f)
        if ext =='.pdf':
            print
            print '`'+ name + ' <file://'+ full + '>`_'
            print 
