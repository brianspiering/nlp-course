#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status
set -x # Exit immediately if a pipeline exits with a non-zero status

# Create environment
conda update -n base conda -y
conda env create --force

# Start environment
source activate nlp

# Update environment (might break stuff. move fast!?)
conda update --all --yes

# Get nlp data
quilt install spiering/shakespeare

# Setup spell checking and other notebook enhancements
git clone https://github.com/Calysto/notebook-extensions.git
cd notebook-extensions
jupyter nbextension install calysto --user
jupyter nbextension enable calysto/spell-check/main
jupyter nbextension enable calysto/cell-tools/main
jupyter nbextension enable calysto/annotate/main
rm -r -f notebook-extensions

# Setup RISE (https://github.com/damianavila/RISE) slideshows 
jupyter nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix
