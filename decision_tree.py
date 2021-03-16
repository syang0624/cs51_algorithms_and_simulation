import matplotlib.pyplot as plt
from sklearn import tree
feature_n=['Temperature', 'WBC Count', 'Headache Severity', 'Cough Severity']
target_n=['Infected', 'Not_Infected']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(dtc,
               feature_names = feature_n, 
               class_names=target_n,
               filled = True,
                rounded = True);
fig.savefig('imagename.png')


# The Code above was adapted from: https://gist.githubusercontent.com/Nikhil-Adithyan/1f5e027d56c6523fe6bc30cde3cec97f/raw/7e71f503dc3446b56a41a07ee6f3fd79fae4aa49/tree_viz.py
# The analyzation of the code is based on the concepts that explained at:
