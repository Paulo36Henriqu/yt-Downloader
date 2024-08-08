YouTube Video/Playlist Downloader 🎥🎶
Este script Python utiliza o yt-dlp para baixar vídeos ou playlists do YouTube nos formatos MP3 ou MP4. Ele é fácil de usar e permite especificar o formato de saída, bem como o caminho para salvar o arquivo.

✨ Funcionalidades
📥 Baixar vídeos ou playlists: Baixe qualquer vídeo ou playlist do YouTube.
🎧 Formato de saída: Escolha entre os formatos mp3 ou mp4.
📝 Personalização do nome do arquivo: Defina o caminho de saída ou utilize o nome original do vídeo.
⚙️ Requisitos
Certifique-se de que você tenha os seguintes requisitos instalados:

Python 3.x
yt-dlp
FFmpeg
🔧 Instalação do yt-dlp e FFmpeg
bash
Copiar código
pip install yt-dlp
Para instalar o FFmpeg, siga as instruções no site oficial do FFmpeg.

🚀 Como usar
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/yt-downloader.git
cd yt-downloader
Execute o script:

bash
Copiar código
python download_video_or_playlist.py
Digite a URL do vídeo ou playlist do YouTube e o formato desejado (mp3 ou mp4) quando solicitado.

💡 Exemplo de uso
bash
Copiar código
Digite a URL do vídeo ou playlist do YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Digite o formato desejado (mp3 ou mp4): mp3
⚙️ Personalização
output_path: Você pode definir um caminho de saída personalizado ao chamar a função download_video_or_playlist.
❗ Tratamento de Erros
Se ocorrer algum erro durante o download, uma mensagem de erro será exibida no console.

🤝 Contribuição
Sinta-se à vontade para enviar pull requests e reportar problemas no repositório GitHub.

📝 Licença