# hooks/hook-midlead.py

from PyInstaller.utils.hooks import collect_data_files

def hook(hook_api):
    # The directory containing your assets
    ASSETS_PATH = 'assets'

    # Collect the data files using the collect_data_files function
    datas = collect_data_files(ASSETS_PATH, include_py_files=False)
    return datas
