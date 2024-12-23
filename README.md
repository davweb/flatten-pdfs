# flatten-pdfs
Flatten multiple PDFs into one.

## How to Use
1. Set up a python virtual environment with:

    ```
    python -m venv --prompt flatten-pdfs .venv
    ```

2. Source the virtual environment with:

    ```
    source .venv/bin/activate
    ```

3. Install required packages using `pip`:

    ```
    pip install --upgrade pip pip-tools
    pip-compile requirements.in
    pip-sync
    ```

6. Run the script with:

    ```
    python flatten_pdfs.py one.pdf two.pdf three.pdf > out.pdf
    ```
