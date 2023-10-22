import tkinter as tk
from tkinter import TOP, GROOVE, BOTTOM, RAISED, LEFT, Y, X, messagebox, RIGHT
from datetime import datetime
import mysql.connector


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Customer, Payment, ViewCustomers,Orders):
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
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        table = []
        for row in range(3):
            row_labels = []
            for col in range(3):
                item_button = tk.Button(center_frame, text="Item", font=('FixedSys', 50, 'bold'), relief=RAISED)
                item_button.grid(row=row, column=col, sticky="nsew", padx=20, pady=30)
                row_labels.append(item_button)
            table.append(row_labels)


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
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        # Labels and Entry fields for customer information
        tk.Label(center_frame, text="Customer ID:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=0, column=0,
                                                                                                    padx=10, pady=5)
        tk.Label(center_frame, text="Customer Name:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=1, column=0,
                                                                                                      padx=10, pady=5)
        tk.Label(center_frame, text="Phone:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=2, column=0, padx=10,
                                                                                              pady=5)
        tk.Label(center_frame, text="Address:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=3, column=0,
                                                                                                padx=10, pady=5)

        self.customer_id_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.customer_name_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.phone_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.address_entry = tk.Entry(center_frame, width=20, borderwidth=7)

        self.customer_id_entry.grid(row=0, column=1, padx=10, pady=15)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=15)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=15)
        self.address_entry.grid(row=3, column=1, padx=10, pady=15)

        save_button = tk.Button(center_frame, text="Submit Data", font=('FixedSys', 20, 'bold'), command=self.save_customer)
        save_button.grid(row=4, columnspan=2, padx=10, pady=15)

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

            self.customer_id_entry.delete(0,tk.END)
            self.customer_name_entry.delete(0,tk.END)
            self.phone_entry.delete(0,tk.END)
            self.address_entry.delete(0,tk.END)

            tk.messagebox.showinfo("showinfo","Inserted Successfully!")

        except Exception as e:
            print(f"Error: {e}")
            tk.messagebox.showerror("showerror","Error!")


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
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        # Fields For Payment

        # Create and place labels and entry fields for Order ID, Payment ID, and Payment Amount in a grid
        self.payment_id_label = tk.Label(center_frame, text="Payment ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.payment_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.payment_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_id_entry.grid(row=0, column=1, padx=10, pady=15)

        self.order_id_label = tk.Label(center_frame, text="Order ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.order_id_label.grid(row=1, column=0, padx=10, pady=5)

        self.order_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.order_id_entry.grid(row=1, column=1, padx=10, pady=15)

        self.payment_amount_label = tk.Label(center_frame, text="Payment Amount:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_label.grid(row=2, column=0, padx=10, pady=5)

        self.payment_amount_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_amount_entry.grid(row=2, column=1, padx=10, pady=15)

        # label and radio buttons for Payment Method in a grid
        self.payment_method_label = tk.Label(center_frame, text="Payment Method:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_method_label.grid(row=3, column=0, padx=10, pady=5)

        # variable to hold the selected payment method
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
            tk.messagebox.showinfo("showinfo","Inserted successfully!")

        except Exception as e:
            print("Error occurred! ", e)
            tk.messagebox.showerror("showerror","Error")


class ViewCustomers(tk.Frame):
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
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        listbox =tk.Listbox(center_frame,width=100,borderwidth=7,height=20)
        listbox.pack()

        def fetch_data(self):
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM customers")

                rows = cursor.fetchall()

                cursor.close()
                conn.close()

                return rows

            except Exception as e:
                print("Error!")

        def update_listbox():
            data = fetch_data(self)
            listbox.delete(0,tk.END)
            listbox.insert(tk.END,"Customer Information: ")

            for row in data:
                for info in row:
                    listbox.insert(tk.END,info)
                listbox.insert(tk.END,"--------------------------------")

        fetch_button = tk.Button(down_nav_frame, text="Fetch", relief=tk.GROOVE, font=('FixedSys', 10, 'bold'),
                                 width=20, height=2, borderwidth=2, command=update_listbox)
        fetch_button.pack(side=tk.BOTTOM, padx=15, pady=10)


class Orders(tk.Frame):
    def __init__(self,parent,controller):
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
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        item_labels = ['1','2','3','4','5','6','7','8','9']
        price = [10,10,10,10,10,10,10,10,10]
        quantity_entries = []  # List to store entry fields for quantities
        for i in range(9):
            item_label = tk.Label(center_frame, text=f"Item {i + 1}", font=('FixedSys', 12))
            item_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
            item_labels.append(item_label)

            quantity_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            quantity_entries.append(quantity_entry)

        self.order_id_label = tk.Label(center_frame, text="Order ID:", font=('FixedSys', 12))
        self.order_id_label.grid(row=10, column=0, padx=10, pady=5, sticky='w')
        self.order_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.order_id_entry.grid(row=10, column=1, padx=10, pady=5)

        self.customer_id_label = tk.Label(center_frame, text="Customer ID:", font=('FixedSys', 12))
        self.customer_id_label.grid(row=11, column=0, padx=10, pady=5, sticky='w')
        self.customer_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.customer_id_entry.grid(row=11, column=1, padx=10, pady=5)

        self.order_date_label = tk.Label(center_frame, text="Order Date:", font=('FixedSys', 12))
        self.order_date_label.grid(row=12, column=0, padx=10, pady=5, sticky='w')

        order_date_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        order_date_value.grid(row=12, column=1, padx=10, pady=5)

        self.total_price_label = tk.Label(center_frame, text="Total Price:", font=('FixedSys', 12))
        self.total_price_label.grid(row=13, column=0, padx=10, pady=5, sticky='w')

        total_price_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        total_price_value.grid(row=13, column=1, padx=10, pady=5)

        # Step 6: Calculate Total Price
        def calculate_total_price():
            total_price = 0
            for i in range(9):
                quantity_str = quantity_entries[i].get()
                if quantity_str and quantity_str.isdigit():
                    quantity = int(quantity_str)
                    total_price += quantity * price[i]

            total_price_value.config(text=f"Total Price: ${total_price}")
            order_date_value.config(text=f"Today: {datetime.now()}")

        # Step 7: Save Order to Database
        def save_order_to_database():
            order_id = int(self.order_id_entry.get())
            customer_id = int(self.customer_id_entry.get())
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_price_str = total_price_value.cget("text")[13:]
            total_price = float(total_price_str.replace('$', ''))

            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                insert_query = "INSERT INTO Orders(order_id,customer_id,order_date,total_price) VALUES (%s, %s, %s, %s)"
                data = (order_id, customer_id, order_date, total_price)

                cursor.execute(insert_query, data)
                conn.commit()

            except Exception as e:
                print("Error occurred! ", e)

        def submit_order():
            calculate_total_price()
            save_order_to_database()

        submit_button = tk.Button(center_frame, text="Submit Order", font=('FixedSys', 12),
                                  command=submit_order)
        submit_button.grid(row=14, column=0, columnspan=2, pady=10)


# Create an instance of TkinterApp and run the application
app = TkinterApp()
app.mainloop()
