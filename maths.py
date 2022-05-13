import matplotlib.pyplot as plt
import numpy as np

# X = range(1, 50)
# Y = [value * 3 for value in X]
# print("Values of X:")
# print(*range(1,50))
# print("Values of Y (thrice of X):")
# print(Y)
# # Plot lines and/or markers to the Axes.
# plt.plot(X, Y)
# # Set the x axis label of the current axis.
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title
# plt.title('Draw a line.')
# # Display the figure.
# plt.show()

# # x axis values
# x = [1,2,3]
# # y axis values
# y = [2,4,1]
# # Plot lines and/or markers to the Axes.
# plt.plot(x, y)
# # Set the x axis label of the current axis.
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title
# plt.title('Sample graph!')
# # Display a figure.
# plt.show()
# #
# line 1 points
# x1 = [10,20,30]
# y1 = [20,40,10]
# # plotting the line 1 points
# plt.plot(x1, y1, label = "line 1")
# # line 2 points
# x2 = [10,20,30]
# y2 = [40,10,30]
# # plotting the line 2 points
# plt.plot(x2, y2, label = "line 2")
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title of the current axes.
# plt.title('Two or more lines on same plot with suitable legends ')
# # show a legend on the plot
# plt.legend()
# # Display a figure.
# plt.show()
#
# # line 1 points
# x1 = [10,20,30]
# y1 = [20,40,10]
# # line 2 points
# x2 = [10,20,30]
# y2 = [40,10,30]
# # Set the x axis label of the current axis.
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Set a title
# plt.title('Two or more lines with different widths and colors with suitable legends ')
# # Display the figure.
# plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
# plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
# # show a legend on the plot
# plt.legend()
# plt.show()

# # line 1 points
# x1 = [10,20,30]
# y1 = [3,89,65]
# # line 2 points
# x2 = [10,20,30]
# y2 = [40,10,30]
# # Set the x axis label of the current axis.
# plt.xlabel('x - axis')
# # Set the y axis label of the current axis.
# plt.ylabel('y - axis')
# # Plot lines and/or markers to the Axes.
# plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
# plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
# # Set a title
# plt.title("Plot with two or more lines with different styles")
# # show a legend on the plot
# plt.legend()
# # function to show the plot
# plt.show()

# # x axis values
# x = [1,4,5,6,7]
# # y axis values
# y = [2,6,3,6,3]
#
# # plotting the points
# plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
#          marker='o', markerfacecolor='green', markersize=10)
# #Set the y-limits of the current axes.
# plt.ylim(1,8)
# #Set the x-limits of the current axes.
# plt.xlim(1,8)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('Display marker')
# # function to show the plot
# plt.show()
#
# X = range(1, 50)
# Y = [value * 9 for value in X]
# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# # shows the current axis limits values
# print(plt.axis())
# # set new axes limits
# # Limit of x axis 0 to 100
# # Limit of y axis 0 to 200
# plt.axis([0, 100, 0, 200])
# # Display the figure.
# plt.show()
#
# # Sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
#
# # green dashes, blue squares and red triangles
# plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
# plt.show()


