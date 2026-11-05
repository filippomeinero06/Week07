import flet as ft

from ui import controller


class View:
    def __init__(self, page):
        self._page = page
        self._controller = None

        self._list_view = None
        self._dd = None

    def set_controller(self, controller):
        self._controller = controller

    # Metodo che chiamo una volta per inizializzare la UI
    def initialize_ui(self):
        self._page.title = "Citibike"
        self._page.window.width = 600
        self._page.window.height = 400
        #self._page.window.resizable = False

        btn = ft.Button(content="All trips",
                        on_click = self._controller.handler_btn)

        self._dd = ft.Dropdown(label="Letter",
                               #on_select=self._controller.handler_btn_sel
                               )
        self._dd.options.append(ft.DropdownOption(key="A", text="A"))
        self._dd.options.append(ft.DropdownOption(key="B", text="B"))
        self._dd.options.append(ft.DropdownOption(key="C", text="C"))

        btn_sel = ft.Button(content="Selected trips",
                        on_click = self._controller.handler_btn_sel)


        row = ft.Row([btn, self._dd, btn_sel],
                     alignment = ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row)

        self._list_view = ft.ListView(expand=True, spacing=10)
        #list_view.controls.append(ft.Text("Ciao"))
        self._page.controls.append(self._list_view)

        #self.update_ui()


    # Metodo che può essere chiamato anche da fuori dalla
    # classe per aggiornare la UI quando necessario
    def update_ui(self):
        self._page.update()

    def show_alert_dialog(self, message):
        dialog=ft.AlertDialog(
            title=ft.Text(message)
        )
        self._page.show_dialog(dialog)