import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="client-test-oidc-theo-aduneo",
    version="0.0.6",
    author="Theo Bedouet",
    author_email="theo.bedouet@aduneo.com",
    description="test package Client OIDC Aduneo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["requests", "wheel", "pyopenssl", "jwcrypto", "lxml", "xmlsec"],
    include_package_data=True,
    package_data={'': ['static/*/*'], '': ['conf/*']},
)