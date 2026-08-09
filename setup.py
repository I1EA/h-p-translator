from setuptools import setup, find_packages

setup(
    name="h-p-translator",
    version="0.1.0",
    description="Translate H and P codes to human-readable text",
    author="Imane El Ayadi",
    author_email="eai9698@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "h_p_translator": ["data/*.csv"],
    },
    install_requires=["pandas"],
    python_requires=">=3.8",
)