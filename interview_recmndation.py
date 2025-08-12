# Create a program to check whether will attempt the interview based on offered package
# To check any model we need existing dataset.
# We have to provide training on existing dataset.

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Get the offer package 

offered_pkg = np.array([[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]])

# To get the intrested company for interview

interview_get = np.array([0,0,0,0,1,1,1,1,1,1,1,1,1])

# To create the instance the logistic Regression

model = LogisticRegression()

# To provide the training given dataset

interview_predict = model.fit(offered_pkg,interview_get)

# To predict the student will attempt or not.

student_interview = interview_predict.predict([[int(input("Enter your package:"))]])


# Display the offered

if student_interview[0] == 0:
    print("Sorry not attempt:")
else:
    print("Thanku you are select:")    



