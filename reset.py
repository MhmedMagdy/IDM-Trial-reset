import winreg

def delete_registry_key(key, sub_key):
    try:
        winreg.DeleteKey(key, sub_key)
        print("Successfully deleted registry key:", sub_key)
    except WindowsError:
        print("Error deleting registry key:", sub_key)

delete_registry_key(winreg.HKEY_USERS, "S-1-5-21-4259968870-517522717-3671290877-1001_Classes\\WOW6432Node\\CLSID\\{07999AC3-058B-40BF-984F-69EB1E554CA7}")