import yt_dlp

def download_video_or_playlist(url, format_type, output_path=None):
    try:
        print("Downloading...")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best' if format_type == 'mp4' else 'bestaudio/best',
            'outtmpl': output_path or '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }] if format_type == 'mp4' else [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)

if __name__ == "__main__":
    url = input("Digite a URL do vídeo ou playlist do YouTube: ")
    format_type = input("Digite o formato desejado (mp3 ou mp4): ").strip().lower()
    
    if format_type not in ['mp3', 'mp4']:
        print("Formato inválido. Escolha 'mp3' ou 'mp4'.")
    else:
        download_video_or_playlist(url, format_type)
