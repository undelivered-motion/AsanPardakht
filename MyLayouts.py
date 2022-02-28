import PySimpleGUI as sg


sg.theme('DarkAmber')   # Add a touch of color

title_font = ('B Nazanin',14,'bold')
font = ('B Nazanin',12)
pad = (0,10)
window_size = (400,400)




main_menu_layout = [  [sg.Text('منوی اصلی', font=title_font)],
            [sg.Button('ثبت کارت بانکی', pad=pad)],
            [sg.Button('خرید شارژ سیم کارت', pad = pad)],
            [sg.Button('مشاهده موجودی', pad = pad)],
            [sg.Button('کارت به کارت', pad = pad)] ]




#-----------------register----------------

register_error_layout = [
    [sg.Text('اطلاعات وارد شده معتبر نمیباشند.', font = title_font)],
    [sg.Button('تایید',key='-register_error_ok-', pad=pad)],
]
register_success_layout = [
    [sg.Text('عملیات موفقیت آمیز بود.', font = title_font)],
    [sg.Button('تایید',key='-register_success_ok-', pad = pad)]
]

register_col1_layout = [
    [sg.Text('ثبت کارت بانکی',font = title_font)],
    [sg.Text('نام خود را وارد کنید', font = font)],
    [sg.InputText(key="-register_name-",justification='center',do_not_clear=False)],
    [sg.Text('شماره کارت را وارد کنید', font = font)],
    [sg.InputText(key="-register_card_number-",justification='center',do_not_clear=False)],
    [sg.Text('رمز کارت را وارد کنید', font = font)],
    [sg.InputText(key="-register_password-",justification='center',do_not_clear=False)],
    [sg.Text('شماره سیم کارت را وارد کنید', font = font)],
    [sg.InputText(key="-register_sim_number-",justification='center',do_not_clear=False)],
    [sg.Button('تایید',key='-register_ok-', pad=pad)]
]

register_layout = [
    [sg.Column(register_col1_layout, visible=True, key='-register_page1-', element_justification='center')]
]


#-----------------charge simcard----------------
charge_sim_page1 = [
    [sg.Text('شارژ سیم کارت',font = title_font)],
    [sg.Text('شماره سیم کارت را وارد کنید', font = font)],
    [sg.InputText(key="-charge_sim_sim_number-",justification='center',do_not_clear=False)],
    [sg.Text('مبلغ وارد کنید', font = font)],
    [sg.InputText(key="-charge_sim_amount-",justification='center',do_not_clear=False)],
    [sg.Button('تایید',key='-charge_sim_page1_ok-', pad=pad)]
]

charge_sim_page2 = [
    [sg.Text('شارژ سیم کارت',font = title_font)],
    [sg.Text('شماره کارت وارد کنید', font = font)],
    [sg.InputText(key="-charge_sim_card_number-",justification='center',do_not_clear=False)],
    [sg.Text('رمز کارت وارد کنید', font = font)],
    [sg.InputText(key="-charge_sim_card_pass-",justification='center',do_not_clear=False)],
    [sg.Button('تایید',key='-charge_sim_page2_ok-', pad=pad)]
]
charge_sim_success = [
    [sg.Text('شارژ سیم کارت',font = title_font)],
    [sg.Text('عملیات موفقیت آمیز بود', font = font)],
    [sg.Button('تایید',key='-charge_sim_success_ok-', pad=pad)]
]

charge_sim_layout = [
    [
        sg.Column(charge_sim_page1, visible=True, key='-charge_sim_page1-', element_justification='center'),
        sg.Column(charge_sim_page2, visible=False, key='-charge_sim_page2-', element_justification='center'),
        sg.Column(charge_sim_success, visible=False, key='-charge_sim_success-', element_justification='center')
    ]
]


#-----------------transaction----------------

transaction_page1=[
    [sg.Text('کارت به کارت',font = title_font)],
    [sg.Text('شماره کارت مبدا را وارد کنید', font = font)],
    [sg.InputText(key="-transaction_source_card-",justification='center',do_not_clear=False)],
    [sg.Text('رمز کارت مبدا را وارد کنید', font = font)],
    [sg.InputText(key="-transaction_source_password-",justification='center',do_not_clear=False)],
    [sg.Text('مبلغ را وارد کنید', font = font)],
    [sg.InputText(key="-transaction_amount-",justification='center',do_not_clear=False)],
    [sg.Button('تایید', key= '-transaction_page1_ok-', pad=pad)]
]
transaction_page2 = [
    [sg.Text('کارت به کارت',font = title_font)],
    [sg.Text('شماره کارت مقصد را وارد کنید', font = font)],
    [sg.InputText(key="-transaction_dest_card-",justification='center',do_not_clear=False)],
    [sg.Button('تایید', key= '-transaction_page2_ok-', pad=pad)]
]
transaction_page3 = [
    [sg.Text('کارت به کارت',font = title_font)],
    [sg.Text('دارنده کارت مقصد', font = font)],
    [sg.Text('',key='-transaction_dest_name-', font = font)],
    [sg.Text('میباشد.', font = font)],
    [sg.Button('تایید', key= '-transaction_page3_ok-', pad=pad)]
]

transaction_layout = [
    [
        sg.Column(transaction_page1, visible=True, key='-transaction_page1-', element_justification='center'),
        sg.Column(transaction_page2, visible=False, key='-transaction_page2-', element_justification='center'),
        sg.Column(transaction_page3, visible=False, key='-transaction_page3-', element_justification='center')
    ]
]



#-----------------mojudi----------------

mojudi_page1=[
    [sg.Text('مشاهده موجودی',font = title_font)],
    [sg.Text('شماره کارت را وارد کنید', font = font)],
    [sg.InputText(key="-mojudi_card_number-",justification='center',do_not_clear=False)],
    [sg.Text('رمز کارت را وارد کنید', font = font)],
    [sg.InputText(key="-mojudi_card_password-",justification='center',do_not_clear=False)],
    [sg.Button('تایید', key= '-mojudi_page1_ok-', pad=pad)]
]

mojudi_layout = [
    [
        sg.Column(mojudi_page1, visible=True, key='-mojudi_page1-', element_justification='center'),
    ]
]


#----------------------------------------

def open_window_continue(msg):
    layout = [
                [sg.Text(msg, font = font)],
                [sg.Button('بازگشت به منوی اصلی',key='-return-', pad=pad)],
                [sg.Button('تلاش مجدد',key='-continue-', pad=pad)]
            ]
    result_window = sg.Window("نتیجه عملیات", layout, modal=True, font=font, element_justification='center')
    choice = None
    event, values = result_window.read()
    if event == "-return-" or event == sg.WIN_CLOSED:
        choice = 0
    elif event == "-continue-":
        choice = 1
    result_window.close()

    return choice

def open_window_return(msg):
    layout = [
                [sg.Text(msg, font = font)],
                [sg.Button('تایید و خروج',key='-return-', pad=pad)],
            ]
    result_window = sg.Window("خروج", layout, modal=True, font=font, element_justification='center')
    event, values = result_window.read()
    if event == "-return-" or event == sg.WIN_CLOSED:
        pass
    result_window.close()
    return 0
