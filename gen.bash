https://askubuntu.com/questions/648244/how-do-i-create-an-animated-gif-from-still-images-preferably-with-the-command-l

ffmpeg \
  -framerate 10 \
  -pattern_type glob \
  -i '*.jpg' \
  -r 15 \
  -vf scale=512:-1 \
  out.gif \
;



ffmpeg \
  -framerate 10 \
  -pattern_type glob \
  -i '*.jpg' \
  -vf scale=1024:-1 \
  -b 2000k \
  out.mp4 \
;

