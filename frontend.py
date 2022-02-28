# run this

from backend import *
from MyLayouts import *


def create_window():
    layout = [
        [sg.Column(main_menu_layout, key='-main_menu-', element_justification='center'),
         sg.Column(register_layout, visible=False, key='-register-', element_justification='center'),
         sg.Column(charge_sim_layout, visible=False, key='-charge_sim-', element_justification='center'),
         sg.Column(mojudi_layout, visible=False, key='-mojudi-', element_justification='center'),
         sg.Column(transaction_layout, visible=False, key='-transaction-', element_justification='center')]
    ]

    window = sg.Window('آپ', layout, size=window_size, font=font, element_justification='center')
    window.finalize()
    return window


def get_register_layout(window):
    window['-main_menu-'].update(visible=False)
    window['-register-'].update(visible=True)
    event, values = window.read()

    if event== '-register_ok-' :
        name = values['-register_name-']
        card_number = values['-register_card_number-']
        password = values['-register_password-']
        sim_number = values['-register_sim_number-']

        msg = "عملیات موفقیت آمیز بود." if make_acc(name,card_number,password, sim_number) else "اطلاعات وارد شده معتبر نمیباشند."
        open_window_return(msg)

    window['-main_menu-'].update(visible=True)
    window['-register-'].update(visible=False)

    return window


def get_charge_sim_layout(window):
    window['-main_menu-'].update(visible=False)
    window['-charge_sim-'].update(visible=True)
    event, values = window.read()
    while event=='-charge_sim_page1_ok-':
        sim_number = values['-charge_sim_sim_number-']
        amount = values['-charge_sim_amount-']
        window['-charge_sim_page1-'].update(visible=False)
        window['-charge_sim_page2-'].update(visible=True)
        event, values = window.read()
        if event=='-charge_sim_page2_ok-':
            card_number = values['-charge_sim_card_number-']
            card_pass = values['-charge_sim_card_pass-']
            result = charge_sim(sim_number, amount, card_number, card_pass) # 0 success 1 mablagh 2 wrong card
            window['-charge_sim_page2-'].update(visible=False)
            if result ==0:
                window['-charge_sim_success-'].update(visible=True)
                event, values = window.read()
                if event=='-charge_sim_success_ok-':# return to menu
                    window['-charge_sim_success-'].update(visible=False)
                    window['-charge_sim_page1-'].update(visible=True)
                    window['-charge_sim-'].update(visible=False)
                    window['-main_menu-'].update(visible=True)
                    break
            else:
                window['-charge_sim_page2-'].update(visible=False)
                window['-charge_sim_page1-'].update(visible=True)
                msg = "موجودی کافی نیست." if result==1 else "اطلاعات کارت صحیح نیست."
                if open_window_continue(msg): # 1 continue
                    event, values = window.read()
                else: # 0 return
                    window['-charge_sim-'].update(visible=False)
                    window['-main_menu-'].update(visible=True)
                    break

    return window


def get_transaction_layout(window):
    window['-main_menu-'].update(visible=False)
    window['-transaction-'].update(visible=True)
    event,values = window.read()
    while event == '-transaction_page1_ok-':
        source_card = values['-transaction_source_card-']
        source_pass = values['-transaction_source_password-']
        amount = values['-transaction_amount-']
        window['-transaction_page1-'].update(visible=False)
        window['-transaction_page2-'].update(visible=True)
        event, values= window.read()
        if event=='-transaction_page2_ok-':
            dest_card = values['-transaction_dest_card-']
            dest_name = get_name_of_card_owner(dest_card)
            window['-transaction_dest_name-'].update(dest_name)
            window['-transaction_page2-'].update(visible=False)
            window['-transaction_page3-'].update(visible=True)
            event, values= window.read()
            if event == '-transaction_page3_ok-':

                window['-transaction_page3-'].update(visible=False)
                window['-transaction_page1-'].update(visible=True)

                res = transaction(source_card,source_pass, dest_card, amount)

                if res==0:
                    open_window_return("عملیات با موفقیت انجام شد.")
                    break

                elif res==1:
                    open_window_return("موجودی کافی نیست.")
                    break

                else:
                    if res==2: # res==2
                        msg = "شماره کارت میدا صحیح نیست."
                    elif res==3:
                        msg = "شماره کارت مقصد صحیح نیست."
                    else:
                        msg = "رمز کارت صحیح نیست."

                    if open_window_continue(msg): #1 continue
                        event, values = window.read()
                    else:
                        break
    window['-main_menu-'].update(visible=True)
    window['-transaction-'].update(visible=False)
    return window


def get_mojudi_layout(window):
    window['-main_menu-'].update(visible=False)
    window['-mojudi-'].update(visible=True)

    event, values = window.read()
    while event == '-mojudi_page1_ok-':
        card_number = values['-mojudi_card_number-']
        card_password = values['-mojudi_card_password-']
        amount = get_balance(card_number, card_password)
        if amount:
            open_window_return(f'{amount} تومان')
            break;
        else: # wrong info
            if open_window_continue('اطلاعات وارد شده صحیح نمیباشد.'):
                event, values = window.read()
            else:
                break

    window['-mojudi-'].update(visible=False)
    window['-main_menu-'].update(visible=True)
    return window


# Create the Window
window = create_window()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event=='ثبت کارت بانکی':
        get_register_layout(window)
    elif event=='خرید شارژ سیم کارت':
        get_charge_sim_layout(window)
    elif event=='مشاهده موجودی':
        get_mojudi_layout(window)
    elif event=='کارت به کارت':
        get_transaction_layout(window)
    else:
        pass

window.close()
