import numpy as np
import matplotlib.pyplot as plt

def main(N = 10000):
    plt.figure(figzise=(8,8))
    x,y = np.random.uniform(-1,1,size=(2,N))
    interior = (x**2 + y**2) <=1
    pi = interior.sum()*4/N
    error = abs((pi-np.pi)/pi)*100
    exterior = np.invert(interior)
    plt.plot(x[interior], y[interior], 'b.')
    plt.plot(x[exterior], y[exterior], 'r.')
    plt.plot(0,0,label = '$\hat \pi$ = {:4.4f} \n {:4.4f} error %'.format(pi,error),alpha= 0)
    plt.axis('square')
    plt.legend(frameon = True, framealpha = 0.9,fontsize = 16)
    plt.show()

     
if __name__ == "__main__":
    main(10000)
