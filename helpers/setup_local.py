import os

PACKAGES = [
    "git",
    "jq",
    "npm",
    "postgresql",
    "rabbitmq",
    'gh',
    "awscli",
    "terraform",
    "minikube",
    "docker-compose"
    ]

CASKS = [
    "firefox",
    "iterm2",
    "slack",
    "vagrant",
    "virtualbox",
    "visual-studio-code",
    "docker"
]

PYTHON_PACKAGES = [
    "virtualenv",
    "pipreqs"
]


def install_packages():
    """
    installs brew packages and casks, python packages based on items in the lists
    """
    print('instaling brew packages...')
    for package in PACKAGES:
        os.system(f'brew install {package}')
    print('installing brew casks...')
    for package in CASKS:
        os.system(f'brew install --cask {package}')
    print('installing python packages...')
    for package in PYTHON_PACKAGES:
        os.system(f'pip3 install {package}')
