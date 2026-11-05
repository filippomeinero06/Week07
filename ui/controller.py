import flet as ft

class Controller():
    def __init__(self, model, view):
        self._model = model
        self._view = view

    # Funzione handler del pulsante, riceve un evento e
    def handler_btn(self, e):
        print("Button clicked")
        result = self._model.get_trips()

        # Prende quanto letto tramite il Model/Dao
        # e lo mostra nella UI, all'interno della listview
        self._view._list_view.controls.clear()
        self._view._list_view.controls.append(ft.Text(f"{len(result)}"))
        for trip in result:
            self._view._list_view.controls.append(ft.Text(f"{trip}"))
        self._view.update_ui()


    def handler_btn_sel(self, e):
        print("Button selected trips clicked")
        letter = self._view._dd.value
        if letter is None:
            self._view.show_alert_dialog("You must select a letter first")
            return

        result = self._model.get_selected_trips(letter)
        self._view._list_view.controls.clear()
        self._view._list_view.controls.append(ft.Text(f"{len(result)}"))
        for trip in result:
            self._view._list_view.controls.append(ft.Text(f"{trip}"))
        self._view.update_ui()

