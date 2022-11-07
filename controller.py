import view, model

def start():
    while True:
        command = view.show_menu()
        match command:
            case '0':
                view.show_read_result(model.read_file())
            case '1':
                view.show_contacts(model.get_contacts())
            case '2':
                view.write_file(model.save_file())
            case '3':
                view.add_contact(model.add_contact())
            case '4':
                name = view.change_contact()
                view.show_contact(model.find_contact_name(name))
                view.show_contact(model.change_contact_name(name))
            case '5':
                view.del_contact(model.delete_contact(view.get_contact_del()))
            case '6':
                view.show_contact(model.find_contact_name(view.find_contact()))
            case '7':
                break