"""
CS131 - Computer Vision: Foundations and Applications
Project 2 Option A
Author: Donsuk Lee (donlee90@stanford.edu)
Date created: 07/2017
Last modified: 2/5/2024
Python Version: 3.5+
"""

import numpy as np


def conv_nested(image, kernel):
    """A naive implementation of convolution filter.

    This is a naive implementation of convolution using 4 nested for-loops.
    This function computes convolution of an image with a kernel and outputs
    the result that has the same shape as the input image.

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))


    ## recall that the point is you take the sum \sum_{i,j} f(a-i,b-j) H(i,j)... f * H. f is image, H is filter... 
    ## f(i,j), i,j should range over Hi, Wi; output, also over H_i, W_i;
    ## real question is the range to sum. Should 
    ## zero-indexed, and odddimensions. How to do this? Well, 
    ## you have to check if a-i in range [0,H_i) and b-j in range [0,H_j);
    ## so we really want i in range [0,H_k) AND []  a >= i > a- H_i
    ## so, start is 0 or a-h_i+1, whichever larger
    
    ### YOUR CODE HERE

    sum = 0
    for a in range(H_i):
        for b in range(W_i):
            sum = 0
            for i in range(max(0, a-H_i+1), min(H_k, a+1)):
                for j in range(max(0, b-W_i+1), min(W_k, b+1)):
                    sum += H[i][j] * f[a-i][b-j]
            out[a][b] = sum

    ### END YOUR CODE

    return out

def zero_pad(image, pad_height, pad_width):
    """ Zero-pad an image.

    Ex: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:

        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]         of shape (3, 5)

    Args:
        image: numpy array of shape (H, W).
        pad_width: width of the zero padding (left and right padding).
        pad_height: height of the zero padding (bottom and top padding).

    Returns:
        out: numpy array of shape (H+2*pad_height, W+2*pad_width).
    """

    H, W = image.shape
    out = None

    ## we look at out[padded_height, padded_width], which is the beginning. It's an offset. 
    ### YOUR CODE HERE
    
    out = np.zeros((H + 2*pad_height, W + 2*pad_width))
    for i in range(H):
        for j in range(W):
            out[i + pad_height][j + pad_width] = image[i][j]
    
    ### END YOUR CODE
    return out


def conv_fast(image, kernel):
    """ An efficient implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Hints:
        - Use the zero_pad function you implemented above
        - There should be two nested for-loops
        - You may find np.flip() and np.sum() useful

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out

def cross_correlation(f, g):
    """ Cross-correlation of image f and template g.

    Hint: use the conv_fast function defined above.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out

def zero_mean_cross_correlation(f, g):
    """ Zero-mean cross-correlation of image f and template g.

    Subtract the mean of g from g so that its mean becomes zero.

    Hint: you should look up useful numpy functions online for calculating the mean.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out

def normalized_cross_correlation(f, g):
    """ Normalized cross-correlation of image f and template g.

    Normalize the subimage of f and the template g at each step
    before computing the weighted sum of the two.

    Hint: you should look up useful numpy functions online for calculating 
          the mean and standard deviation.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out
