"""
Script pour positionner l'écran Turtle sur le deuxième écran
"""
import turtle

# Crée l'écran turtle
screen = turtle.Screen()

# Taille et position
width = 700
height = 700
x_pos = 1920 + 100  # Pour 2e écran à droite de 1920px
y_pos = 100

# Récupère la fenêtre Tk associée à Turtle
root = turtle.getcanvas().winfo_toplevel()

# Applique la géométrie
geometry_string = f"{width}x{height}+{x_pos}+{y_pos}"
root.geometry(geometry_string)

# Exemple de tracé
turtle.circle(100)
turtle.done()