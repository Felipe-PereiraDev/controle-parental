import flet as ft


class AppLogin:
    @staticmethod
    def tipo_conta(page):
        def show_login_responsavel(e):
            page.controls.clear()
            page.add(AppLogin._login_responsavel(page))
            page.update()

        def show_login_filho(e):
            page.controls.clear()
            page.add(AppLogin._login_filho(page))
            page.update()

        tipo_conta = ft.Container(
            width=600,
            height=350,
            bgcolor=ft.colors.WHITE,
            border_radius=12,
            content=ft.Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=50,
                controls=[
                    ft.Container(
                        width=600 * 0.50,
                        height=60,
                        bgcolor=ft.colors.GREEN_300,
                        border_radius=10,
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value="ESCOLHA UMA OPÇÃO",
                                    size=18,
                                    weight="bold",
                                    color=ft.colors.WHITE,
                                    text_align=ft.TextAlign.JUSTIFY
                                ),
                            ],
                            vertical_alignment="center",
                            alignment="center"
                        )
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="CONTA DO RESPONSÁVEL",
                                color=ft.colors.WHITE,
                                bgcolor=ft.colors.BLUE_900,
                                elevation=0,
                                width=240,
                                height=50,
                                on_click=show_login_responsavel,  # Função chamada no clique
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(
                                        width=1,
                                        color=ft.colors.WHITE
                                    )
                                )
                            ),
                            ft.ElevatedButton(
                                text="CONTA DO FILHO(A)",
                                color=ft.colors.WHITE,
                                bgcolor=ft.colors.BLUE_900,
                                elevation=0,
                                width=240,
                                height=50,
                                on_click=show_login_filho,
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(
                                        width=1,
                                        color=ft.colors.WHITE
                                    )
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                    )
                ]
            )
        )
        return tipo_conta

    @staticmethod
    def _registrar_conta_responsavel(page):
        def voltar_inicio(e):
            page.controls.clear()
            page.add(AppLogin.tipo_conta(page))
            page.update()

        def show_login_responsavel(e):
            page.controls.clear()
            page.add(AppLogin._login_responsavel(page))
            page.update()

        registar_responsavel = ft.Container(
            width=600,
            height=350,
            bgcolor=ft.colors.WHITE,
            border_radius=12,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=600 * 0.40,
                        height=350,
                        bgcolor=ft.colors.GREEN_300,
                        border_radius=ft.border_radius.only(
                            top_left=12,
                            top_right=0,
                            bottom_left=12,
                            bottom_right=0
                        ),
                        padding=ft.padding.only(
                            top=50,
                            left=15,
                            right=5,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.HOME,
                                            icon_color=ft.colors.WHITE,
                                            on_click=voltar_inicio
                                        ),
                                        ft.Container(
                                            width=80,
                                            height=80,
                                            border=ft.border.all(1, ft.colors.WHITE),
                                            border_radius=5
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    width=600 * 0.40
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="ENTRAR NA CONTA",
                                            size=18,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                        ft.Text(
                                            value="Caso já tenha uma conta, faça login clicando no botão abaixo",
                                            size=12,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                    ],
                                    spacing=0
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="ENTRAR",
                                            color=ft.colors.WHITE,
                                            bgcolor=ft.colors.GREEN_300,
                                            elevation=0,
                                            on_click=show_login_responsavel,
                                            style=ft.ButtonStyle(
                                                side=ft.BorderSide(
                                                    width=1,
                                                    color=ft.colors.WHITE
                                                )
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            spacing=25
                        )
                    ),

                    ft.Container(
                        width=600 * 0.6,
                        height=350,
                        padding=ft.padding.only(
                            top=50,
                            left=12,
                            right=20,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="CRIE SUA CONTA AGORA",
                                            color=ft.colors.GREEN_300,
                                            size=18,
                                            weight="bold",
                                            font_family="Poppins"
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.TextField(
                                                    hint_text="nome",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.PERSON,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.NAME
                                                ),
                                                ft.TextField(
                                                    hint_text="email",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.EMAIL,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.EMAIL
                                                ),
                                                ft.TextField(
                                                    hint_text="senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.TextField(
                                                    hint_text="confirme sua senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.ElevatedButton(
                                                    text='REGISTRAR',
                                                    width=600 * 0.60,
                                                    height=40,
                                                    bgcolor=ft.colors.GREEN_300,
                                                    style=ft.ButtonStyle(
                                                        side=ft.BorderSide(
                                                            width=1,
                                                            color=ft.colors.WHITE
                                                        )
                                                    ),
                                                    color=ft.colors.WHITE
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        return registar_responsavel

    @staticmethod
    def _login_responsavel(page):
        def voltar_inicio(e):
            page.controls.clear()
            page.add(AppLogin.tipo_conta(page))
            page.update()

        def show_resgiter_responsavel(e):
            page.controls.clear()
            page.add(AppLogin._registrar_conta_responsavel(page))
            page.update()

        login_responsavel = ft.Container(
            width=600,
            height=350,
            bgcolor=ft.colors.WHITE,
            border_radius=12,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=600 * 0.40,
                        height=350,
                        bgcolor=ft.colors.GREEN_300,
                        border_radius=ft.border_radius.only(
                            top_left=12,
                            top_right=0,
                            bottom_left=12,
                            bottom_right=0
                        ),
                        padding=ft.padding.only(
                            top=50,
                            left=15,
                            right=5,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.HOME,
                                    icon_color=ft.colors.WHITE,
                                    on_click=voltar_inicio
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            width=80,
                                            height=80,
                                            border=ft.border.all(1, ft.colors.WHITE),
                                            border_radius=5
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    width=600 * 0.40
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="REGISTRAR CONTA",
                                            size=18,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                        ft.Text(
                                            value="Caso não tenha uma conta, faça o resgistro clicando no botão abaixo",
                                            size=12,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                    ],
                                    spacing=0
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="REGISTRAR",
                                            color=ft.colors.WHITE,
                                            bgcolor=ft.colors.GREEN_300,
                                            elevation=0,
                                            on_click=show_resgiter_responsavel,
                                            style=ft.ButtonStyle(
                                                side=ft.BorderSide(
                                                    width=1,
                                                    color=ft.colors.WHITE
                                                )
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            spacing=25
                        )
                    ),

                    ft.Container(
                        width=600 * 0.6,
                        height=350,
                        padding=ft.padding.only(
                            top=50,
                            left=12,
                            right=20,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="LOGIN DO RESPONSÁVEL",
                                            color=ft.colors.GREEN_300,
                                            size=18,
                                            weight="bold",
                                            font_family="Poppins"
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.TextField(
                                                    hint_text="emaiL",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.EMAIL,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.EMAIL
                                                ),
                                                ft.TextField(
                                                    hint_text="senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        ft.TextButton(text="esqueci minha senha",
                                                                      style=ft.ButtonStyle(
                                                                          color=ft.colors.BLUE,
                                                                      ),
                                                                      )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.END
                                                ),
                                                ft.ElevatedButton(
                                                    text='LOGIN',
                                                    width=600 * 0.60,
                                                    height=40,
                                                    bgcolor=ft.colors.GREEN_300,
                                                    style=ft.ButtonStyle(
                                                        side=ft.BorderSide(
                                                            width=1,
                                                            color=ft.colors.WHITE
                                                        )
                                                    ),
                                                    color=ft.colors.WHITE
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        return login_responsavel

    @staticmethod
    def _login_filho(page):
        def voltar_inicio(e):
            page.controls.clear()
            page.add(AppLogin.tipo_conta(page))
            page.update()

        def show_register_filho(e):
            page.controls.clear()
            page.add(AppLogin._registrar_conta_filho(page))
            page.update()

        login_filho = ft.Container(
            width=600,
            height=350,
            bgcolor=ft.colors.WHITE,
            border_radius=12,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=600 * 0.40,
                        height=350,
                        bgcolor=ft.colors.GREEN_300,
                        border_radius=ft.border_radius.only(
                            top_left=12,
                            top_right=0,
                            bottom_left=12,
                            bottom_right=0
                        ),
                        padding=ft.padding.only(
                            top=50,
                            left=15,
                            right=5,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.HOME,
                                            icon_color=ft.colors.WHITE,
                                            on_click=voltar_inicio
                                        ),
                                        ft.Container(
                                            width=80,
                                            height=80,
                                            border=ft.border.all(1, ft.colors.WHITE),
                                            border_radius=5
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    width=600 * 0.40
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="REGISTRAR CONTA",
                                            size=18,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                        ft.Text(
                                            value="Caso não tenha uma conta, faça o resgistro clicando no botão abaixo",
                                            size=12,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                    ],
                                    spacing=0
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="REGISTRAR",
                                            color=ft.colors.WHITE,
                                            bgcolor=ft.colors.GREEN_300,
                                            elevation=0,
                                            on_click=show_register_filho,
                                            style=ft.ButtonStyle(
                                                side=ft.BorderSide(
                                                    width=1,
                                                    color=ft.colors.WHITE
                                                )
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            spacing=25
                        )
                    ),

                    ft.Container(
                        width=600 * 0.6,
                        height=350,
                        padding=ft.padding.only(
                            top=50,
                            left=12,
                            right=20,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="LOGIN DO FILHO",
                                            color=ft.colors.GREEN_300,
                                            size=18,
                                            weight="bold",
                                            font_family="Poppins"
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.TextField(
                                                    hint_text="email do responsável",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.EMAIL,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.EMAIL
                                                ),
                                                ft.TextField(
                                                    hint_text="senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.Row(
                                                    controls=[
                                                        ft.TextButton(text="esqueci minha senha",
                                                                      style=ft.ButtonStyle(
                                                                          color=ft.colors.BLUE,
                                                                      ),
                                                                      )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.END
                                                ),
                                                ft.ElevatedButton(
                                                    text='LOGIN',
                                                    width=600 * 0.60,
                                                    height=40,
                                                    bgcolor=ft.colors.GREEN_300,
                                                    style=ft.ButtonStyle(
                                                        side=ft.BorderSide(
                                                            width=1,
                                                            color=ft.colors.WHITE
                                                        )
                                                    ),
                                                    color=ft.colors.WHITE
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        return login_filho

    @staticmethod
    def _registrar_conta_filho(page):
        def voltar_inicio(e):
            page.controls.clear()
            page.add(AppLogin.tipo_conta(page))
            page.update()

        def show_login_filho(e):
            page.controls.clear()
            page.add(AppLogin._login_filho(page))
            page.update()

        registrar_filho = ft.Container(
            width=600,
            height=350,
            bgcolor=ft.colors.WHITE,
            border_radius=12,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=600 * 0.40,
                        height=350,
                        bgcolor=ft.colors.GREEN_300,
                        border_radius=ft.border_radius.only(
                            top_left=12,
                            top_right=0,
                            bottom_left=12,
                            bottom_right=0
                        ),
                        padding=ft.padding.only(
                            top=50,
                            left=15,
                            right=5,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.HOME,
                                            icon_color=ft.colors.WHITE,
                                            on_click=voltar_inicio
                                        ),
                                        ft.Container(
                                            width=80,
                                            height=80,
                                            border=ft.border.all(1, ft.colors.WHITE),
                                            border_radius=5
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    width=600 * 0.40
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="ENTRAR NA CONTA",
                                            size=18,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                        ft.Text(
                                            value="Caso já tenha uma conta, faça login clicando no botão abaixo",
                                            size=12,
                                            weight="bold",
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.JUSTIFY
                                        ),
                                    ],
                                    spacing=0
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="ENTRAR",
                                            color=ft.colors.WHITE,
                                            bgcolor=ft.colors.GREEN_300,
                                            elevation=0,
                                            on_click=show_login_filho,
                                            style=ft.ButtonStyle(
                                                side=ft.BorderSide(
                                                    width=1,
                                                    color=ft.colors.WHITE
                                                )
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            spacing=25
                        )
                    ),

                    ft.Container(
                        width=600 * 0.6,
                        height=350,
                        padding=ft.padding.only(
                            top=50,
                            left=12,
                            right=20,
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="CRIE A CONTA PARA SEU FILHO",
                                            color=ft.colors.GREEN_300,
                                            size=18,
                                            weight="bold",
                                            font_family="Poppins"
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.TextField(
                                                    hint_text="email do responsável",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.EMAIL,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.EMAIL
                                                ),
                                                ft.TextField(
                                                    hint_text="senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.TextField(
                                                    hint_text="confirme sua senha",
                                                    hint_style=ft.TextStyle(
                                                        size=15,
                                                        color="#b3b3b3"
                                                    ),
                                                    prefix_icon=ft.icons.LOCK,
                                                    height=40,
                                                    border_color=ft.colors.GREEN_300,
                                                    color=ft.colors.BLACK,
                                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                    password=True,
                                                    can_reveal_password=True
                                                ),
                                                ft.ElevatedButton(
                                                    text='REGISTRAR',
                                                    width=600 * 0.60,
                                                    height=40,
                                                    bgcolor=ft.colors.GREEN_300,
                                                    style=ft.ButtonStyle(
                                                        side=ft.BorderSide(
                                                            width=1,
                                                            color=ft.colors.WHITE
                                                        )
                                                    ),
                                                    color=ft.colors.WHITE
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        return registrar_filho
