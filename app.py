from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import yt_dlp
import os
from moviepy import AudioFileClip
import re

app = Flask(__name__)
app.secret_key = "mAnICKmacHORkHanarcLOtrEGIbleSioPhySPaNtRAnIeLtyrA"

# Definindo os diretórios para download e conversão
DOWNLOAD_FOLDER = "downloads"
CONVERTED_FOLDER = "converted"

# Função para garantir que as pastas existam
def create_folders():
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Chama a função para criar as pastas ao iniciar a aplicação
create_folders()

def download_video_or_audio(url, format_type):
    try:
        if format_type == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            }
        elif format_type == 'mp4':
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            }
        else:
            raise ValueError("Formato inválido. Escolha 'mp3' ou 'mp4'.")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
            return file_path
    except Exception as e:
        return f"Erro durante o download: {e}"

def convert_to_mp3(input_path, output_folder):
    try:
        video = AudioFileClip(input_path)
        output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".mp3")
        video.write_audiofile(output_path)
        return output_path
    except Exception as e:
        return f"Erro durante a conversão para MP3: {e}"

def is_youtube_url(url):
    """Verifica se a URL é de um vídeo ou playlist do YouTube."""
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
    )
    return youtube_regex.match(url) is not None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        format_type = request.form.get("format")

        if not url or format_type not in ['mp3', 'mp4']:
            flash("Por favor, insira uma URL válida e escolha um formato válido.")
            return redirect(url_for("index"))

        if not is_youtube_url(url):
            flash("A URL fornecida não é válida para o YouTube. Tente novamente.")
            return redirect(url_for("index"))

        # Download do vídeo ou áudio
        file_path = download_video_or_audio(url, format_type)
        if "Erro" in file_path:
            flash(file_path)
            return redirect(url_for("index"))

        # Se o formato for MP3 e o arquivo baixado não for MP3, converte
        if format_type == "mp3" and file_path.endswith('.webm'):
            converted_path = convert_to_mp3(file_path, CONVERTED_FOLDER)
        else:
            converted_path = file_path

        if "Erro" in converted_path:
            flash(converted_path)
            return redirect(url_for("index"))

        # Redirecionar para a rota de download
        return redirect(url_for("download_file", file_path=converted_path))

    return render_template("index.html")

@app.route("/download")
def download_file():
    file_path = request.args.get("file_path")
    if not os.path.exists(file_path):
        flash("Arquivo não encontrado.")
        return redirect(url_for("index"))
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
