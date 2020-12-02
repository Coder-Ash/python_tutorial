#from mymodule import my_func

#To create a package you create a folder and add "__init__.py" file within the folder
#This tells Python to treat folder as a package and all scripts within will be 
#organized within that package.
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage.mysubscript import sub_report

#my_func()

some_main_script.main_report()
sub_report()