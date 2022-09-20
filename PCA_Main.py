from PrincipalComponentAnalysis import *

# WILDAN FAJRI ALFARABI G64190060
if __name__ == "__main__":
    input_2_var = [
        [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1],
        [2.4, 0.7, 2.9, 2.2, 3, 2.7, 1.6, 1.1, 1.6, 0.9]
    ]

    input_5_var = [
        [2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1],
        [2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9],
        [2.5, 2.1, 6, 2.2, 3, 2, 1.6, 8, 11, 3],
        [1,2,3,4,5,6,7,8,9,10],
        [1.2,3.5,4.5,0.2,0.6,2.5,2.8,9.3,2.6,5.3]
    ]

    standarized_input = standarize_mean_subtract(input_2_var)
    cov_mtrx = cov_matrix(standarized_input)
    eig_val,eig_vec = eigenvalue(cov_mtrx)

    print("\n---------Eigen Value----------\n",eig_val)
    print("\n---------Eigen Vector----------\n",eig_vec)

    #change the eigen value threshold
    eigen_value_threshold = int(input("\npilih threshold eigenvalue tertinggi:\n"))

    new_data = reduce_dimension(eigen_value_threshold,eig_val,eig_vec,standarized_input)

    print("\n----------Reduced Dimension Data---------\n",new_data)

    plot_data(new_data,eigen_value_threshold)

