# Overview

Given the number of different kinds of neural networks, here is a cheat sheet to help choose the network to use.

# Neural Network Architecture Review

## Artificial Neural Network (ANN) and Deep Neural Networks (DNN)

Typically, ANNs and DNNs are composed of dense layers.  ANNs are typically defined by having one hidden layer and DNNs have two or more.

### Choosing Topology for ANNs and DNNs

The topology or architecture of a neural network is defined as the type and number of layers and the type and number of neurons in each layer.  By following a small set of clear rules, one can programmatically configure a competent network architecture. Following this schema will generate a competent architecture but probably not an optimal one. Once this network is initialized, the configuration can be iteratively tuned during training using a number of ancillary algorithms including pruning, genetic optimization, etc.

Every neural network has three types of layers: *input*, *hidden*, and *output*..

#### The Input Layer

Every neural network should have exactly one.  With respect to the number of neurons comprising this layer, this parameter is completely and uniquely determined once the shape of the training data is known. Specifically, the number of neurons comprising the hidden layer is equal to the number of features (columns) in the data. Some neural network configurations add one additional node for a bias term.

#### The Output Layer

Every neural network has exactly one output layer.Determining its size (number of neurons) is simple; it is completely determinedby the chosen model configuration.

Is your neural network going to run a classification problem(returns a discrete value) or a regression problem (returns a continuousvalue)?

·       If the neural network is a regressor, then theoutput layer has a single node.

·       If the neural network is a classifier, then italso has a single node unless softmax is used in which case the output layerhas one node per class label in your model.

##### The Hidden Layers

How many hidden layers should be in the neural network?

If your data is linearly separable, then you don't need anyhidden layers at all. Of course, you don't need an neural network to resolveyour data either, but it will still do the job.

Beyond that, there's a mountain of commentary on thequestion of hidden layer configuration in neural networks (see <http://www.faqs.org/faqs/ai-faq/neural-nets/part1/preamble.html>).One issue is the performance difference from adding additional hidden layers.One hidden layer is sufficient for a large majority of classification andregression problems.  Jeff Heaton (<http://www.heatonresearch.com/2017/06/01/hidden-layers.html>)provides these outlines for choosing the number of hidden layers:

**Table: Determining the Number of Hidden Layers**

| **Num   Hidden Layers** | **Result**                                                   |
| ----------------------- | ------------------------------------------------------------ |
| none                    | Only  capable of representing linear separable functions or decisions. |
| 1                       | Can  approximate any function that contains a continuous mapping from one finite  space to another. |
| 2                       | Can  represent an arbitrary decision boundary to arbitrary accuracy with rational  activation functions and can approximate any smooth mapping to any accuracy. |
| >2                      | Additional  layers can learn complex representations (sort of automatic feature  engineering) for layer layers. |

How many neurons should go on the hidden layers? Jeff Heatongives some empirically-derived rules-of-thumb (<http://www.heatonresearch.com/2017/06/01/hidden-layers.html>):

·       The number of hidden neurons should be betweenthe size of the input layer and the size of the output layer.

·       The number of hidden neurons should be 2/3 thesize of the input layer, plus the size of the output layer.

·       The number of hidden neurons should be less thantwice the size of the input layer.

##### Optimization of the Network Configuration

Pruning describes a set of techniques to trim network size(by nodes not layers) to improve computational performance and sometimesresolution performance. The gist of these techniques is removing nodes from thenetwork during training by identifying those nodes which, if removed from thenetwork, would not noticeably affect network performance (i.e., resolution ofthe data). (Even without using a formal pruning technique, you can get a roughidea of which nodes are not important by looking at your weight matrix aftertraining; look weights very close to zero--it's the nodes on either end ofthose weights that are often removed during pruning.) Obviously, if you use apruning algorithm during training then begin with a network configuration thatis more likely to have excess (i.e., 'prunable') nodes--in other words, whendeciding on a network architecture, err on the side of more neurons, if you adda pruning step.

 

Put another way, by applying a pruning algorithm to yournetwork during training, you can approach optimal network configuration;whether you can do that in a single "up-front" (such as agenetic-algorithm-based algorithm) I don't know, though I do know that for now,this two-step optimization is more common.

#### References

Cross Validated, "How to choose the number of hidden layers and nodes in a feedforward neural network", March 15, 2017, https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw

Cross Validated, "Why are neural networks becoming deeper, but not wider?", July 13, 2016, <https://stats.stackexchange.com/questions/222883/why-are-neural-networks-becoming-deeper-but-not-wider>

Heaton Research, "The Number of Hidden Layers", June 1, 2017, http://www.heatonresearch.com/2017/06/01/hidden-layers.html

Stathakis, D., "How many hidden layers and nodes", International Journal of Remote Sensing
Vol. 30, No. 8, 20 April 2009, 2133–2147, http://dstath.users.uth.gr/papers/IJRS2009_Stathakis.pdf

TensorFlow Playground, Accessed May 10, 2018, http://playground.tensorflow.org