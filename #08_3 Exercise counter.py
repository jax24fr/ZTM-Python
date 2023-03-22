#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#1 iterate over picture
for row in picture:
  for pixel in row:
#if 0 -> print ''
    if (pixel == 1):
      print('*',end='')
  #if 1 -> print *
    else:
      print(' ',end='')
  print()
