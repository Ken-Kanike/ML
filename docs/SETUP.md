# Setup and Troubleshooting

## Requirements

- Python 3.10 or newer. The notebooks were tested with Python 3.12.2.
- Git.
- JupyterLab or Jupyter Notebook.
- A terminal (PowerShell on Windows, bash/zsh on macOS or Linux).
- Roughly 1 GB of free disk space for the environment and outputs.

No GPU is required. The notebooks run on a laptop CPU.

## Windows setup

Open PowerShell in the repository folder.

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m jupyterlab
```

If PowerShell blocks the activation script:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again.

If `python` points to the Microsoft Store stub, use the Python launcher:

```powershell
py -3.12 -m venv .venv
```

## macOS and Linux setup

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m jupyterlab
```

## Register the environment as a Jupyter kernel

If Jupyter does not automatically see the environment:

```bash
python -m ipykernel install --user --name ml-course --display-name "Python (ML course)"
```

Select **Python (ML course)** in the kernel menu.

## Run a notebook

Start JupyterLab from the repository root:

```bash
python -m jupyterlab
```

The advanced notebooks are self-contained. Open one and use **Run All**, or run the cells from top to
bottom.

The foundation notebooks read files such as `yahoo_data.xlsx` and `student_data.csv` from the
repository root. Start Jupyter from the root directory so those relative paths resolve.

To execute a notebook from the command line:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=600 \
  Advanced_ML/01_knn_svm/01_knn_svm.ipynb
```

## Verify the environment

```bash
python -c "import numpy, pandas, sklearn, matplotlib, seaborn; print('core packages OK')"
python -c "import statsmodels, imblearn, mlxtend, fastapi, joblib; print('advanced packages OK')"
```

## Troubleshooting

### `ModuleNotFoundError`

The notebook is using a different kernel from the environment where `requirements.txt` was installed.
Check the kernel name in JupyterLab and reinstall inside the active environment:

```bash
python -m pip install -r requirements.txt
python -m ipykernel install --user --name ml-course --display-name "Python (ML course)"
```

### `FileNotFoundError` for a CSV or Excel file

The foundation notebooks use relative paths. Start Jupyter from the repository root, or update the
path in the notebook. Do not commit absolute paths from your machine.

### `jupyter` is not recognized

Use the module form:

```bash
python -m jupyterlab
```

### Excel files fail to open

Install `openpyxl`:

```bash
pip install openpyxl
```

It is included in `requirements.txt`.

### PowerShell activation error

Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### zmq warning about the Proactor event loop

On Windows, notebook execution may print:

```text
RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq
```

This is a harmless warning from the Jupyter kernel transport. Execution continues normally.

### Plots do not display

Ensure the notebook uses `%matplotlib inline` or that the cell ends with `plt.show()`. In JupyterLab,
plots render in the output area. If output is disabled, use **View > Show Output**.

### Slow execution

The advanced notebooks are intentionally small. If a notebook is slow:

- stop other memory-heavy applications;
- reduce `n_estimators`, `n_boot`, or the number of cross-validation folds;
- use a smaller sample in synthetic-data cells;
- restart the kernel to clear memory.

### Kernel dies or runs out of memory

Restart the kernel and run cells one at a time. The deployment and interpretability notebooks use
small data, so memory pressure usually comes from other applications or from repeated large plots.

### Notebook outputs look outdated

Re-run the notebook:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=600 \
  Advanced_ML/01_knn_svm/01_knn_svm.ipynb
```

## Cleaning notebook outputs

If you contribute a notebook, keep executed outputs for learner convenience. If you need a clean copy
for debugging:

```bash
jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True \
  --output cleaned.ipynb Advanced_ML/01_knn_svm/01_knn_svm.ipynb
```

Do not commit the cleaned copy unless the contribution guidelines say otherwise.

## Uninstall

Deactivate the environment and delete the `.venv` folder:

```powershell
deactivate
Remove-Item -Recurse -Force .venv
```

On macOS or Linux:

```bash
deactivate
rm -rf .venv
```
