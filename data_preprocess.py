import pandas as pd
import numpy as np

X = pd.read_csv('emnist-letters-train.csv');
X = np.array(X);

Y_text = pd.read_csv('Y.csv');
Y_text = np.array(Y_text);

X_text=[]
for i in range(0,len(X)):
    X_text+=[np.transpose(X[i,:].reshape(28,28))]
    
X_text = np.array(X_text);

X_text = X_text[:].reshape(len(X_text),28,28,1)
Y_text = np.array(Y_text)
print Y_text.shape

un_label=[];
Y_temp=[];



for label in Y_text:
    if label not in un_label:
        un_label.append(label)

for i in Y_text:
    one_enc = np.zeros(26, dtype=int)
    np.put(one_enc,un_label.index(i),1);
    Y_temp.append(one_enc);

Y_temp=np.transpose(np.array(Y_temp))
