### About

Code found here is a reimplementation of the model described in [DeViSE: A Deep Visual-Semantic Embedding Model](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41473.pdf).

The goal is to achieve semantic search over image dataset in a scalable fashion. We used [VGG16](https://keras.io/api/applications/vgg/) CNN pretrained on [ImageNet](http://www.image-net.org/about-overview) dataset, combining it with [GloVE](https://nlp.stanford.edu/projects/glove/) pretrained model consisting of [400k words and their 300D corresponding vectors](http://nlp.stanford.edu/data/glove.6B.zip).

Such a hybrid model performs reasonably well on images outside of image corpus, as well as on some categories that were not present during model creation.

Searching over dataset can be done in different ways:

* text -> images
* image -> labels
* image -> images

Fast queries are facilitated by [Annoy](https://github.com/spotify/annoy) library which implements an [approximate nearest neighbor](https://en.wikipedia.org/wiki/Nearest_neighbor_search#Approximate_nearest_neighbor) search algorithm.

### Resources and links

You can download training dataset by using `get-dataset.py`. Dataset is under (CC BY 3.0) licence and it's available [here](https://vision.cs.uiuc.edu/pascal-sentences/). This dataset is also used by [Emmanuel Ameisen](https://mlpowered.com/about/) in his [QCon 2018 talk](https://www.infoq.com/presentations/semantic-search-engine/) where he discusses DeViSE paper.

Other resources covering the same topic:

* <https://medium.com/@fpingham/devise-a-deep-visual-semantic-embedding-be2fd605de05>
* <https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/>
* [Jeremy Howard](https://medium.com/@jeremyphoward)'s [lecture](https://www.youtube.com/watch?v=tY0n9OT5_nA&feature=youtu.be&t=1h55m23s) where he explains devise approach
