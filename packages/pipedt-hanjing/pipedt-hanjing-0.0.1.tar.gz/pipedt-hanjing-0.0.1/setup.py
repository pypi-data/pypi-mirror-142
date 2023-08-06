import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    desc = f.read()


setuptools.setup(
    name="pipedt-hanjing",
    version="0.0.1",
    author="Hanjing Wang, Mankit",
    description="An unified engine for training and inference for large-scale models",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/VegeWong/PipelineDT",
    project_urls={
        "Bug Tracker": "https://github.com/VegeWong/PipelineDT/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)