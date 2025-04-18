from setuptools import setup, find_packages

setup(
    name="bigdata_actividad1",
    version="0.0.1",
    author="Andres Callejas",
    author_email="",
    description="",
    py_modules=["actividad_1"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "scikit-learn",
        "matplotlib",
        "joblib",
        "python-dotenv",
        "openai==0.28",
        "httpx"
    ]
) 