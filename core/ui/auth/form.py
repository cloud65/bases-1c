# pylint: disable=line-too-long
"""Формы для авторизации"""
from fast_semaintic_ui import FormInput, FormButton, ColorEnum, SizeEnum, TextAlignEnum, EventSubmit, Form, Segment, \
    GridColumn, Grid, VerticalAlignEnum, EventData
from fast_semaintic_ui.elements import Value
from fast_semaintic_ui.header import Header
from fast_semaintic_ui.types import AnyElement


def page_login() -> list[AnyElement]:
    """Окно авторизации"""
    user = FormInput(name='auth.username', fluid=True, focus=True,
                     icon='user', icon_position='left', placeholder='Логин')
    password = FormInput(name='auth.password', fluid=True,
                         icon='lock', icon_position='left',
                         placeholder='Пароль', type='password')

    button = FormButton(
        color=ColorEnum.teal, fluid=True, size=SizeEnum.large,
        content='Авторизация', icon='key', disabled=Value('login.disabled')
    )
    button.on_click = EventSubmit(url='/auth/token', name=['auth'], loading='loading_form')

    header = Header(h='h2', color=ColorEnum.blue, text_align=TextAlignEnum.center)
    header.text = 'Авторизация'
    form = Form(id='login_form', size=SizeEnum.large, loading=Value('loading_form'))

    form.add(Segment().add(user, password, button))

    column = GridColumn(style={'maxWidth': 450})
    column.add(header, form)

    grid = Grid(text_align=TextAlignEnum.center, vertical_align=VerticalAlignEnum.middle)
    grid.style = {'height': '100vh'}
    grid.add(column)
    return [grid, EventData(data={'login.disabled': False})]
