import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.all(30)
    page.bgcolor = ft.colors.BLACK

    habits_list = [
        {'title': 'Estudar inglês', 'done': False},
        {'title': 'Estudar Django', 'done': True},
        {'title': 'Fazer projetos', 'done': False},
    ]

    # Função para calcular e atualizar o progresso
    def update_progress():
        done = list(filter(lambda x: x['done'], habits_list))
        total = len(done) / len(habits_list) if habits_list else 0
        progress_bar.value = float(f'{total:.2f}')
        progress_text.value = f'{total:.0%}'
        progress_bar.update()
        progress_text.update()

    # Função que altera o estado do hábito e atualiza o progresso
    def change(e=None):
        for hl in habits_list:
            if hl['title'] == e.control.label:
                hl['done'] = e.control.value
        update_progress()  # Chama a atualização de progresso após mudança

    # Função para adicionar um novo hábito
    def add_habit(e):
        new_habit = e.control.value
        if new_habit:  # Verifica se o campo não está vazio
            habits_list.append({'title': new_habit, 'done': False})
            habits.content.controls = [
                ft.Checkbox(
                    label=hl['title'],
                    value=hl['done'],
                    on_change=change,
                ) for hl in habits_list
            ]
            habits.update()
            e.control.value = ''
            e.control.update()
            update_progress()  # Atualiza o progresso após adicionar novo hábito

    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(value='Que bom ter você aqui', size=30, color=ft.colors.WHITE),
            ft.Text(value='Como estão seus hábitos hoje?', size=20, color=ft.colors.GREY),

            ft.Container(
                padding=ft.padding.all(30),
                bgcolor=ft.colors.INDIGO,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=30),
                content=ft.Column(
                    controls=[
                        ft.Text(value='Sua evolução hoje', size=20, color=ft.colors.WHITE),
                        progress_text := ft.Text(value='0%', size=50, color=ft.colors.WHITE),
                        progress_bar := ft.ProgressBar(
                            value=0,
                            color=ft.colors.INDIGO_900,
                            bgcolor=ft.colors.INDIGO_100,
                            height=20,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),

            ft.Text(value='Hábitos de hoje', size=20, weight=ft.FontWeight.BOLD),
            ft.Text(value='Marcar suas tarefas como concluidas te motiva a continuar focado.'),

            habits := ft.Container(
                expand=True,
                padding=ft.padding.all(30),
                bgcolor=ft.colors.GREY_900,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=20),
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    spacing=20,
                    controls=[
                        ft.Checkbox(
                            label=hl['title'],
                            value=hl['done'],
                            on_change=change,
                        ) for hl in habits_list
                    ]
                )
            ),

            ft.Text(value='Adicionar novo hábito', size=20, color=ft.colors.WHITE),
            ft.TextField(
                hint_text='Escreva um hábito...',
                border=ft.InputBorder.UNDERLINE,
                on_submit=add_habit
            )
        ]
    )

    page.add(layout)
    update_progress()  # Garante que o progresso inicial seja calculado

if __name__ == '__main__':
    ft.app(target=main)
