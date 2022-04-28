import os


def cleanup_images():
    os.system('docker rmi $(docker images -q) -f')
