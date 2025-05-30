"""
Etoiles à 6 branches
Il faut que je travaille dessus pour comprendre mieux le principe de l'algoritme.
"""
import turtle
import math

# Rayon du cercle
R = 300
turtle.speed(2)

# Fonction angle → coordonnées cartésiennes
def polar_to_cartesian(angle_deg, radius):
    angle_rad = math.radians(angle_deg)
    x = radius * math.cos(angle_rad)
    y = radius * math.sin(angle_rad)
    return x, y

# Triangles (sommet du haut à 90°)
triangle_up_angles = [90, 210, 330]
triangle_down_angles = [150, 270, 30]

triangle_up = [polar_to_cartesian(a, R) for a in triangle_up_angles]
triangle_down = [polar_to_cartesian(a, R) for a in triangle_down_angles]

# Tracer le cercle (facultatif)
turtle.penup()
turtle.goto(0, -R)
turtle.pendown()
turtle.pencolor("gray")
turtle.circle(R)

# Remplir triangle vers le haut
turtle.fillcolor("skyblue")
turtle.penup()
turtle.goto(triangle_up[0])
turtle.begin_fill()
turtle.pendown()
for pt in triangle_up[1:] + [triangle_up[0]]:
    turtle.goto(pt)
turtle.end_fill()

# Remplir triangle vers le bas
turtle.fillcolor("lightgreen")
turtle.penup()
turtle.goto(triangle_down[0])
turtle.begin_fill()
turtle.pendown()
for pt in triangle_down[1:] + [triangle_down[0]]:
    turtle.goto(pt)
turtle.end_fill()

# 🔷 Repasser les périmètres avec trait épais
turtle.pensize(2)
turtle.pencolor("navy")  # Couleur du trait

# Contour triangle vers le haut
turtle.penup()
turtle.goto(triangle_up[0])
turtle.pendown()
for pt in triangle_up[1:] + [triangle_up[0]]:
    turtle.goto(pt)

# Contour triangle vers le bas
turtle.penup()
turtle.goto(triangle_down[0])
turtle.pendown()
for pt in triangle_down[1:] + [triangle_down[0]]:
    turtle.goto(pt)

# Fin
turtle.hideturtle()
turtle.done()


