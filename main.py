import os
from config import *
from scripts.git_operations import clone_repo, create_branch, commit_changes, push_changes
from scripts.image_operations import create_splash_screen
from scripts.file_operations import ensure_dir_exists, replace_file
from scripts.aws_operations import download_from_s3, upload_to_s3

def main():
    print("starting process...")

    # Garante que o diretório temporário exista
    ensure_dir_exists(LOCAL_TEMP_DIR)

    # Baixa os arquivos necessários do S3
    download_from_s3(ICON_S3_PATH, LOCAL_ICON_PATH)
    download_from_s3(BACKGROUND_S3_PATH, LOCAL_BACKGROUND_PATH)
    download_from_s3(LOGO_BENEFICIOS_S3_PATH, LOCAL_LOGO_PATH)

    local_repo_path = f"./{LOCAL_TEMP_DIR}/{CLIENTE_NAME}-app"
    branch_name = f"{CLIENTE_NAME}-version"

    # Clona o repositório
    clone_repo(REPO_URL, local_repo_path)

    # Navega para o diretório do repositório
    os.chdir(local_repo_path)

    # Cria e muda para a nova branch
    create_branch(branch_name)

    # Cria a splash screen
    create_splash_screen(LOCAL_BACKGROUND_PATH, LOCAL_ICON_PATH, LOCAL_SPLASH_OUTPUT_PATH)

    # Substitui os arquivos no projeto
    replace_file(LOCAL_ICON_PATH, "./assets/icon.png")
    replace_file(LOCAL_SPLASH_OUTPUT_PATH, "./assets/splash.png")
    replace_file(LOCAL_LOGO_PATH, "./src/assets/logo.png")
    replace_file(LOCAL_BACKGROUND_PATH, "./src/assets/background.png")

    # Confirma as mudanças no Git
    commit_changes(f"feat: first customization for {CLIENTE_NAME}")

    # Faz push das mudanças para o repositório
    push_changes(branch_name)

    # Faz upload do splash screen final para o S3
    upload_to_s3(LOCAL_SPLASH_OUTPUT_PATH, f"{CLIENTE_NAME}/splash.png")

    # Limpa arquivos temporários
    os.system(f"rm -rf {LOCAL_TEMP_DIR}")

    print("process completed successfully.")

if __name__ == "__main__":
    main()
