from setuptools import setup

configuration = {
    "name": "MixedTypeANN",
    "version": "0.1.0",
    "description": "Approximate nearest neighbors for mixed type data",
    "keywords": "nearest neighbor, knn, ANN",
    "author": "Robin Chien",
    "author_email": "goodnana1224@gmail.com",
    "packages": ["MixedTypeANN"],
    "install_requires": [
        "scikit-learn >= 0.18",
        "scipy >= 1.0",
    ]
}

setup(**configuration)