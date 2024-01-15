import matplotlib.pyplot as plt

teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F', 'Team G', 'Team H', 'Team I', 'Team X']
points = [40, 35, 30, 25, 20, 18, 15, 12, 10, 8]  

selected_team = 'Team H'
selected_points = 12 

fig, ax = plt.subplots()
explode = [0.1 if team == selected_team else 0 for team in teams]
ax.pie(points, labels=teams, autopct='%1.1f%%', startangle=90, explode=explode, shadow=True)


ax.set_title('Розподіл очок між командами')

plt.show()
