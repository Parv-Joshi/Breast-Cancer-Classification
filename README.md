# Breast Cancer Classification Project
This is Logistic Regression classification project using the famous [UCI Breast Cancer Wisconsin (Original) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29).
The data was in a .DATA file, which is also a part of this repository. The data description can also be found in the source website.

This project aimed to compare the different classification models and find which type of classification method provided the best accuracy, and best suits the data set. The types of classification used are: logistic regression, k-nearest neighbors, support vector regression, kernal svm, decision tree regression, and random forest regression.
This project includes data preprocessing, basic visualization, splitting the dataset into training and testing data to overcome overfitting, feature scaling, creating several classification models, and comparing the accuracy of all models.

## Data Description

These are the attributes and their scales:

1. Sample code number: id number
2. Clump Thickness: 1 - 10
3. Uniformity of Cell Size: 1 - 10
4. Uniformity of Cell Shape: 1 - 10
5. Marginal Adhesion: 1 - 10
6. Single Epithelial Cell Size: 1 - 10
7. Bare Nuclei: 1 - 10
8. Bland Chromatin: 1 - 10
9. Normal Nucleoli: 1 - 10
10. Mitoses: 1 - 10
11. Class: (2 for benign, 4 for malignant)

## Required Packages

This project uses Python's famous [Scikit-Learn](https://scikit-learn.org/stable/) machine learning package, alongwith [Pandas](https://pandas.pydata.org/),
[NumPy](https://numpy.org/), [MatplotLib](https://matplotlib.org/), [GraphViz](https://pypi.org/project/graphviz/) and [MissingNo](https://pypi.org/project/missingno/). It also uses the packages [warnings](https://docs.python.org/3/library/warnings.html) to hide extra warnings and [MatplotLib's ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html) for better graphs. For who do not have these installed, 
execute the following lines in your terminal:

```
pip install missingno
pip install matplotlib
pip install numpy
pip install pandas
pip install scikit-learn
pip install warnings
pip install graphviz
```

## Citations

According to the UCI Machine Learning website, publishing any material based on databases obtained from this repository requires acknowledgement, and a note of assistance received by using the repository, if any, so that it helps others to obtain the same data sets and replicate the experiments. For this dataset, two papers are required to be cited. The following are:


*Wolberg, W.H., & Mangasarian, O.L. (1990). Multisurface method of pattern separation for medical diagnosis applied to breast cytology. In Proceedings of the National Academy of Sciences, 87, 9193--9196. [Web Link](http://rexa.info/paper/781d2581b297dad058cf6f1be2a009144b5306fb)*

*Zhang, J. (1992). Selecting typical instances in instance-based learning. In Proceedings of the Ninth International Machine Learning Conference (pp. 470--479). Aberdeen, Scotland: Morgan Kaufmann. [Web Link](http://rexa.info/paper/8530b076d4e5d17b52264686e9d23ef329eb33ee)*
