#simple practice
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Random data generate kar rahe hain (ML type example)
np.random.seed(42)
x = np.random.rand(100) * 10
y = 3 * x + 5 + np.random.randn(100) * 3

# DataFrame bana lete hain
data = pd.DataFrame({
    "Feature": x,
    "Target": y
})

# Seaborn theme set
sns.set_theme(style="darkgrid")

# Regression plot
sns.regplot(data=data, x="Feature", y="Target")

plt.title("Seaborn Professional Regression Plot")
plt.show()

