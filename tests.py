import matplotlib.pyplot as plotter

# Simple line Graph
x = [0,1,2,3,4]
y = [5,6,7,1,2]
#plotter.plot(x,y)
#plotter.show()

# Simple scatter plot
x1 = [5,6,7,8,9]
y1 = [4.2,4.6,7,6.33,1.2]
#plotter.scatter(x1,y1)
#if you want 2 plots on same graph use plotter.plot() twice or scatter

#Simple Bar Chart
#plotter.bar(x,y,label = 'Bar Chart Test 1', color = 'r')
#plotter.bar(x1,y1,label = 'Bar Chart Test 2', color = 'c')

#Simple Histogram
bins = [0,10,20,30,40,50,60,70,80,90,100]
scores = [80,93,76,82,63,12,45,50,58,68,78,88,92,99,71,70,80,53,36,42,85,75,74]
plotter.hist(scores, bins, histtype = 'bar', rwidth = 0.8)

plotter.xlabel("X axis Label")
plotter.ylabel("Y axis Label")
plotter.title("Plot Title")
plotter.legend()
plotter.show()
