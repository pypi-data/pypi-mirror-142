# benfordslaw

[![Python](https://img.shields.io/pypi/pyversions/benfordslaw)](https://img.shields.io/pypi/pyversions/benfordslaw)
[![PyPI Version](https://img.shields.io/pypi/v/benfordslaw)](https://pypi.org/project/benfordslaw/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/benfordslaw/blob/master/LICENSE)
[![BuyMeCoffee](https://img.shields.io/badge/buymeacoffee-grey.svg)](https://www.buymeacoffee.com/erdogant)
[![Github Forks](https://img.shields.io/github/forks/erdogant/benfordslaw.svg)](https://github.com/erdogant/benfordslaw/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/benfordslaw.svg)](https://github.com/erdogant/benfordslaw/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/benfordslaw/month)](https://pepy.tech/project/benfordslaw/month)
[![Downloads](https://pepy.tech/badge/benfordslaw)](https://pepy.tech/project/benfordslaw)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/erdogant/benfordslaw/blob/master/notebooks/benfordslaw.ipynb)
[![DOI](https://zenodo.org/badge/239205250.svg)](https://zenodo.org/badge/latestdoi/239205250)

<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``benfordslaw`` is Python package to test if an empirical (observed) distribution differs significantly from a theoretical (expected, Benfords) distribution. The law states that in many naturally occurring collections of numbers, the leading significant digit is likely to be small. This method can be used if you want to test whether your set of numbers may be artificial (or manipulated). If a certain set of values follows Benford's Law then model's for the corresponding predicted values should also follow Benford's Law. Normal data (Unmanipulated) does trend with Benford's Law, whereas Manipulated or fraudulent data does not.

* Assumptions of the data:
  1. The numbers need to be random and not assigned, with no imposed minimums or maximums.
  2. The numbers should cover several orders of magnitude
  3. Dataset should preferably cover at least 1000 samples. Though Benford's law has been shown to hold true for datasets containing as few as 50 numbers.


### Installation
* Install ``benfordslaw`` from PyPI (recommended). benfordslaw is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

#### Installation
```
pip install benfordslaw
```

* Alternatively, install benfordslaw from the GitHub source:
```bash
git clone https://github.com/erdogant/benfordslaw.git
cd benfordslaw
pip install -U .
```  

#### Import benfordslaw package
```python
from benfordslaw import benfordslaw

# Initialize
bl = benfordslaw(alpha=0.05)

# Load elections example
df = bl.import_example(data='USA')

# Extract election information.
X = df['votes'].loc[df['candidate']=='Donald Trump'].values

# Print
print(X)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
results = bl.fit(X)

# Plot
bl.plot(title='Donald Trump')
```
<p align="center">
  <img src="https://github.com/erdogant/benfordslaw/blob/master/docs/figs/fig1.png" width="600" />
</p>


#### Analyze second digit-distribution

```python
from benfordslaw import benfordslaw

# Initialize and set to analyze the second digit postion
bl = benfordslaw(pos=2)
# USA example
df = bl.import_example(data='USA')
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

```


#### Analyze last digit-distribution

```python
from benfordslaw import benfordslaw

# Initialize and set to analyze the last postion
bl = benfordslaw(pos=-1)
# USA example
df = bl.import_example(data='USA')
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

```

#### Analyze second last digit-distribution

```python
from benfordslaw import benfordslaw

# Initialize and set to analyze the last postion
bl = benfordslaw(pos=-2)
# USA example
df = bl.import_example(data='USA')
results = bl.fit(X)
# Plot
bl.plot(title='Donald Trump', barcolor=[0.5, 0.5, 0.5], fontsize=12, barwidth=0.4)

```

#### References
* https://en.wikipedia.org/wiki/Benford%27s_law
* https://towardsdatascience.com/frawd-detection-using-benfords-law-python-code-9db8db474cf8

#### Citation
Please cite in your publications if this is useful for your research (see citation).
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
