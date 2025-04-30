import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import NormalDist

def between_prob(m, s, low, up):
    plt.figure(figsize=(10, 6))
    x= np.linspace(m-4*s, m+4*s, 100)
    plt.plot(x, stats.norm.pdf(x,m,s), 'r')
    section=np.linspace(low,up,100)
    plt.fill_between(section, stats.norm.pdf(section,m,s))
    prob_ = NormalDist(mu=m, sigma=s).cdf(up) - NormalDist(mu=m, sigma=s).cdf(low)
    print(f"Probability between {low} and {up}: {prob_:.5f}")
    z1 = (low-m)/s
    z2 = (up-m)/s
    print(f"Z-Score for {low}: {z1:.4f}")
    print(f"Z-Score for {up}: {z2:.4f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Normal Distribution')
    plt.grid(True)
    plt.show()
    
def left_tail(m, s, up):
    plt.figure(figsize=(10, 6))
    x= np.linspace(m-4*s, m+4*s, 100)
    plt.plot(x, stats.norm.pdf(x,m,s), 'r')
    section=np.linspace(min(x),up,100)
    plt.fill_between(section, stats.norm.pdf(section,m,s))
    prob_ = NormalDist(mu=m, sigma=s).cdf(up)
    print(f"Probability for {up}: {prob_:.5f}")
    z = (up-m)/s
    print(f"Z-Score for {up}: {z:.4f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Normal Distribution')
    plt.grid(True)
    plt.show()

def right_tail(m, s, low):
    plt.figure(figsize=(10, 6))
    x= np.linspace(m-4*s, m+4*s, 100)
    plt.plot(x, stats.norm.pdf(x,m,s), 'r')
    section=np.linspace(low,max(x),100)
    plt.fill_between(section, stats.norm.pdf(section,m,s))
    prob_ = 1 - NormalDist(mu=m, sigma=s).cdf(low)
    print(f"Probability for {low}: {prob_:.5f}")
    z = (low-m)/s
    print(f"Z-Score for {low}: {z:.4f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Normal Distribution')
    plt.grid(True)
    plt.show()

def both_tails(m, s, low, up):
    plt.figure(figsize=(10, 6))
    x= np.linspace(m-4*s, m+4*s, 100)
    plt.plot(x, stats.norm.pdf(x,m,s), 'r')
    section1=np.linspace(min(x),low,100)
    section2=np.linspace(up,max(x),100)
    plt.fill_between(section1, stats.norm.pdf(section1,m,s))
    plt.fill_between(section2, stats.norm.pdf(section2,m,s), color='tab:blue')
    prob_l = NormalDist(mu=m, sigma=s).cdf(low)
    prob_r = 1 - NormalDist(mu=m, sigma=s).cdf(up)
    prob_ = prob_l + prob_r
    print(f"Probability between {low} and {up}: {prob_:.5f}")
    z1 = (low-m)/s
    z2 = (up-m)/s
    print(f"Z-Score for {low}: {z1:.4f}")
    print(f"Z-Score for {up}: {z2:.4f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Normal Distribution')
    plt.grid(True)
    plt.show()


