import glob
import pkg_resources
import subprocess
import sys
import pathlib
import pkg_resources
import json

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

req = glob.glob("/DMP/dockerfile/**/requirements.txt", recursive=True)

install("pipenv")
install("pip-licenses")

#add preinstalled packages to ignore list 
with subprocess.Popen([sys.executable, "-m", "pipenv", "run", "pip-licenses", "--format=json-license-finder"], stdout=subprocess.PIPE) as proc:
	preinstalled = json.loads(proc.stdout.read())

ignore=[i['name'] for i in preinstalled]
	
for r in req:
	print("Processing {}".format(r))
	
	with pathlib.Path(r).open() as requirements_txt:
		install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]
	
	subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", r])
	
subprocess.check_call([sys.executable, "-m", "pipenv", "run", "pip-licenses", "--order=license", "--format=markdown", "--ignore-packages"] + ignore)
