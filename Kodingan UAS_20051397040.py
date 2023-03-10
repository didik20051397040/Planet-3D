"""

********CONTROLS********
* Tekan PANAH ATAS atau PANAH BAWAH untuk menyesuaikan irisan dan tumpukan bentuk objek .
                [Mengontrol bentuk dari objek]
* A,W,S,D untuk bergerak di sekitar area objek.
* Scroll Mouse untuk zoom in dan out.
* X untuk masuk ke mode X-ray [wireframe mode].
************************

"""

import time
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


# warna dan variabel lain untuk memudahkan modifikasi
planetColor = (0.0, 0.6, 0.7)
partialDiskColor=(0.7, 0.4, 0.0)

# memulai solid Drawing
def draw(slices, stacks):

    t = time.time() % 1000
    angle = t*90
    quad = gluNewQuadric()

    glColor3fv(planetColor)

    # planet
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    glRotatef(45,1,0,0)
    glRotatef(angle,0,0,1)
    gluSphere(quad, 2, slices, stacks) # quads, radius, slices, stacks
    glPopMatrix()

    # partial disk menunjukkan bahwa objek dapat menghasilkan suatu hal yang sama atau ganda (overlapping).
    glColor3fv(partialDiskColor)
    glPushMatrix()
    glTranslatef(4.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 0, 1)
    gluPartialDisk(quad, 0.5, 1, slices, stacks, 0, 270)   # quad, inner, outer, slices, loops, start angle, sweep angle
    glPopMatrix()

    # Cincin
    glColor3f(1.0, 0.8, 0.2)        # mengontrol warna cincin
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 1, 1)
    gluDisk(quad, 2.2, 2.7, slices, stacks) # quad, inner, outer, slices, loops
    glPopMatrix()

    # glColor3f(0.7, 0.5, 0.0)      # Jika ingin mengubah warna cincin lainnya.
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    glRotatef(-60, 1, 0.2, 0)       # memutar dengan angle
    glRotatef(-angle, 1, 0, 1)      # putaran cincin terus menerus.
    gluDisk(quad, 2.2, 2.7, slices, stacks)  # quad, inner, outer, slices, loops
    glPopMatrix()

# Menggambar mode xray/Wireframe 
def xrayDraw(slices, stacks):
    t = time.time() % 1000
    angle = t * 90
    quad = gluNewQuadric()

    glColor3fv(planetColor)

    gluQuadricDrawStyle(quad, GLU_LINE)     # WireFrame Mode
    # planet
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    glRotatef(45, 1, 0, 0)
    glRotatef(angle, 0, 0, 1)
    gluSphere(quad, 2, slices, stacks)  # quads, radius, slices, stacks
    glPopMatrix()

    # space station
    glColor3fv(partialDiskColor)
    glPushMatrix()
    glTranslatef(4.4, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 0, 1)
    gluPartialDisk(quad, 0.5, 1, slices, stacks, 0, 270)  # quad, inner, outer, slices, loops, start angle, sweep angle
    glPopMatrix()

    # Cincin
    glColor3f(1.0, 0.8, 0.2)  # mengontrol warna cincin
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    # glRotatef(-60, 1, 0.2, 0)
    glRotatef(-angle, 0, 1, 1)
    gluDisk(quad, 2.2, 2.7, slices, stacks)  # quad, inner, outer, slices, loops
    glPopMatrix()

    # glColor3f(0.7, 0.5, 0.0)      # Jika ingin mengubah warna cincin lainnya.
    glPushMatrix()
    glTranslatef(1.8, 1.5, -6)
    glRotatef(-60, 1, 0.2, 0)   # memutar dengan angle
    glRotatef(-angle, 1, 0, 1)  # putaran cincin terus menerus.
    gluDisk(quad, 2.2, 2.7, slices, stacks) # quad, inner, outer, slices, loops
    glPopMatrix()

def UFO(xyz_pos):
    t = time.time() % 1000
    angle = t * 90

    quad = gluNewQuadric()

    glColor3f(0.4, 0.1, 0.4)
    glPushMatrix()
    glTranslatef(1, 1.5, -8)   #adalah -8
    glTranslatef(xyz_pos, xyz_pos, -xyz_pos)
    glRotatef(45, 1, 0, 0)
    glRotatef(angle, 0, 0, 1)
    gluSphere(quad, 1, 17, 17) # quads, radius, slices, stacks
    # glRotatef(70, 1, 0, 0)
    glPopMatrix()

    glColor3f(0.4, 0.8, 0.2)
    glPushMatrix()
    glTranslatef(1, 0.56, -8)
    glTranslatef(xyz_pos, xyz_pos, -xyz_pos)
    glRotatef(-90, 1, 0.0, 0)
    glRotatef(angle, 0, 0, 1)
    gluCylinder(quad, 1.5, 0.74, 1.6, 17, 17) # quads, base, top, height, slices, stacks
    glPopMatrix()

# mengatur light
light_ambient = [0.0, 0.0, 0.0, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [2.0, 5.0, 5.0, 0.0]

mat_ambient = [0.7, 0.7, 0.7, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
high_shininess = [100.0]


def main():
    slices = 7
    stacks = 7

    xrayButton = 1
    xyz_pos = 0.1
    movingDown = False
    z_pos = -8

    pygame.init()
    display = (800, 600)
    pygame.display.set_caption("OpenGL --> Transformasi Planet 3D")
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(-2.0, -1.0, -5)
    # glTranslatef(0,0,-5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    slices += 1
                    stacks += 1
                if event.key == pygame.K_DOWN and (slices > 3 and stacks > 3):
                    slices -= 1
                    stacks -= 1
                if event.key == pygame.K_x:
                    xrayButton = xrayButton+1

                # mengontrol view
                if event.key == pygame.K_a:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_d:
                    glTranslatef(-0.5, 0, 0)

                if event.key == pygame.K_w:
                    glTranslatef(0, -0.5, 0)
                if event.key == pygame.K_s:
                    glTranslatef(0, 0.5, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.5)
                if event.button == 5:
                    glTranslatef(0, 0, -0.5)
        # Pergerakan UFO
        if(movingDown):
            if(xyz_pos > -4):
                xyz_pos = xyz_pos - 0.04
            else:
                movingDown = False

        else:
            if(xyz_pos < 8):
                xyz_pos = xyz_pos + 0.04
            else:
                movingDown = True

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 3.0)

        # memulai menggambar stasiun luar angkasa
        if(xrayButton % 2):
            draw(slices, stacks)
        else:
            xrayDraw(slices, stacks)
        UFO(xyz_pos)

        # background color (warna angkasa)
        glClearColor(0.0, 0.0, 0.12, 1)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)

        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

        pygame.display.flip()
        pygame.time.wait(10)


angle = 0
main()
