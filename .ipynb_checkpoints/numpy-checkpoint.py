{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "[31.36094675 29.12976442 29.41975607 24.47091413 29.42923554 45.24949877\n",
      " 30.63773833 29.52418516 25.51584102 17.98169078]\n",
      "[31.36094675 29.12976442 29.41975607 29.42923554 45.24949877 30.63773833\n",
      " 29.52418516]\n"
     ]
    }
   ],
   "source": [
    "# Numpy Arrays\n",
    "# These are great alteratives to python lists\n",
    "# The key advantages are that they are fast, easy to work with and give users \n",
    "# an opportunity to perform calculations across entire arrays\n",
    "\n",
    "# Create 2 arrays - Weight and Height\n",
    "height = [1.56, 1.67, 1.82, 1.90, 1.76, 1.34, 1.56, 1.67, 1.83, 1.93]\n",
    "weight = [76.32, 81.24, 97.45, 88.34, 91.16, 81.25, 74.56, 82.34, 85.45, 66.98]\n",
    "\n",
    "# import numpy package\n",
    "import numpy as np\n",
    "\n",
    "# Create both arrays in numpy from height and weight\n",
    "np_height = np.array(height)\n",
    "np_weight = np.array(weight)\n",
    "\n",
    "# type of np_height\n",
    "print(type(np_height))\n",
    "\n",
    "# Element-wise calculations\n",
    "bmi = np_weight / np_height ** 2\n",
    "print(bmi)\n",
    "\n",
    "# Subsetting\n",
    "bmi > 29\n",
    "subset = bmi[bmi > 29]\n",
    "print(subset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
