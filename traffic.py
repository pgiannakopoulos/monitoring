import os, random
import numpy as np
import math
from numpy import random
import time
import matplotlib.pyplot as plt

# generate traffic distribution
def linear(x, l):
	y = l*x + 1
	return int(y)

# made requests
def get(n, url):
	cmd = 'ab -c 1 -n '+str(n)+' '+ url
	os.popen(cmd)

#show traffic plot
def plot(requests):
	plt.plot(requests)
	plt.title('Traffic')
	plt.xlabel('samples')
	plt.ylabel('number of requests')
	plt.savefig('img/traffic.png')


samples = 100
requests = []
urls = ['http://localhost:8080/bin/view/Dashboard/',
'http://localhost:8080/bin/view/Main/',
'http://localhost:8080/bin/view/Help/',
'http://localhost:8080/bin/view/Menu/',
'http://localhost:8080/bin/view/Sandbox/',
'http://localhost:8080/bin/view/Help/Macros/',
'http://localhost:8080/bin/view/Help/Templates/']


for t in range(1,samples):
	index = random.randint(0, len(urls)-1)
	url = urls[index]
	n = linear(t, 1.1)
	requests.append(n)

	print(n, url)
	time.sleep(5)
	get(n,url)

plot(requests)