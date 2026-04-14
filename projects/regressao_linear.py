from sklearn.linear_model import LinearRegression

X = [[10], [20], [30]]  # preço
y = [100, 80, 60]      # popularidade

model = LinearRegression()
model.fit(X, y)

print(model.intercept_)  # β₀
print(model.coef_)       # β₁