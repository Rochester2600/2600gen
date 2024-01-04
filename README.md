# 2600gen
Generate images and blog post updates for Rochester 2600 website

python ./image.py {path to overlay image} name of image

python ./blog.py

sEE ALSO: https://stackoverflow.com/questions/41959355/how-can-i-combine-these-commands-to-achieve-circular-crop-in-imagemagick

0009  convert checkbox.png -resize 400 giraffe.png
10010  convert giraffe.png -resize 400 giraffe.png
10013  convert -h
10014  convert giraffe.png \\n        -gravity Center \\n        \( -size 200x200 \\n           xc:Black \\n           -fill White \\n           -draw 'circle 100 100 100 1' \\n           -alpha Copy \\n        \) -compose CopyOpacity -composite \\n        -trim output.png
10017  convert giraffe.png \\n        -gravity Center \\n        \( -size 200x200 \\n           xc:Black \\n           -fill White \\n           -draw 'circle 400 400 400 1' \\n           -alpha Copy \\n        \) -compose CopyOpacity -composite \\n        -trim output.png
10020  convert giraffe.png \\n        -gravity Center \\n        \( -size 400x400 \\n           xc:Black \\n           -fill White \\n           -draw 'circle 100 100 100 1' \\n           -alpha Copy \\n        \) -compose CopyOpacity -composite \\n        -trim output.png
10024  convert -size 200x200 xc:Black -fill White -draw 'circle 100 100 100 1' -alpha Copy mask.png\n
10026  convert -size 400x400 xc:Black -fill White -draw 'circle 400 400 100 1' -alpha Copy mask.png\n
10028  convert -size 400x400 xc:Black -fill White -draw 'circle 400 100 100 1' -alpha Copy mask.png\n
10030  convert -size 400x400 xc:Black -fill White -draw 'circle 100 100 100 1' -alpha Copy mask.png\n
10032  convert giraffe.png \( +clone -threshold 101% -fill white -draw 'circle %[fx:int(w/2)],%[fx:int(h/2)] %[fx:int(w/2)],%[fx:80+int(h/2)]' \) -channel-fx '| gray=>alpha'   circle.png\n
10033  man convert
10034  convert -size 400x400 xc:Black -fill White -draw 'circle 200,200 200,1' -alpha Copy mask.png\n
10044  convert -size 600x600 xc:Black -fill White -draw 'circle 300,300 300,1' -alpha Copy mask.png\n
10048  convert giraffe.png -gravity Center mask.png -compose CopyOpacity -composite -trim giraffe_output.png\n
10053  convert giraffe.png -resize 600 giraffe.png
10080  convert giraffe.jpg -resize 600 giraffe.png
10082  convert giraffe.png -gravity Center mask.png -compose CopyOpacity -composite -trim giraffe_output2.png\n

