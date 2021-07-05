def Predict(classifier, X_test, y_test):
    '''
    This function makes classification predictions (from the classifier 'classifier') of the data set's 
    testing set (X_test) and stores it into the global variable y_pred. Moreover, it prints a table of 
    the first 10 observations' Actual vs. Predicted outcomes.
    '''
    global y_pred
    y_pred = classifier.predict(X_test)
    
    print('First 10 Actual vs. Predicted:')
    print()
    print('Observation # \t Actual \t Predicted')
    for i in range(10):
        print(f"{i+1} \t\t {y_test[i]} \t\t {y_pred[i]}")


def ConfusionMatrixAndAccuracy(y_test):
    '''
    This function creates a confusion matrix using the 'y_pred' variable created using the Predict() function,
    and the dependent variable's testing set array. Moreover, it prints the R^2 value, the number of false 
    positives, and the number of false negatives made.
    '''
    from sklearn.metrics import confusion_matrix, accuracy_score

    cm = confusion_matrix(y_test, y_pred)

    print(f"""
    Confusion Matrix
             Predicted 0 Predicted 1
    Actual 0     {cm[0][0]}          {cm[0][1]}
    Actual 1     {cm[1][0]}          {cm[1][1]}
    """)

    R_squared = accuracy_score(y_test, y_pred)
    print("R-squared: %.2f" % (R_squared*100) + "%")
    FalsePositives = cm[0][1]
    print("Number of false positives:", FalsePositives)
    FalseNegatives = cm[1][0]
    print("Number of false positives:", FalseNegatives)

