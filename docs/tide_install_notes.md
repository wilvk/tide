# Dev install (linux)_

## prerequisites:

make sure gnu build tools are installed to be able to run Make

docker is required for tests


## clone the repos:

git clone https://github.com/tide-org/tide

git clone https://github.com/tide-org/tide-plugins

git clone https://github.com/tide-org/vgdb

# install tide for local dev:

cd tide

make local-dev

cd ..

## test from commandline (optional):

ln -s ./tide/plugins ./tide-plugins/plugins/

export TIDE_CONFIG_LOCATION=$(pwd)/tide-plugins/plugins/atom/test_c_filter/ 

tide

there will be some json output to stdou

Ctrl-C, Ctrl-C

# run python in vim:

edit tide-plugins/plugins/atom/python/settings.yaml:

change the line with main_process_default_arguments: to
  main_process_default_arguments: ' -m pdb /home/will/source/wilvk/vgdb/tests/binaries/test_py_script.py'

cd tide

make vim_python 

in vim, to start:

:Vgdb

to step into the code:

:VgRunConfigCommand step


## running tests

from the tide base path, run `make tests`

from the vgdb base path, run `make tests`



# Dev install MacOs

## prerequisites

Install XCode tools for the 'make' command.

Install Docker and docker-compose for tests, etc.

Install brew to install gdb

Install the `./tests/scripts/gdb_tim.rb` brew formula to allow switching between remote-capable gdb and local MacOS capable gdb.


