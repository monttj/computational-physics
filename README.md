# Special topics in deep learning for big data

## ssh access
If you have accout for server @HYU\_PHY, you can access the server using the following command:
```bash
ssh -Y {YourID}@{ServerIP}
```

## Environment set up
If you don't have accout, follow these steps to set up the necessary environment:

### Prerequisite
- Python == 3.6.5
- cudnn == 7
- cudatoolkit == 9.0

### Anaconda set up
You need to install anaconda.
```
# download conda installation file by wget
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

sh Anaconda3-2022.10-Linux-x86_64.sh

# add conda path
export PATH=/opt/anaconda3/bin/:$PATH
```

In your conda environment, need to install tensorflow, Keras, Jupyter notebook, ipykernel. 
You can set up the environment using the provided 'env.yaml' file.
```
# create conda environment with env.yaml file
conda env create --file env.yaml
conda activate py36-cuda9.0 # this env name is set in env.yaml file.
```

## Usage
### Jupyter Notebook
[Jupyter Notebook](https://jupyter.org/) is a web-based interactive computing platform that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

To use Jupyter Notebook:
1. At the server
```
conda activate py36-cuda9.0
jupyter notebook --no-browser
```
You should check which port number is opened for jupyter notebook.

2. At your local computer
```
ssh -NL {Port}:localhost:{Port} {YourID}@{ServerIP}
```

3. Open a new browser and copy and paste the url from the step 1.
