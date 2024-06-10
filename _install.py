"""
Installs the plugin to Dragonfly
"""

import os
import shutil

PLUGIN_NAME = "AnnotationUnion_924df9cb243f11efad78f83441a96bd5"


def main():
    # If the OS is not Windows
    if os.name != "nt":
        print("This script is only for Windows. Please install manually")
        return

    """
    Install locations for my system:
    Local user: C:/Users/myUser/AppData/Local/ORS/Dragonfly2024.1/pythonUserExtensions/Plugins
    All users: C:/ProgramData/ORS/Dragonfly2024.1/pythonAllUsersExtensions/Plugins
    
    Up to Dragonfly2024.1 will be called "base path". After that, it will be called "version path"
    """

    # Base path
    install_all_users = ""
    while install_all_users.lower() not in ("y", "n"):
        install_all_users = input("Install the plugin for all users? (y/n): ")

    install_all_users_bool = install_all_users.lower() == "y"

    if install_all_users_bool:
        base_path = "C:/ProgramData/ORS/"
    else:
        base_path = f"C:/Users/{os.getlogin()}/AppData/Local/ORS/"

    # Version path
    versions = os.listdir(base_path)

    # Filter versions that don't begin in "Dragonfly" (case-sensitive)
    versions = [version for version in versions if version.startswith("Dragonfly")]
    versions.sort(reverse=True)  # Sort versions by Z to A since the latest version is the most likely be first

    if not versions:
        print("No Dragonfly versions found. Please install manually")
        return

    print("\nSelect the Dragonfly version:")
    for i, version in enumerate(versions, 1):
        print(f"{i}. {version}")

    version_index = -1
    while version_index < 1 or version_index > len(versions):
        try:
            version_index = int(input("Enter the number of the version: "))
        except ValueError:
            pass

    if install_all_users_bool:
        install_path = os.path.join(base_path, versions[version_index - 1], "pythonAllUsersExtensions/Plugins")
    else:
        install_path = os.path.join(base_path, versions[version_index - 1], "pythonUserExtensions/Plugins")

    # Delete previous plugin folder if it exists
    plugin_path = os.path.join(install_path, PLUGIN_NAME)

    if os.path.exists(plugin_path):
        shutil.rmtree(plugin_path)

    # Copy the plugin folder
    shutil.copytree(".", plugin_path)

    print("\nPlugin installed successfully. Restart Dragonfly to see the changes.")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
