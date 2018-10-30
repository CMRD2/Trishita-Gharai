import matplotlib.pyplot as plt 
#x-coordinate
left=[1,2,3,4,5]
#height for bars
height=[12,24,36,48,60]
#labels for bars
tick=['1','2','3','4','5']
#plotting a bar chart
plt.bar(left,height, tick_label=tick,width=0.8,color=['purple','pink'])
#naming x axis
plt.xlabel("x axis")
#naming y axis
plt.ylabel("y axis")
plt.title('Bar graph ^_^')
plt.show()