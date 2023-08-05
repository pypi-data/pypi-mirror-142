import numpy as np

def accuracy(targets, outputs):
    accuracy = 1e-10
    outputs = np.array(outputs)
    if outputs.shape[1] > 1:
        for i in range(outputs.shape[0]):
            outputs[i][np.argmax(outputs[i], axis=0)] = 1.0
    for i in range(outputs.shape[1]):
        if i+2 > outputs.shape[1]:
            accuracy = np.array(np.sum(np.around(outputs[:,i]) == targets[:,i]) / len(targets[:,i]))
            return accuracy
        else:
            accuracy = np.array(np.sum(np.around(outputs[:,i]) == targets[:,i]) / len(targets[:,i])) * np.array(np.sum(np.around(outputs[:,i+1]) == targets[:,i+1]) / len(targets[:,i+1]))