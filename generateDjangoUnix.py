import os
import sys

virtualenvname = "mbrs"
packagename = "ftn-jsd"
print("---------Creating virtualenv---------")
os.system("virtualenv " + virtualenvname)
print("Successfully created virtualenv.")

print("---------Activating virtualenv---------")
activate_this_file = "./" + virtualenvname + "/bin/activate_this.py" 
with open(activate_this_file) as f:
    exec(f.read(), {'__file__': activate_this_file})
print("Successfully Activated virtualenv")

print("---------Install missing packeges.---------")
os.system("python -m pip install --upgrade pip")
os.system("pip install " + packagename)
print("Successfully finished package installation.")

import generated
if len(sys.argv) == 4:
	generated.main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
	generated.main()

print("Successfully generated.")

os.system("rm -rf " + virtualenvname)
