"""Examples for benfords law."""

# import benfordslaw
# print(benfordslaw.__version__)


# %% Analyze Second digit
from benfordslaw import benfordslaw

bl = benfordslaw(pos=2)
# USA example
df = bl.import_example(data='USA')
Iloc = df['candidate']=='Donald Trump'
X = df['votes'].loc[Iloc].values
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

# %%
import numpy as np
from benfordslaw import benfordslaw
bl = benfordslaw(alpha=0.05, method='chi2')
x = np.linspace(0,1000,1001)
x = np.append(x,[1,1,1,1,1,1,])
isben2 = bl.fit(x)

print(f"isben2 {isben2}")
print(f"P_significant: {isben2['P_significant']}")
if not isben2['P_significant']:
    print("sorry, nope.")

# %% USA example
from benfordslaw import benfordslaw

bl = benfordslaw(pos=1)

# USA example
df = bl.import_example(data='USA')

# Get data for candidate
Iloc = df['candidate']=='Donald Trump'
X = df['votes'].loc[Iloc].values

# Fit
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)


# %% Analyze last digit

bl = benfordslaw(pos=-1)
# USA example
df = bl.import_example(data='USA')
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

# %% second last digit

bl = benfordslaw(pos=-2)
# USA example
df = bl.import_example(data='USA')
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

# %% RUS
df = bl.import_example('RUS')
candidates=['Putin Vladimir Vladimirovich', 'Baburin Sergei Nikolaevich', 'Titov Boris Yurievich', 'Yavlinskiy Gregory Alekseivich']

for candidate in candidates:
    bl = benfordslaw(method='ks')
    bl.fit(df[candidate].values)
    bl.plot(title=candidate)

# %% USA
df = bl.import_example('USA')
for candidate in df['candidate'].unique():
    Iloc = df['candidate']==candidate
    X = df['votes'].loc[Iloc].values
    bl.fit(X)
    bl.plot(title=candidate)
