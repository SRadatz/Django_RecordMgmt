# Django_RecordMgmt

Django server to managing grant records.
This is a windows installation guide for the Grants Management system.

Download and install the latest version .Net framework from https://dotnet.microsoft.com/download/dotnet-framework
Download and install the latest version of Visual C++ redistributable package from https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
Download and install the latest version of Mysql community server from https://dev.mysql.com/downloads/mysql/
  While installing set the DB name to “mydb”
  Set the root password to “InfInIty25!”
  All capital i’s
  Can be changed in settings.py once repo is downloaded
Download and install the latest version of python from https://www.python.org/downloads/
  Make sure to check the box that adds python to PATH
Download and install the latest version of Git from https://git-scm.com/download/win
  While installing add Git to PATH
Open an administrative powershell window and install pip, virtualenv, and django
  Install pip
    “python -m pip install -U pip”
  Install virtualenv
    “pip install virtualenv”
  Change directory to current drive
    “cd /”
  Create a virtual environment
    “virtualenv CSI_3450_Ivory_Radatz”
  Navigate to “C:\CSI_3450_Ivory_Radatz\Scripts”
    “cd /CSI_3450_Ivory_Radatz/Scripts”
  Activate Virtual environment
     “.\activate”
  Install Django
    “pip install django”
  Import Django into Python
   “Python”
  Opens a python terminal
    “Import django”
    “exit()”
  Change directory
    “cd /CSI_3450_Ivory_Radatz”
  Download git repo
    “git clone https://github.com/SRadatz/Django_RecordMgmt.git”
  Change directory
    “cd /CSI_3450_Ivory_Radatz/CSI3450_project”
  Start server
    “manage.py runserver”
Browse to localhost:8000
