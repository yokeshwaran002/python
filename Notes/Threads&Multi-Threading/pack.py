import numpy as np, pandas as pd, matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# NumPy: create data
x = np.linspace(0, 10, 5)
y = np.tan(x)

print(x)
print(y)

# Pandas: create DataFrame
df = pd.DataFrame({'X': x, 'Y': y})
print(df)

# Matplotlib: plot
plt.plot(df['X'], df['Y'], marker='^')
plt.title("Sine Wave")
plt.show() 

# BeautifulSoup: parse HTML
html = "<ul><li>Apple</li><li>Banana</li></ul>"
soup = BeautifulSoup(html, 'html.parser')
print([li.text for li in soup.find_all('li')])

 