import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


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

# # Sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
#
# # green dashes, blue squares and red triangles
# plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
# plt.grid(linestyle='-', linewidth='5', color='blue')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()


# x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
# plt.bar(x_pos, popularity, color='blue')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# plt.xticks(x_pos, x)
# # Turn on the grid
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# # Customize the minor grid
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()

# x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
# plt.barh(x_pos, popularity, color='green')
# plt.xlabel("Popularity")
# plt.ylabel("Languages")
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# plt.yticks(x_pos, x)
# # Turn on the grid
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# # Customize the minor grid
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()


# x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(x)]
#
# plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
#
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# plt.xticks(x_pos, x)
# # Turn on the grid
# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# # Customize the minor grid
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.show()

# languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
# popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# #colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
# colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# # explode 1st slice
# explode = (0.1, 0, 0, 0, 0, 0)
# # Plot
# plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=140)
# plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
# plt.show()


# Tips database is the record of the tip given by the customers in a restaurant for two and a half months in the
# early 1990s. It contains 6 columns such as total_bill, tip, sex, smoker, day, time, size.


# reading the database
# data = pd.read_csv("tips.csv")
# pdata = pd.read_csv("penguins.csv")
# # Scatter plot with day against tip
# plt.scatter(data['day'], data['tip'], c=data['size'],
#             s=data['total_bill'])
#
# # Adding Title to the Plot
# plt.title("Scatter Plot")
#
# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')
#
# plt.colorbar()
#
# plt.show()

# plt.bar(data['day'], data['tip'])
#
# plt.title("Bar Chart")
#
# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')
#
# # Adding the legends
# plt.show()

# plt.hist(data['total_bill'])
#
# plt.title("Histogram")
#
# # Adding the legends
# plt.show()

# plt.plot(data['tip'])
# plt.plot(data['size'])
#
# # Adding Title to the Plot
# plt.title("Scatter Plot")
#
# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')
#
# plt.show()

# smokers database using seaborn

# sns.scatterplot(x="total_bill", y="tip", data=data, hue="size", palette="ch:r=-.65,l=.5", size="size", sizes=(15, 200))
# sns.lineplot(x="total_bill", y="tip", data=data, hue="size", palette="ch:r=-.65,l=.5")
# sns.lineplot(x='day', y='tip', data=data)

# sns.lineplot(data=data.drop(['total_bill'], axis=1))
# sns.barplot(x='day',y='tip', data=data, hue='size')
# sns.barplot(x='day',y='tip', data=data, hue='tip')
#  totalbill=data.total_bill+ data.tip
# sns.barplot(x='total_bill',y='tip', data=data, hue='day')

# print(totalbill)
# plt.title('Total bill vs tip ')
# sns.set_theme(style="ticks")

# df = sns.load_dataset("penguins")
# a = sns.pairplot(df, hue="species")
# plt.show()

