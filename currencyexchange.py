import customtkinter as ctk
import requests
ctk.set_appearance_mode('system')
ctk.set_default_color_theme("green")

url = "https://v6.exchangerate-api.com/v6/6ee6526b7aa7775a3faac095/latest/USD"
response = requests.get(url)
infos = response.json()
currency_data = infos.get("conversion_rates")

def conversion():
    amount = float(base_amount.get())
    org_crncy = selected_opt1.get()
    target_crncy = selected_opt2.get()

    org_rate = currency_data[org_crncy]
    target_rate = currency_data[target_crncy]
 
    conversion_amount = amount * target_rate / org_rate

    result.configure(text=f"Converted amount: {round(conversion_amount,4)} {selected_opt2.get()}")

app = ctk.CTk()
app.title("Currency Exchange App")
app.geometry("400x500")
app.iconbitmap("moneyicon.ico")

main_frame = ctk.CTkFrame(master=app,border_width=1)
main_frame.pack(expand=True,fill="both",padx=10,pady=10)

header = ctk.CTkLabel(master=main_frame,text="Currency\nExchange",font=("Eras Bold ITC",50))
header.pack(pady=10)

base_amount = ctk.CTkEntry(master=main_frame,placeholder_text="Insert Amount Here",width=300,height=40,font=("Arial",20))
base_amount.pack(pady=10)

selected_opt1 = ctk.StringVar()
selected_opt2 = ctk.StringVar()

options1 = ctk.CTkOptionMenu(master=main_frame,values=['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 
                                                       'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 
          'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 
          'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 
          'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 
          'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 
          'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 
          'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 
          'TRY', 'TTD', 
          'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'],
          dropdown_hover_color="green",font=("Arial",20,"bold"),text_color="black",variable=selected_opt1)
options1.pack(pady=10)
options1.set("USD")

CTo = ctk.CTkLabel(master=main_frame,text="Convert To -",font=("Bahnschrift SemiBold",20))
CTo.pack(pady=10)

options2 = ctk.CTkOptionMenu(master=main_frame,values=['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 
                                                       'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 
          'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 
          'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 
          'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 
          'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 
          'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 
          'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 
          'TRY', 'TTD', 
          'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'],
          dropdown_hover_color="green",font=("Arial",20,"bold"),text_color="black",variable=selected_opt2)
options2.pack(pady=10)
options2.set("USD")

conv_btn = ctk.CTkButton(master=main_frame,text="Convert",font=("Bahnschrift SemiBold",20,"bold"),text_color="black",command=conversion,fg_color="white",width=30)
conv_btn.pack(pady=20)

result = ctk.CTkLabel(master=main_frame,text="",font=("Bahnschrift SemiBold",20),text_color="white")
result.pack(pady=10)

app.mainloop()
