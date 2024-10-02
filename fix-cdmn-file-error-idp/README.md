# Fix for missing file '/tmp/idp_temp.txt' encountered with cDMN python package (in Anaconda/Miniconda)

This repository contains a Python script designed to fix a file error encountered while using the [CDMN Python API (v. 2.1.1)](https://pypi.org/project/cdmn/2.1.1/).
Here below the error raised:
```bash
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/idp_temp.txt'
```

For more info, please check out the Stack Overflow discussion: [Error about a missing file when executing the example code of the CDMN Python API](https://stackoverflow.com/questions/76258652/error-about-a-missing-file-when-excecuting-the-example-code-of-the-cdmn-python-m).

## What it does

The script modifies file paths within the API.py file from relative to absolute to resolve issues with incorrect or missing file references that prevent the package from functioning as expected.

The corrections could also be performed manually, but this script automates the process.

## Usage Instructions

Before running the script, ensure that:
- You are using the Python interpreter of the Conda environment in which the cDMN package is installed.

When ready, do the following:
**1. Open the Conda Terminal**: Make sure you are using the Conda environment where the cDMN is installed. You can activate your environment with the following command:
   ```bash
   conda activate your_environment_name
   ```
**3. Navigate to the Script's Directory**: Change directory to the location where you have downloaded the GitHub repository. For example, if you cloned the repository into your home directory, use:
   ```bash
   cd ~/fix-cdmn-file-error-idp
   ```
**4. Run the Script**: Execute the script by running:
   ```bash
   python main.py
   ```

## Disclaimer

This solution has been tested on Windows operating systems using Anaconda and Miniconda environments.

Use under your own responsibility.
