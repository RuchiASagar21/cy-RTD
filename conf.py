import os
import sys

project_root = sys.path[4]
package_path = os.path.join(project_root, 'custom_py_package')
sys.path.insert(0, package_path)

# project_root = os.path.abspath(".")
# sys.path.insert(5, project_root)

# Log the path being added
print(f"Project root added to sys.path: {package_path}")

# Log the entire sys.path to verify
print("Current sys.path:", sys.path)

# Detect if the build is happening on Read the Docs
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# -- Project Information --
project = 'cy-RTD'
author = 'RCH'
release = '0.1'

# -- General Configuration --
extensions = [
    'sphinx.ext.autodoc',        # Automatically include docstrings
    'sphinx.ext.napoleon',       # For Google-style or NumPy-style docstrings
    'sphinx.ext.viewcode',       # Link to source code
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output --
html_theme = 'sphinx_rtd_theme'

# Handle static files: disable on RTD if it raises warnings
html_static_path = [] if on_rtd else ['static']

if not on_rtd:
    print("Running locally. Make sure CODEARTIFACT_URL and AWS credentials are set.")

# Add custom packages to sys.path for testing (if needed)

#custom_package_dir = os.getenv('CUSTOM_PACKAGE_PATH', None)
#if custom_package_dir:
 #   sys.path.insert(0, custom_package_dir)


