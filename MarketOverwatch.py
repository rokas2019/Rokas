import tkinter as tk
from tkinter import ttk
import yfinance as yahooFinance
from yahoo_fin import stock_info

LARGE_FONT = ("Verdana", 13)


class SeaofStocks(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.iconbitmap(self, default='financial_profit_OqW_icon.ico')
        tk.Tk.wm_title(self, "Market Overwatch")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MarketOverwatch, FavoriteStocks, HistoricalData):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MarketOverwatch)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MarketOverwatch(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Current_stock = tk.StringVar()
        label1 = ttk.Label(self, text="Online Market Watch", font=LARGE_FONT)
        label1.grid(row=0, column=1, sticky="NSEW")
        label2 = ttk.Label(self, text="Company Symbol : ", font=LARGE_FONT)
        label2.grid(row=1, sticky="w")
        label3 = ttk.Label(self, text="Stock Price:    $", font=LARGE_FONT)
        label3.grid(row=4, sticky="w")
        result = tk.Label(self, text="", font=LARGE_FONT, textvariable=Current_stock)
        result.grid(row=4, column=1, sticky="w")

        def stock_price():
            price = stock_info.get_live_price(e1.get())
            Current_stock.set(price)

        e1 = tk.Entry(self)
        e1.grid(row=1, column=1)
        button0 = ttk.Button(self, text="Show", command=stock_price)
        button0.grid(row=1, column=2, columnspan=2, rowspan=1, padx=10, pady=10)
        button = ttk.Button(self, text="Favorite Stocks",
                            command=lambda: controller.show_frame(FavoriteStocks))
        button.grid(row=7, column=1, sticky="wens")

        button2 = ttk.Button(self, text="Historical Data",
                             command=lambda: controller.show_frame(HistoricalData))
        button2.grid(row=8, column=1, sticky="WENS")


class FavoriteStocks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Current_stock = tk.StringVar()

        def pushed_fav_1():
            price = stock_info.get_live_price('ASXC')
            Current_stock.set(price)

        def pushed_fav_2():
            price = stock_info.get_live_price('IDEX')
            Current_stock.set(price)

        def pushed_fav_3():
            price = stock_info.get_live_price('HTBX')
            Current_stock.set(price)

        def pushed_fav_4():
            price = stock_info.get_live_price('CIEN')
            Current_stock.set(price)

        def pushed_fav_5():
            price = stock_info.get_live_price('GSAT')
            Current_stock.set(price)

        def pushed_fav_6():
            price = stock_info.get_live_price('GEVO')
            Current_stock.set(price)

        def pushed_fav_7():
            price = stock_info.get_live_price('TAL')
            Current_stock.set(price)

        def pushed_fav_8():
            price = stock_info.get_live_price('TSLA')
            Current_stock.set(price)

        def pushed_fav_9():
            price = stock_info.get_live_price('ZOM')
            Current_stock.set(price)

        button_1 = ttk.Button(self, text="ASXC", command=pushed_fav_1)
        button_1.grid(row=5, column=0, columnspan=1, padx=20, pady=20, sticky="wens")
        button_2 = ttk.Button(self, text="IDEX", command=pushed_fav_2)
        button_2.grid(row=5, column=1, columnspan=1, padx=20, pady=20, sticky="wens")
        button_3 = ttk.Button(self, text="HTBX", command=pushed_fav_3)
        button_3.grid(row=5, column=2, columnspan=1, padx=20, pady=20, sticky="wens")
        button_4 = ttk.Button(self, text="CIEN", command=pushed_fav_4)
        button_4.grid(row=6, column=0, columnspan=1, padx=20, pady=20, sticky="wens")
        button_5 = ttk.Button(self, text="GSAT", command=pushed_fav_5)
        button_5.grid(row=6, column=1, columnspan=1, padx=20, pady=20, sticky="wens")
        button_6 = ttk.Button(self, text="GEVO", command=pushed_fav_6)
        button_6.grid(row=6, column=2, columnspan=1, padx=20, pady=20, sticky="wens")
        button_7 = ttk.Button(self, text="TAL", command=pushed_fav_7)
        button_7.grid(row=7, column=0, columnspan=1, padx=20, pady=20, sticky="wens")
        button_8 = ttk.Button(self, text="TSLA", command=pushed_fav_8)
        button_8.grid(row=7, column=1, columnspan=1, padx=20, pady=20, sticky="wens")
        button_9 = ttk.Button(self, text="ZOM", command=pushed_fav_9)
        button_9.grid(row=7, column=2, columnspan=1, padx=20, pady=20, sticky="wens")

        label = ttk.Label(self, text="▼Favorite Stocks▼", font=LARGE_FONT)
        label.grid(row=0, column=1, columnspan=3, sticky="wens")
        label3 = ttk.Label(self, text="Stock Price:    $", font=LARGE_FONT)
        label3.grid(row=4, sticky="w")
        result = tk.Label(self, text="", font=LARGE_FONT, textvariable=Current_stock)
        result.grid(row=4, column=1, sticky="w")
        button1 = ttk.Button(self, text="Back Stock Overwatch",
                             command=lambda: controller.show_frame(MarketOverwatch))
        button1.grid(row=8, column=1, sticky="WENS")

        button2 = ttk.Button(self, text="Historical Data",
                             command=lambda: controller.show_frame(HistoricalData))
        button2.grid(row=9, column=1, sticky="ENSW")


class HistoricalData(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Historical Stock Data!!!", font=LARGE_FONT)
        label.grid(row=0, columnspan=7, sticky="wens")
        label = ttk.Label(self, text="Company Symbol : ", font=LARGE_FONT)
        label.grid(row=1, sticky="wens")
        entry = tk.Entry(self)
        entry.grid(row=1, column=1)
        GetInformation = yahooFinance.Ticker("ASXC")
        list0 = (GetInformation.history(period="1mo"))

        button1 = ttk.Button(self, text="SEARCH", command=lambda: GetInformation)
        button1.grid(row=1, column=2)

        text = tk.Text(self)
        text.insert(tk.END, list0)
        text.grid(row=2, columnspan=7)

        button1 = ttk.Button(self, text="Online Market Overwatch",
                             command=lambda: controller.show_frame(MarketOverwatch))
        button1.grid(row=30, column=1, sticky="wens")

        button2 = ttk.Button(self, text="Favorite Stocks",
                             command=lambda: controller.show_frame(FavoriteStocks))
        button2.grid(row=31, column=1, sticky="wens")


app = SeaofStocks()
app.mainloop()
