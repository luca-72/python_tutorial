import sys ### The sys module provides access to some variable used or maintained ny the interpreter and to functions that interact stronly with the interpreter.
import datetime
now = datetime.datetime.now()
print("The current date and time is ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Python Version")
print(sys.version)
print("Version Information")
print(sys.version_info)
print("Python Copyrights")
print(sys.copyright)