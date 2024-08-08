import os

# Configurações globais e variáveis

# URL do repositório a ser clonado
REPO_URL = "https://github.com/seu-repo/white-label-app.git"

# Nome padrão do cliente (pode ser substituído por entrada do usuário)
CLIENTE_NAME = "grecale"

# Caminhos de arquivos no S3
S3_BUCKET_NAME = "seu-bucket"
ICON_S3_PATH = f"{CLIENTE_NAME}/icon.png"
BACKGROUND_S3_PATH = f"{CLIENTE_NAME}/background.png"
LOGO_BENEFICIOS_S3_PATH = f"{CLIENTE_NAME}/logo.png"

# Caminhos temporários locais para manipulação dos arquivos
LOCAL_TEMP_DIR = "./temp/"
LOCAL_ICON_PATH = os.path.join(LOCAL_TEMP_DIR, "icon.png")
LOCAL_BACKGROUND_PATH = os.path.join(LOCAL_TEMP_DIR, "background.png")
LOCAL_LOGO_PATH = os.path.join(LOCAL_TEMP_DIR, "logo.png")
LOCAL_SPLASH_OUTPUT_PATH = os.path.join(LOCAL_TEMP_DIR, "splash.png")
