import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

dists = importlib_metadata.distributions()
# with open('requirements.txt', 'w') as f:
    for i in dists:
        name = i.metadata["Name"]
        version = i.version
        # f.write(f'{name}=={version}')
        # f.write('\n')