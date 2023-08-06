from setuptools import find_packages, setup

with open("docs/pkg_docs.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="budget-constrained-CB",
    version="0.0.0",
    author="Honglei Xie",
    author_email="xhonglei2007@gmail.com",
    description="Constrained Contextual Bandits for Personalized Recommendation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    url="https://github.com/HongleiXie/budgetCB",
    project_urls={
        "Bug Tracker": "https://github.com/HongleiXie/budgetCB/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[],
    extras_require={
        "dev": [
            "black==21.7b0",
            "isort==5.9.3",
            "flake8==3.9.2",
            "flake8-annotations==2.6.2",
            "flake8-colors==0.1.9",
            "pre-commit==2.14.0",
            "pytest==6.2.4",
            "numpy==1.21.0",
            "joblib==1.0.1",
            "scipy>=1.7.3",
            "matplotlib==3.5.1",
            "scikit-learn==1.0.2",
        ]
    },
)
