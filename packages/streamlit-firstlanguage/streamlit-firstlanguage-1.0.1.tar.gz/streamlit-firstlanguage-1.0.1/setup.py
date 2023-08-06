import setuptools

setuptools.setup(
    name="streamlit-firstlanguage",
    version="1.0.1",
    author="Selva",
    author_email="selva@firstlangauge.in",
    description="Streamlit components for FirstLanguage API",
    long_description="Ready to use components to interact with FirstLanguage API",
    long_description_content_type="text/plain",
    url="https://github.com/FirstLanguage/streamlit-firstlanguage",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "firstlanguage-python >= 2.5.0",
        "jsonpickle",
        "pandas >= 1.4.1",
        "st-annotated-text >= 3.0.0"
    ],
)
