''' Juego de Departamentos de Colombia '''
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Juego de Departamentos de Colombia")
IMAGE = "ProjectsPerDay/Day 025/Project - Juego de los Departamentos de Colombia/departamentos_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
puntaje = 0
departamentos_acertados = []
departamentos_faltantes = []
departamentos = pd.read_csv(r"ProjectsPerDay\Day 025\Project - Juego de los Departamentos de Colombia\32_departamentos.csv")
todos_departamentos = departamentos.departamento.to_list()

while puntaje < len(departamentos.departamento)-1:
    respuesta_departamento = screen.textinput(
        title=f"{puntaje}/{len(departamentos.departamento)} Departamentos Correctos",
        prompt="¿Cuál es el nombre de otro departamento?").title()

    if respuesta_departamento == "Salir":
        for departamento in todos_departamentos:
            if departamento not in departamentos_acertados:
                departamentos_faltantes.append(departamento)
        departamentos_faltantes = pd.DataFrame(departamentos_faltantes)
        departamentos_faltantes.to_csv("estados_a_aprender.csv")
        break
    if respuesta_departamento in todos_departamentos:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = departamentos[departamentos["departamento"] == respuesta_departamento]
        departamentos_acertados.append(respuesta_departamento)
        t.color('white')
        style = ('Courier', 8, 'normal')
        t.goto(int(state.x),int(state.y))
        t.write(respuesta_departamento, font=style, align='left')
        puntaje += 1

screen.exitonclick()
