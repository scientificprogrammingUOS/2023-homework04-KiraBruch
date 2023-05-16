import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):

    parameters = [loc, scale, lower_bound, upper_bound]   
    for element in parameters:

        if (not(isinstance(element, int) or not(isinstance(element, float)))):
            raise TypeError ("Parameters must be of type integer or float.")
        
        elif lower_bound >= upper_bound:
            raise ValueError ("The lower bound must be smaller than the upper bound.")
        
        else:
            samples = np.random.normal(loc, scale, 100)
            samples_filtered = []
            for i in samples:
                if i >= lower_bound and i <= upper_bound:
                    samples_filtered.append(i)

            std = np.std(samples_filtered)
            mean = np.mean(samples_filtered)

    return (mean, std)


if __name__ == "__main__":
    pass

