import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'English', 'Science', 'Computer']
marks = [75, 60, 85, 90]

# Pie Chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)

# Title
plt.title("Marks Distribution")

# Show chart
plt.show()
