import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo 

def f(X) :
    '''given scalar X, return some value (a real number). '''
    Y = (X - 1.5)**2 + 0.5
    print 'X = {}, Y = {}'.format(X,Y) # for tracing 
    return Y

def error(line,data):
    '''Compute error between givn linear model and observed data. 
    
    Parameters
    -----------
    line : tuple/list/array ( C0,C1) where C0 is slope and C1 is Y-interecept
    data: 2D array where each row is a point (x,y) 
    
    Returns error as a single real value. 
    '''
    
    # Metric: Sum of Squared y-axis differences 
    err= np.sum((data[:,1] -(line[0]*data[:,0] + line[1])) **2)
    return err 

def error_poly(C,data):
    '''Compute error between given polynomial and observd data. 
    
    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point in (x,y) 
    
    Returns error as a single real value. '''
    
    err = np.sum((data[:,1]-np.polyval(C,data[:,0]))**2 )
    return err

def fit_line(data, error_func):
    ''' Fit a line to given data, using a supplied error function. 
    Parameters
    ----------
    data: 2D array where each row is a point (X0,Y)
    error_func: function that computes the error between a line and observed data
    
    Returns a line that minimizes the error function 
    '''
    
    # Generate initial guess for line model 
    line = np.float32([0,np.mean(data[:,1])]) # slope = 0, intercept = mean(y values) 
     # plot initial guess (optional) 
    x_ends = np.float32([-5,5])
    plt.plot(x_ends, line[0]*x_ends + line[1], 'm--',linewidth = 2.0, label = 'Initial guess')
    
    # call optimizer to minimize error function
    result = spo.minimize(error_func,line,args = (data,), method = 'SLSQP', options = {'disp':True})
    return result.x
    
def fit_poly(data, error_func, degree = 4):
    '''Fit a polynomial to given data, using supplied error function. 
    Parameters
    ----------
    data: 2D array where each row is a point (X0,Y)
    error_func: function that computes the error between a poynomial and observed data
    
    Returns polynomial that minimizes the error function '''
    
    Cguess = np.poly1d(np.ones(degree + 1, dtype = np.float32))
    print Cguess
    #plot initial guess (optional) 
    x =np.linspace(-5,5,21)
    plt.plot(x, np.polyval(Cguess,x), 'm--', linewidth=2.0, label = 'Initial Guess')
    # Call Optimizer
    result = spo.minimize(error_func,Cguess, args = (data,), method = 'SLSQP', options = {'disp':True} )
    return np.poly1d(result.x)
    
  
    
    

def test_run():
    Xguess = 2.0
    min_result = spo.minimize(f,Xguess,method = 'SLSQP', options = {'disp':True})
    print "Minima found at: "
    print 'X = {}, Y = {}'.format(min_result.x,min_result.fun)
    
    l_orig = np.float32([4,2])
    print "Original Line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])
    x_orig = np.linspace(0,10,21)
    y_orig = l_orig[0]*x_orig + l_orig[1] 
    plt.plot(x_orig,y_orig, 'b--', linewidth = 2.0, label = 'Original Line')
    
    ### Generate Noisy Points 
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, y_orig.shape)
    data = np.asarray([x_orig,y_orig + noise]).T
    fitline = fit_line(data,error)
    plt.plot(data[:,0],data[:,1], 'go', label = 'Data Points')
    plt.plot(data[:,0],fitline[0]*data[:,0]+fitline[1], 'r--', label = 'fitted line')
    plt.legend(loc = 'upper left')
    plt.show()
    print 'Fitted Line: C0 = {}, C1 = {}'.format(fitline[0],fitline[1])
    
    ### Fitting Higher Order Polynomials 
    Cguess = np.poly1d(np.array([1.5,-10, -5,60, 50], dtype = np.float32))
    print Cguess
    x =np.linspace(-5,5,21)
    y = np.polyval(Cguess,x)
    noise = np.random.normal(0, noise_sigma, y.shape)
    print noise
    data =  np.asarray([x,y+ noise]).T
    fitpoly = fit_poly(data,error_poly)
    print fitpoly
    plt.plot(x,y, 'b-', label = 'Original Line Approx')
    plt.plot(data[:,0],data[:,1], 'go', label = 'Data Points')
    plt.plot(data[:,0],np.polyval(fitpoly,data[:,0]), 'r--', label = 'Fitted Line')
    plt.legend(loc = 'upper right')
    plt.show()
    
if __name__ == '__main__':
    test_run()
