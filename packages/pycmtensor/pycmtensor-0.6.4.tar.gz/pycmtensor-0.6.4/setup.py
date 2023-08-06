# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycmtensor']

package_data = \
{'': ['*']}

install_requires = \
['Cython>=0.29.28,<0.30.0',
 'aesara>=2.4.0,<3.0.0',
 'biogeme>=3.2.8,<4.0.0',
 'dill>=0.3.4,<0.4.0',
 'ipykernel>=6.9.1,<7.0.0',
 'ipywidgets>=7.6.5,<8.0.0',
 'numpy>=1.19.0,<1.22.0',
 'pandas>=1.3.5,<2.0.0',
 'pydot>=1.4.2,<2.0.0',
 'scipy>=1.7.1,<1.8.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'pycmtensor',
    'version': '0.6.4',
    'description': 'Python Tensor based package for Deep neural net assisted Discrete Choice Modelling.',
    'long_description': '# PyCMTensor\n\n[![GitHub version](https://badge.fury.io/gh/mwong009%2Fpycmtensor.svg)](https://badge.fury.io/gh/mwong009%2Fpycmtensor)\n[![Documentation Status](https://readthedocs.org/projects/pycmtensor/badge/?version=latest)](https://pycmtensor.readthedocs.io/en/latest/?version=latest)\n![](https://img.shields.io/pypi/pyversions/pycmtensor)\n![Licence](https://img.shields.io/badge/Licence-MIT-blue)\n\nA tensor-based choice modelling Python package with deep learning capabilities\n\n`PyCMTensor` is a discrete choice model development platform which is designed with the use of deep learning in mind, enabling users to write more complex models using neural networks.\n`PyCMTensor` is build on [Aesara library](https://github.com/aesara-devs/aesara), and uses many features commonly found in deep learning packages such as Tensorflow and Keras.\n`Aesara` was chosen as the back end mathematical library because of its hackable, open-source nature.\nAs users of [Biogeme](https://biogeme.epfl.ch), you will be familiar with the syntax of `PyCMTensor` and as it is built on top of existing `Biogeme` choice models.\n\nThe combination of `Biogeme` and `Aesara` allows one to incorporate neural networks into discrete choice models that boosts accuracy of model estimates which still being able to produce all the same statistical analysis found in traditional choice modelling software.\n\n\n<!-- ![](https://img.shields.io/pypi/v/pycmtensor.svg) -->\n\n\n## Features\n\n* Efficiently estimate complex choice models with neural networks using deep learning algorithms\n* Combines traditional econometric models (Multinomial Logit) with deep learning models (ResNets)\n* Similar programming syntax as `Biogeme`, allowing easy substitution between `Biogeme` and `PyCMTensor` methods\n* Uses tensor based mathematical operations from the advanced features found in the `Aesara` library\n\n## Install\n\nTo install PyCMTensor, you need [Conda](https://docs.conda.io/en/latest/miniconda.html) (Full Anaconda works fine, but **miniconda** is recommmended for a minimal installation)\n\nOnce Conda is installed, install the required dependencies from conda by running the following \ncommand in your terminal:\n\n```console\n$ conda install pip git cxx-compiler m2w64-toolchain libblas libpython mkl numpy\n```\n\n>Note: Mac OSX user should also install `Clang` for a fast compiled code.\n\nThen, run this command in your terminal to download and install the development branch of `PyCMTensor`:\n\n```console\n$ pip install git+https://github.com/mwong009/pycmtensor.git@develop -U\n```\n\nThe development branch is the most up-to-date version of `PyCMTensor`. If you want a stable branch, remove ``@develop`` at the end of the url.\n\n## How to use\n\nPyCMTensor uses syntax very similar to `Biogeme`. Users of `Biogeme` should be familiar \nwith the syntax.\n\nStart an interactive session (IPython or Jupyter Notebook) and import PyCMTensor:\n```Python\nimport pycmtensor as cmt\n```\n\nSeveral submodules are also important to include:\n```Python\nfrom pycmtensor.expressions import Beta # Beta class for model parameters\nfrom pycmtensor.models import MNLogit   # model library\nfrom pycmtensor.optimizers import Adam  # Optimizers\nfrom pycmtensor.results import Results  # for generating results\n```\n\nFor a full list of submodules and description, refer to [API Reference](/autoapi/index)\n\n## Simple example: Swissmetro dataset\n\nUsing the swissmetro dataset from Biogeme to define a simple MNL model. \n\nThe following is a replication of the results from Biogeme using the `Adam` optimization algorithm and a `Cyclic learning rate`. For further examples including the ResLogit model, refer **here**.\n\n1. Import the dataset and perform some data santiation\n\t```Python\n\tswissmetro = pd.read_csv("swissmetro.dat", sep="\\t")\n\tdb = cmt.Database(name="swissmetro", pandasDatabase=swissmetro, choiceVar="CHOICE")\n\tglobals().update(db.variables)\n\t# additional steps to format database\n\tdb.data["CHOICE"] -= 1 # set the first choice to 0\n\tdb.choices = sorted(db.data["CHOICE"].unique()) # save original choices\n\tdb.autoscale(\n\t\tvariables=[\'TRAIN_CO\', \'TRAIN_TT\', \'CAR_CO\', \'CAR_TT\', \'SM_CO\', \'SM_TT\'], \n\t\tdefault=100., \n\t\tverbose=False\n\t) # automatically scales features by 1/100.\n\t```\n\n\t``cmt.Database()`` loads the dataset and automatically defines symbolic Tensor Variables.\n\n2. Initialize the model parameters\n\t```Python\n\tb_cost = Beta("b_cost", 0.0, None, None, 0)\n\tb_time = Beta("b_time", 0.0, None, None, 0)\n\tasc_train = Beta("asc_train", 0.0, None, None, 0)\n\tasc_car = Beta("asc_car", 0.0, None, None, 0)\n\tasc_sm = Beta("asc_sm", 0.0, None, None, 1)\n\t```\n\n3. Specify the utility functions and availability conditions\n\t```Python\n\tU_1 = b_cost * db["TRAIN_CO"] + b_time * db["TRAIN_TT"] + asc_train\n\tU_2 = b_cost * db["SM_CO"] + b_time * db["SM_TT"] + asc_sm\n\tU_3 = b_cost * db["CAR_CO"] + b_time * db["CAR_TT"] + asc_car\n\tU = [U_1, U_2, U_3]\n\tAV = [db["TRAIN_AV"], db["SM_AV"], db["CAR_AV"]]\n\t```\n\n4. Specify the model ``MNLogit``\n\t```Python\n\tmymodel = MNLogit(u=U, av=AV, database=db, name="mymodel")\n\tmymodel.add_params(locals())\n\t```\n\n5. Set up the training hyperparameters\n\t```Python\n\tmymodel.config["patience"] = 20000\n\tmymodel.config["base_lr"] = 0.0012\n\tmymodel.config["max_lr"] = 0.002\n\tmymodel.config["learning_scheduler"] = "CyclicLR"\n\tmymodel.config["cyclic_lr_step_size"] = 8\n\tmymodel.config["cyclic_lr_mode"] = "triangular2"\n\t```\n\n6. Call the training function and save the trained model\n\t```Python\n\tmodel = cmt.train(mymodel, database=db, optimizer=Adam, batch_size=128, \n\t                  max_epoch=999)\n\t```\n\n7. Generate the statistics and correlation matrices\n\t```Python\n\tresult = Results(model, db, show_weights=True)\n\tresult.print_beta_statistics()\n\tresult.print_correlation_matrix()\n\t```\n\n8. Plot the training performance and accuracy\n\t![](../viz/fig.png)\n\n8. Visualize the computation graph\n\t```Python\n\timport aesara.d3viz as d3v\n\tfrom aesara import printing\n\tprinting.pydotprint(mymodel.cost, "graph.png")\n\t```\n\t![](../viz/print.png)\n\n\n## Credits\n\nPyCMTensor was inspired by [Biogeme](https://biogeme.epfl.ch) and aims to provide deep learning modelling tools for transport modellers and researchers.\n\nThis package was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.',
    'author': 'Melvin Wong',
    'author_email': 'm.j.w.wong@tue.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mwong009/pycmtensor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
