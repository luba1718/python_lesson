import lesson2
import view

def button_click():
    # lesson2.init(get_value())
    value_a = view.get_value()
    value_b = view.get_value()
    lesson2.init(value_a, value_b)
    result = lesson2.sum()
    view.view_data(result)