To consolidate your MTN and Airtel clients into a single SDK that can be imported from a central location, you should consider packaging your Python code into a distributable format. This allows you to manage your clients as a cohesive unit, making it easier to distribute and use across your company's products. Here's a step-by-step guide based on best practices:

### 1. Organize Your Code

First, organize your MTN and Airtel clients into separate modules within a package. Typically, this involves creating a directory structure that reflects the logical grouping of your modules.

```
my_sdk/
│
├── mtnclient.py
└── airtelclient.py
```

### 2. Create Setup Files

Use `setup.py` or `pyproject.toml` (for newer projects) to define your package metadata and dependencies. This file tells Python about your package, its contents, and any external libraries it depends on.

#### Using `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="my_sdk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="My Company's SDK for MTN and Airtel Clients",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="http://github.com/mycompany/my_sdk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
```

#### Using `pyproject.toml`:

For newer projects, `pyproject.toml` is recommended for defining build system requirements and dependencies.

```toml
[tool.poetry]
name = "my_sdk"
version = "0.1.0"
description = "My Company's SDK for MTN and Airtel Clients"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 3. Build and Distribute Your Package

After organizing your code and setting up your package metadata, you can build your package. If you're using `setuptools`, run:

```bash
python setup.py sdist bdist_wheel
```

For `poetry`, simply run:

```bash
poetry build
```

This command generates a `.tar.gz` file (source distribution) and a `.whl` file (wheel distribution) in the `dist/` directory.

### 4. Share Your Package

You can now share your package via PyPI or host it on GitHub and instruct users to install it using pip:

```bash
pip install my_sdk
```

Or, if hosted on GitHub:

```bash
pip install git+https://github.com/mycompany/my_sdk.git
```

### 5. Import in Your Projects

Once installed, you can import your clients in any project:

```python
from my_sdk import mtnclient, airtelclient
```

This approach not only organizes your code neatly but also leverages Python's packaging ecosystem to streamline distribution and installation across your company's products.

Citations:
[1] https://medium.com/@miqui.ferrer/python-packaging-best-practices-4d6da500da5f
[2] https://dagster.io/blog/python-project-best-practices
[3] https://stackoverflow.com/questions/62630756/what-are-the-best-coding-practice-for-creating-python-package
[4] https://packaging.python.org/tutorials/packaging-projects/
[5] https://blog.inedo.com/python/packages-authoring-best-practices/
[6] https://docs.python-guide.org/writing/structure/
[7] https://www.reddit.com/r/learnpython/comments/12ril6t/how_to_level_up_my_python_package_development/
[8] https://www.turing.com/kb/python-packaging
[9] https://www.linkedin.com/pulse/package-development-python-comprehensive-guide-ketan-raval-neu7f
[10] https://www.reddit.com/r/learnpython/comments/skq335/what_are_the_best_practices_for_function_files_in/
