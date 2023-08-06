import pypiplot
# print(pypiplot.__version__)
# print(dir(Pypiplot))
from pypiplot import Pypiplot


# %% Top 10 best repos

pp = Pypiplot(username='erdogant', savepath='D://REPOS/pypiplot/repo_data/')
# Get download statistics
pp.stats()
# Get top 10
repo=pp.results['data'].sum().sort_values()[-10:].index.values
# Get stats for the top10
pp.stats(repo=repo)
# Plot
pp.plot()
#
pp.plot_year()
# 
pp.plot_cal()
# 
path = 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap_full.html'
pp.plot_heatmap(vmin=10, vmax=2000, cmap='interpolateOranges', path=path)


# %% Plot
# Init
pp = Pypiplot(username='erdogant', savepath='D://REPOS/pypiplot/repo_data/')
# Get download statistics
results = pp.stats()

# Store svg on github.io
# path = 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'
path = 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'
path = 'C://temp/pypi_heatmap.html'
pp.plot_year(path=path, vmin=700)
# Store all repo info in github.io
pp.plot(legend=False)


# %%
pp = Pypiplot(username='erdogant')

pp.stats(repo='distfit')
pp.plot_year()
pp.plot(vmin=25)


# %% Update single repo
pp.update(repo=['bnlearn'])
pp.update(repo='bnlearn')

results = pp.stats(repo=['df2onehot','pca'])
results = pp.stats(repo='df2onehot')

# %% Get some stats
results = pp.stats(repo=['df2onehot','pca','bnlearn','ismember','thompson'])
pp.plot(legend=True)

# %%
pp = Pypiplot(username='erdogant')

pp.stats(repo='distfit')
pp.plot_year()
pp.plot(vmin=25)

pp.stats(repo='worldmap')
pp.plot_year()

pp.stats(repo='hnet')
pp.plot_year()

pp.stats(repo='ismember')
pp.plot_year()

pp.stats(repo='flameplot')
pp.plot_year()

pp.stats(repo='pca')
pp.plot_year()

pp.stats()
pp.stats(repo=['df2onehot','clustimage','bnlearn','distfit','pypickle','clusteval','findpeaks', 'kaplanmeier','pca','colourmap'])

pp.results['data'].rolling(window=30).mean().plot(figsize=(15,10))
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Average nr. download based on a rolling window of 30 days')
# pp.results['data'].cumsum().plot()

pp.plot_year(vmin=100)
pp.plot(vmin=25)

pp.results['data'].cumsum().plot()

# %% Plot bnlearn
results = pp.stats(repo='bnlearn')
pp.plot_year()

# %%
pp.update()
results = pp.stats()
pp.plot_year(vmin=700)
pp.plot(vmin=25)

# %% Plot
# Init
pp = Pypiplot(username='erdogant', savepath='D://REPOS/pypiplot/repo_data/')
# Get download statistics
results = pp.stats()

# Store svg on github.io
path = 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap.html'
path = 'C://temp/pypi_heatmap.html'
pp.plot_year(path=path, vmin=700)
# Store all repo info in github.io
path = 'D://REPOS/erdogant.github.io/docs/imagesc/pypi/pypi_heatmap_repos.html'
pp.plot(path=path, vmin=100)

# %%
from pypiplot import Pypiplot
# results = pp.stats()
pp.stats(repo=['df2onehot','clustimage','bnlearn','distfit','pypickle','clusteval','findpeaks', 'kaplanmeier','colourmap'])

pp.plot_cal(method='mean', vmin=100)
pp.plot(method='mean')

# %%
