#Problem 1: P = 10000 and X = 1

import numpy as np
import matplotlib.pyplot as plt


##experiments prepare
dimension = 2                   #pair 
n_points_per_experiment = 10000 #number of pair/ P=10000
n_experiments = 1               #number of independent experiment/ X=1
points = np.random.uniform(low=-1.0, high=1.0,size=(dimension, n_points_per_experiment,n_experiments, )) #{[(px1,py1),(px2,py2)...(px10000),(py10000)]}

##experiments result calculation
radius = (points**2).sum(axis=0)  #px^2 + py^2
inside_the_circle = (radius <= 1) # how many points in the circle
inside_the_square = ((-1.0 <= points[0]) & (points[0] <= 1.0) &(-1.0 <= points[1]) & (points[1] <= 1.0)) #how many points inside the square
pi_by_4 = inside_the_circle.sum(axis=0) / inside_the_square.sum(axis=0) #ratio 
pi = 4 * pi_by_4


##experiment analysis
average = pi.mean()
uncertainty = pi.std()
average = pi.mean()
uncertainty = pi.std()
print(f'pi ={average} ± {uncertainty}')


#• Compute the mean and standard deviation of the π observable inside this single experiment.
print(f'pi ={average} ± {uncertainty}')
print(f'pi_average = {average}, pi_uncertatinty = {uncertainty}')

#• Plot a histogram of all the radii 
plt.hist(radius**0.5, bins = 25)
plt.show()

#• Plot a histogram of all the squared radii 
plt.hist(radius, bins = 25)
plt.show()

#•Write a few sentences (which may include mathematics) explaining why the histograms have the features they do to the left of 1 and to the right of 1. In particular explain why the behavior differs so dramatically for values less than 1
#For the r**2 histogram, it can be explained from the picture of r. Since any number less than 1 their square will converge to 0.
#From the histogram from HW1-1-2, we can find most of value is less than one. Thus, the histogram HW1-1-3 will have more datas that tend to approach to 0.
#For the r histogram, we can first to analyze the uniform distrubution.
#for 1 D case(10000 elements):
one_D_number_array = np.random.uniform(low=-1.0, high=1.0,size=(1, 10000,1, ))
print(one_D_number_array.mean(axis = 1))      #theoratically approaching to 0
print((one_D_number_array**2).mean(axis = 1)) #approaching to 0.33 
#the meanvalue of all x^2, theoratically we are calculating the "(integration x^2)/(total length)" from -1 to 1
#theoratically the mean value for all x^2 from -1 to +1 is 0.33.

#Then we can find the median value of x^2
print(np.median((one_D_number_array**2),axis = 1)) #my one trial : 0.26089879/
#Check the histogram, most of the datas are in the left side.
plt.hist((one_D_number_array**2)[0], bins = 25) #we find most of datas are approaching to left
plt.show()
#as this statistcal result we will find that most of additions for x^2+y^2 are less than 1
#Thus the square root less than 1, the histogram of r leans to left of 1



#•Plot a histogram of the indicator variable 4[x^2+y^2>=1],. Draw a vertical line at the mean of all the samples, and indicate the mean ± standard deviation with vertical lines. Indicate the true, known value of π for comparison.
plt.hist(pi, bins=25) #bins: the size of histogram bar
plt.axvline(np.pi, color='black', zorder=1, linestyle=':')
plt.axvspan(average-uncertainty, average+uncertainty, alpha=0.25)
plt.show()