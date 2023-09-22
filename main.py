import tkinter as tk
from tkinter import TOP, GROOVE, BOTTOM, RAISED, LEFT, Y, X

import mysql.connector


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Customer, Payment):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=10)
        button_frame.pack(side=LEFT, fill=Y)

        # Title
        f1 = tk.Frame(self, bg="grey", relief=GROOVE, borderwidth=10)
        f1.pack(side=TOP, fill=X)

        # Items
        center_frame = tk.Frame(self, bg='white', relief=GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=TOP, anchor="n", fill=X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=TOP, fill=X)

        setting = tk.Label(button_frame, text="⚙️Settings", font=('FixedSys', 10, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Customer", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        table = []
        for row in range(3):
            row_labels = []
            for col in range(3):
                item_button = tk.Button(center_frame, text="Item", font=('FixedSys', 50, 'bold'), relief=RAISED)
                item_button.grid(row=row, column=col, sticky="nsew", padx=20, pady=30)
                row_labels.append(item_button)
            table.append(row_labels)


import tkinter as tk
import mysql.connector


class Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="⚙️Settings", font=('FixedSys', 10, 'bold'), width=10, height=2,
                           relief=tk.GROOVE, borderwidth=5)
        setting.pack(side=tk.BOTTOM, padx=15, pady=80)

        b1 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b1.pack(side=tk.BOTTOM, padx=15, pady=20)

        b2 = tk.Button(button_frame, text="Customer", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b2.pack(side=tk.BOTTOM, padx=15, pady=20)

        b3 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        # Labels and Entry fields for customer information
        tk.Label(center_frame, text="Customer ID:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=0, column=0,
                                                                                                    padx=15, pady=15)
        tk.Label(center_frame, text="Customer Name:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=1, column=0,
                                                                                                      padx=15, pady=15)
        tk.Label(center_frame, text="Phone:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=2, column=0, padx=15,
                                                                                              pady=15)
        tk.Label(center_frame, text="Address:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=3, column=0,
                                                                                                padx=15, pady=15)

        self.customer_id_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.customer_name_entry = tk.Entry(center_frame, width=40, borderwidth=7)
        self.phone_entry = tk.Entry(center_frame, width=30, borderwidth=7)
        self.address_entry = tk.Entry(center_frame, width=50, borderwidth=7)

        self.customer_id_entry.grid(row=0, column=1, padx=15, pady=15)
        self.customer_name_entry.grid(row=1, column=1, padx=15, pady=15)
        self.phone_entry.grid(row=2, column=1, padx=15, pady=15)
        self.address_entry.grid(row=3, column=1, padx=15, pady=15)

        save_button = tk.Button(center_frame, text="Save", font=('FixedSys', 10, 'bold'), command=self.save_customer)
        save_button.grid(row=4, column=1, padx=15, pady=15)

    def save_customer(self):
        customer_id = self.customer_id_entry.get()
        customer_name = self.customer_name_entry.get()
        phone = self.phone_entry.get()
        customer_address = self.address_entry.get()

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()

            insert_query = "INSERT INTO customers (customer_id, customer_name, phone, customer_address) VALUES (%s, %s, %s, %s)"
            values = (customer_id, customer_name, phone, customer_address)

            cursor.execute(insert_query, values)
            conn.commit()

            cursor.close()
            conn.close()

            print("Customer information saved successfully!")

        except Exception as e:
            print(f"Error: {e}")


class Payment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="⚙️Settings", font=('FixedSys', 10, 'bold'), width=10, height=2,
                           relief=tk.GROOVE, borderwidth=5)
        setting.pack(side=tk.BOTTOM, padx=15, pady=80)

        b1 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b1.pack(side=tk.BOTTOM, padx=15, pady=20)

        b2 = tk.Button(button_frame, text="Customer", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b2.pack(side=tk.BOTTOM, padx=15, pady=20)

        b3 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        # Fields For Payment

        # Create and place labels and entry fields for Order ID, Payment ID, and Payment Amount in a grid
        self.payment_id_label = tk.Label(center_frame, text="Payment ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.payment_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.payment_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.order_id_label = tk.Label(center_frame, text="Order ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.order_id_label.grid(row=1, column=0, padx=10, pady=5)

        self.order_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.order_id_entry.grid(row=1, column=1, padx=10, pady=5)

        self.payment_amount_label = tk.Label(center_frame, text="Payment Amount:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_label.grid(row=2, column=0, padx=10, pady=5)

        self.payment_amount_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create a label and radio buttons for Payment Method in a grid
        self.payment_method_label = tk.Label(center_frame, text="Payment Method:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_method_label.grid(row=3, column=0, padx=10, pady=5)

        # Create a variable to hold the selected payment method
        self.payment_method_var = tk.StringVar()

        card_radio = tk.Radiobutton(center_frame, text="Card", variable=self.payment_method_var, value="Card",
                                    bg='white', font=('FixedSys', 20, 'bold'))
        cash_radio = tk.Radiobutton(center_frame, text="Cash", variable=self.payment_method_var, value="Cash",
                                    bg='white', font=('FixedSys', 20, 'bold'))

        card_radio.grid(row=3, column=1, padx=10, pady=5)
        cash_radio.grid(row=4, column=1, padx=10, pady=5)

        # Create a payment button to process the payment
        self.payment_button = tk.Button(center_frame, text="Process Payment", bg='white', font=('FixedSys', 20, 'bold'),
                                        command=self.process_payment)
        self.payment_button.grid(row=5, columnspan=2, padx=10, pady=15)

    def process_payment(self):
        payment_id = self.payment_id_entry.get()
        order_id = self.order_id_entry.get()
        payment_amount = self.payment_amount_entry.get()
        payment_method = self.payment_method_var.get()

        # Insert payment data into the database
        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )

            cursor = conn.cursor()

            insert_query = "INSERT INTO payments (payment_id, order_id,payment_amount, payment_method) VALUES (%s, %s, %s, %s)"
            data = (payment_id, order_id, payment_amount, payment_method)

            cursor.execute(insert_query, data)
            conn.commit()

            self.payment_id_entry.delete(0, tk.END)
            self.order_id_entry.delete(0, tk.END)
            self.payment_amount_entry.delete(0, tk.END)
            self.payment_method_var.set("")
            print("Successfully Added!")

        except Exception as e:
            print("Error occurred! ", e)


# Your other classes (StartPage, TkinterApp) remain unchanged.

# Create an instance of TkinterApp and run the application
app = TkinterApp()
app.mainloop()
