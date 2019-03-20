import pygame as py
import math
from random import randint
py.init()

w = 1500
h = 800
size = 100
r = (size-15)//2
cols = w//size
rows = h//size
angle = 0
black = (0, 0, 0)
white = (255, 255, 255)

screen = py.display.set_mode([w,h])
screen2 = py.Surface([w,h])

clock = py.time.Clock()

pointsX, pointsY = [], []

colors = []
for i in range(cols*rows):
  colors.append((randint(100,255),randint(100,255),randint(100,255)))

game = True
while game:
  for event in py.event.get():
    if event.type == py.QUIT:
      game = False

  if angle <= -(2*math.pi):
    screen2.fill(black)
    angle = 0
    img = screen.copy()
    py.image.save(img, 'Lissajous.png')
  screen.fill(black)
  screen.blit(screen2, (0, 0))

  for i in range(cols):
    cx = int(size + i * size + size / 2)
    cy = size//2
    py.draw.circle(screen, white, (cx, cy), r, 1)
    x = int(r * math.cos(angle * (i + 1) - math.pi / 2))
    y = int(r * math.sin(angle * (i + 1) - math.pi / 2))
    py.draw.circle(screen, white, (cx + x, cy + y), 4, 4)
    py.draw.line(screen, (112,128,144), (cx + x, cy + y + 4), (cx + x, h), 1)
    pointsX.append([cx+x,cy+y])
  for i in range(rows):
    cy = int(size + i * size + size / 2)
    cx = size//2
    py.draw.circle(screen, white, (cx, cy), r, 1)
    x = int(r * math.cos(angle * (i + 1) - math.pi / 2))
    y = int(r * math.sin(angle * (i + 1) - math.pi / 2))
    py.draw.circle(screen, white, (cx + x, cy + y), 4, 4)
    py.draw.line(screen, (112,128,144), (cx + x + 4, cy + y), (w, cy + y), 1)
    pointsY.append([cx+x,cy+y])

  index = 0
  for i in range(cols):
    for j in range(rows):
      py.draw.circle(screen2, colors[index], (pointsX[i][0],pointsY[j][1]), 1)
      py.draw.circle(screen, white, (pointsX[i][0],pointsY[j][1]), 4)
      index += 1

  angle -= 0.002
  pointsX.clear()
  pointsY.clear()
  py.display.update()

py.quit()