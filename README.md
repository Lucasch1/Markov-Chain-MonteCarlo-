# Metropolis-Hastings Sampler

This repository contains a Python implementation of the Metropolis-Hastings algorithm for sampling from a probability distribution. The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method used for generating a sequence of samples from a probability distribution for which direct sampling is difficult.

## Requirements

-   Python 3.x
-   NumPy
-   Matplotlib
-   SciPy

## Usage

Clone this repository to your local machine and ensure you have the required dependencies installed. You can then run the script using Python.
It's recommended to use a virtual environment (venv) to manage dependencies and isolate your project's environment. Create and activate a virtual environment before running the script to avoid conflicts with other projects or system-wide packages.

```bash
python -m venv myenv
source myenv/bin/activate  # On Unix/Linux
myenv\Scripts\activate.bat  # On Windows
pip install -r requirements.txt
python metropolis_hastings.py
```

## Description

The code consists of two main functions:

### 1. `metropolis_hastings(N, s)`

This function implements the Metropolis-Hastings algorithm to generate samples from a probability distribution. It takes two parameters:

-   `N`: The number of samples to generate.
-   `s`: The standard deviation of the proposal distribution.

### 2. `calculate_Rb(N, s, J)`

This function calculates the R value, a measure of convergence, for the generated samples. It takes three parameters:

-   `N`: The number of samples to generate for each chain.
-   `s`: The standard deviation of the proposal distribution.
-   `J`: The number of chains to run.

## Example

The script also includes an example of how to use the Metropolis-Hastings sampler and calculate the R values for different standard deviation values. It generates samples using the Metropolis-Hastings algorithm, plots the histogram and kernel density plot of the samples, calculates the mean and standard deviation of the samples, and plots the R values against different standard deviation values.

## License

This code is licensed under the MIT License. Feel free to use and modify it according to your needs.
