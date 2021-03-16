from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# split data into training and testing arrays
all_inputs = df[['Temperature', 'WBC Count', 'Headache Severity', 'Cough Severity']].values
all_classes = df[ 'Infected'].values
(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, test_size=0.3,random_state=1)

# grow a tree!!!
depth = 4 # <----- try different depths between 2 and 10
dtc = DecisionTreeClassifier(max_depth=depth)
dtc.fit(train_inputs, train_classes)
print("Training Accuracy score:",dtc.score(train_inputs, train_classes))
print("Test Accuracy score:",dtc.score(test_inputs, test_classes))

#Different Training Accuracy Scores from tree depth 2 to 10:
#2 .957 
#3 .985
#4 1.0 
#5 1.0
#6 1.0
#7 1.0
#8 1.0
#9 1.0
#10 1.0

#For the Tree Depth 4, the training accuracy achieved 1.0. Further depths also provdie 1.0; however, I set the depth as 4 to avoid over-fitting.


#the code above was provided in CS51 Session 5.2 Spring 2021 at Minerva Schools at KGI.

#in order to import the libraries and to understand, I refered the following link
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
