from setuptools import setup

PLUGIN_NAME = "pod"

microlib_name = f"flytekitplugins-{PLUGIN_NAME}"

plugin_requires = [
    "flytekit>=1.3.0b2",
    "kubernetes>=12.0.1",
]

__version__ = "0.0.0+develop"

setup(
    title="Kubernetes Pod",
    title_expanded="Flytekit Kubernetes Pod Plugin",
    name=microlib_name,
    version=__version__,
    author="flyteorg",
    author_email="admin@flyte.org",
    description="Flytekit plugin to support K8s Pod tasks",
    namespace_packages=["flytekitplugins"],
    packages=[f"flytekitplugins.{PLUGIN_NAME}"],
    install_requires=plugin_requires,
    license="apache2",
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
