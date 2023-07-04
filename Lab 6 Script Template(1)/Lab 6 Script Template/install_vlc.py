import requests
import hashlib
import os
import subprocess


def main():
  

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    
    
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/'
    resp_msg = requests.get(file_url)
    file_content = resp_msg.text

    sha = file_content.split()[10]
    print(sha[10])



    
    # Hint: See example code in lab instructions entitled "Extracting Text from a Response Message Body"
    # Hint: Use str class methods, str slicing, and/or regex to extract the expected SHA-256 value from the text 
    return 

def download_installer():
   
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/'
    resp_msg = requests.get(file_url)

   
       



    
    return resp_msg.content

def installer_ok(installer_data, expected_sha256):
    
    expected_sha256 = hashlib.sha256(installer_data).hexdigest()
    print(expected_sha256)

    return expected_sha256

def save_installer(installer_data):
    """Saves the VLC installer to a local directory.

    Args:
        installer_data (bytes): VLC installer file binary data

    Returns:
        str: Full path of the saved VLC installer file
    """
    # TODO: Step 4
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"
    
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/'
    resp_msg = requests.get(file_url)
    installer_data = resp_msg
    folderos = os.getenv('temp')
    with open (folderos , 'wb') as file:
        installer_data(folderos)





    return

def run_installer(installer_path):
    """Silently runs the VLC installer.

    Args:
        installer_path (str): Full path of the VLC installer file
    """    
    # TODO: Step 5
    
    installer_path = r'C:\temp\os.getenv', 'wb'
    subprocess.run ([installer_path, '/L=1033', '/S'])





    # Hint: See example code in lab instructions entitled "Running the VLC Installer"
    return
    
def delete_installer(installer_path):
    os.remove(installer_path)



    
   
    return

if __name__ == '__main__':
    main()