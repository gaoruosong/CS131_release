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
    ## you have to check if a-c-i in range [0,H_i) and b-d-j in range [0,H_j);
    ## so we really want i in range [0,H_k) AND []  a-c >= i > a-c- H_i
    ## so, start is 0 or a-c-h_i+1, whichever larger
    
    ### YOUR CODE HERE

    sum = 0
    mid_height = (Hk-1)/2
    mid_width = (Wk-1)/2
    for a in range(Hi):
        for b in range(Wi):
            sum = 0
            for i in range(max(0, a-Hi-mid_height+1), min(Hk, a-mid_height+1)):
                for j in range(max(0, b-Wi-mid_width+1), min(Wk, b-mid_width+1)):
                    sum += H[i][j] * f[a-i-mid_height][b-j-mid_width]
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
    
    ## so we want to pad the image. We probably want to pad with size Hk, Wk first. 
    ## actually, is this the right padding? let us say we have a filter with size 2a+1, 2b+1.
    ## 
    ## then we may want to flip, and then do something like np.sum().
    ### YOUR CODE HERE

    mid_height = (Hk-1)/2
    mid_width = (Wk-1)/2
    padded_image = zero_pad(image, mid_height, mid_width)
    flipped_kernel = np.flip(kernel)
    for i in range(Hi):
        for j in range(Wi):
            patch = padded_image[i-mid_height:i+mid_height+1][j-mid_width,j+mid_width+1]
            out[i][j] = np.sum(partch * flipped_kernel)
            
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
    out = conv_fast(f, np.flip(g))
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
    
    Hg, Wg = g.shape
    mean = float(np.sum(g)) / float(Hg * Wg)
    out = cross_correlation(f, g - np.full((Hg, Wg), mean))
    
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
    
    normalized_f = (f - np.mean(f)) / np.std(f)
    normalizeg_g = (g - np.mean(g)) / np.std(g)
    out = cross_correlation(normalized_f, normalized_g)
    
    ### END YOUR CODE

    return out
