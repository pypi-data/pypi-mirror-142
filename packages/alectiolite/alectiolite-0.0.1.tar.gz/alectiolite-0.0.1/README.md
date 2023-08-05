# Alectiolite
New SDK format <br />


# Brief instructions 
conda create -n myenv python=3.6 <br />
conda activate myenv<br />

# Testing
## Temporary installation instructions until stable and publishable
python setup.py sdist bdist_wheel <br />
pip install . <br />

## Temporary uninstallation instructions
rm -fr  < path-to-alectio-lite-installation > <br />
rm -rf ./build <br />
rm -rf ./alectiolite.egg-info <br />
rm -rf ./dist <br />

## TODO 
- creating docstrings <br />
