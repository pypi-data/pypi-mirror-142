import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml_eis",
    version="0.0.15",
    author="Yuefan Ji",
    author_email="yuefan@uw.edu",
    description="data processing and machine learning model for EIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuefan98/Machine-Learning-on-EIS",
    project_urls={
        "Bug Tracker": "https://github.com/yuefan98/Machine-Learning-on-EIS",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={
        # If any package contains *.txt files, include them:
        "ml_eis": ["data/*.csv"],
        # If any package contains *.csv files, include them:
        "ml_eis": ["data/*.txt"],
	# If any package contains *.csv files, include them:
        "ml_eis": ["data/*.sav"],},
    
    python_requires=">=3.6",
)
