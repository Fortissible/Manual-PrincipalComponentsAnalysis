import numpy as np
import matplotlib.pyplot as plt

# WILDAN FAJRI ALFARABI G64190060
def covariance(arr_input1,arr_input2):
    mean1 = np.mean(arr_input1)
    mean2 = np.mean(arr_input2)
    sum_total = 0
    for (x,y) in zip(arr_input1,arr_input2):
        a = x-mean1
        b = y-mean2
        sum_total += a*b
    return sum_total/(len(arr_input1)-1)

def standarize_mean_subtract(arr_input):
    mean_arr =  np.zeros(np.array(arr_input).shape[0])
    for i in range(len(mean_arr)):
        mean_arr[i] = np.mean(arr_input[i])
    print("\n---------Mean of Array----------\n",mean_arr)
    stdrz_arr = np.zeros((np.array(arr_input).shape[0],np.array(arr_input).shape[1]))
    for i in range(len(stdrz_arr)):
        stdrz_arr[i] = np.array(arr_input[i])-mean_arr[i]
    print("\n---------Mean Subtracted Array----------\n",stdrz_arr)
    return stdrz_arr

def cov_matrix(arr_input):
    cov_mtrx = np.zeros((len(arr_input),len(arr_input)))
    for i in range(len(arr_input)):
        for j in range(len(arr_input)):
            cov_mtrx[i][j] = covariance(arr_input[i],arr_input[j])
    print("\n---------Covariance Matrix of Mean Subtracted Array----------\n",cov_mtrx)
    return cov_mtrx

def eigenvalue(arr_input):
    eig_val,eig_vec = np.linalg.eig(arr_input)
    return eig_val,eig_vec

def reduce_dimension(threshold,eig_val,eig_vec,stdrz_arr):
    #sort eigen value and vector
    if (len(eig_val)>2):
        eig_val = np.flip(eig_val)
        eig_vec = np.flip(eig_vec,axis=1)

    sorted_eig_val = np.append(eig_val[-1:], eig_val[:len(eig_val) - 1])
    sorted_eig_vec = np.append([eig_vec[:,-1]],[eig_vec[:,0]],axis=0)
    for i in range(1,len(eig_vec)-1):
        sorted_eig_vec = np.append(sorted_eig_vec,[eig_vec[:,i]],axis=0)

    print("\n---------Eigen Vector Sorted----------\n",sorted_eig_vec)
    print("\n----------Eigen Value Sorted---------\n", sorted_eig_val)

    reduced_dimension_data = np.matmul(sorted_eig_vec[:threshold],stdrz_arr)

    return reduced_dimension_data

def plot_data(data,dimension):
    fig, ax = plt.subplots(figsize=(10, 10))
    if dimension==2 :
        ax.scatter(data[0], data[1])
        ax.set(xlim=(np.amin(data[0])-1, np.amax(data[0])+1), ylim=(np.amin(data[1])-1, np.amax(data[1])+1), aspect='equal')
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
    elif dimension==1 :
        ax.scatter(data[0], data[0])
        ax.set(xlim=(np.amin(data[0]) - 1, np.amax(data[0]) + 1), ylim=(np.amin(data[0]) - 1, np.amax(data[0]) + 1),
               aspect='equal')
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
    plt.show()
