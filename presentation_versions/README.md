# Python notebooks used for presentation

This directory contains different Jupyter notebooks used for training the model with different parameters or datasets:

- 1000 images dataset, 30 epochs, 32 batch size, 3 additional layers -- [Jupyter notebook](./semantic-image-search-30epoch-32batch-3layer.ipynb) and corresponding [PDF](./semantic-image-search-30epoch-32batch-3layer.pdf)
- 1000 images dataset, 50 epochs, 32 batch size, 2 additional layers -- [Jupyter notebook](./semantic-image-search-final.ipynb) and corresponding [PDF](./semantic-image-search-final.pdf)
- 1000 images dataset, 30 epochs, 16 batch size, 1 additional layer -- [Jupyter notebook](./semantic-image-search-30epoch-16batch-1layer.ipynb) and corresponding [PDF](./semantic-image-search-30epoch-16batch-1layer.pdf)
- ≈10000 images dataset, 50 epochs, 32 batch size, 2 additional layers -- [Jupyter notebook](./semantic-image-search-iaprtc12.ipynb) and corresponding [PDF](./semantic-image-search-iaprtc12.pdf)

The first three models were trained using the same image dataset which is available under (CC BY 3.0) licence [here](https://vision.cs.uiuc.edu/pascal-sentences/).

In the last notebook the IAPR TC-12 Benchmark is used, it is available without copyright restriction [here](http://www-i6.informatik.rwth-aachen.de/imageclef/resources/iaprtc12.tgz). We loaded around half of the set. These are the directories which were kept for training: `00  05  06  07  10  11  17  21  23  24  27  28  29  30  31  32  33  34  35  37  39`.
