import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

money = "$" #,"€","¥","₽",

# Translations dictionary
translations = {
    'en': {
        'title': "Interactive Mortgage Calculator",
        'loan_amount': "Loan amount (" + money + ")",
        'annual_rate': "Annual interest rate (%)",
        'loan_term': "Loan term (years)",
        'start_date': "Starting date",
        'representation': "Representation method: ",
        'interactive': "Interactive",
        'image': "Image",
        'calculate': "Calculate",
        'payment_total': "Payment total: " + money,
        'monthly_payment': "Monthly Payment: " + money,
        'amortization_schedule': "Amortization Schedule (all in " + money + ")",
        'date': "Date",
        'payment_amount': "Payment Amount",
        'principal': "Principal",
        'interest': "Interest",
        'remaining_balance': "Remaining Balance",
        'payment_breakdown': "Payment Breakdown",
        'balance_over_time': "Balance Over Time",
        'mortgage_amortization': "Mortgage Amortization",
        'total_interest': "Total Interest Paid",
        'total_capital': "Total Principal Repaid",
        'total_paid': "Total Amount Paid",
        'amount': "Amount (" + money + ")",
        'tp': "Total Payment Breakdown",
        'mp': "Mortgage Payment Breakdown",
        'ma': "Mortgage analysis",
        'mam': "Mortgage amortization",
        'tot': "Total Payment",
        'warning': "If you are from a MOBILE DEVICE please ROTATE IT or switch the \"representation\" from \"Interactive\" to \"Image\""
    },
    'it': {
        'title': "Calcolatore Interattivo di Mutui",
        'loan_amount': "Importo del prestito (" + money + ")",
        'annual_rate': "Tasso di interesse annuale (%)",
        'loan_term': "Durata del prestito (anni)",
        'start_date': "Data di inizio",
        'representation': "Metodo di rappresentazione: ",
        'interactive': "Interattivo",
        'image': "Immagine",
        'calculate': "Calcola",
        'payment_total': "Totale pagamenti: " + money,
        'monthly_payment': "Rata mensile: " + money,
        'amortization_schedule': "Piano di Ammortamento (tutto in " + money + ")",
        'date': "Data",
        'payment_amount': "Importo Rata",
        'principal': "Capitale",
        'interest': "Interessi",
        'remaining_balance': "Saldo Rimanente",
        'payment_breakdown': "Suddivisione dei Pagamenti",
        'balance_over_time': "Saldo nel Tempo",
        'mortgage_amortization': "Ammortamento del Mutuo",
        'total_interest': "Totale Interessi Pagati",
        'total_capital': "Totale Capitale Rimborsato",
        'total_paid': "Totale Versato",
        'amount': "Denaro (" + money + ")",
        'tp': "Ripartizione totale pagamenti",
        'mp': "Ripartizione pagamento mutuo",
        'ma': "Analisi del mutuo",
        'mam': "Ammortamento del mutuo",
        'tot': "Pagamento totale",
        'warning': "Se fai accesso DA TELEFONO, ruota lo schermo o cambia la \"rappresentazione\" da \"Interattiva\" a \"Immagine\""
    },
    'ru': {
        'title': "Интерактивный Калькулятор Ипотеки",
        'loan_amount': "Сумма кредита (" + money + ")",
        'annual_rate': "Годовая процентная ставка (%)",
        'loan_term': "Срок кредита (лет)",
        'start_date': "Дата начала",
        'representation': "Метод представления: ",
        'interactive': "Интерактивный",
        'image': "Изображение",
        'calculate': "Рассчитать",
        'payment_total': "Общая сумма выплат: " + money,
        'monthly_payment': "Ежемесячный платеж: " + money,
        'amortization_schedule': "График погашения (все в " + money + ")",
        'date': "Дата",
        'payment_amount': "Сумма платежа",
        'principal': "Основной долг",
        'interest': "Проценты",
        'remaining_balance': "Остаток долга",
        'payment_breakdown': "Разбивка платежей",
        'balance_over_time': "Изменение баланса во времени",
        'mortgage_amortization': "Амортизация ипотеки",
        'total_interest': "общая сумма выплаченных процентов",
        'total_capital': "общая сумма погашенной основной суммы долга",
        'total_paid': "общая сумма выплачена",
        'amount': "деньги (" + money + ")",
        'tp': "Общая разбивка платежей",
        'mp': "Разбивка платежей по ипотеке",
        'ma': "Ипотечный анализ",
        'mam': "Амортизация ипотеки",
        'tot': "Общее количество страниц",
        'warning': "Если вы используете МОБИЛЬНОЕ УСТРОЙСТВО, ПОВЕРНИТЕ ЕГО или переключите «представление» с «Интерактивного» на «Изображение»."
    }
}

# Language selection
lang = st.selectbox("Language / Lingua / Язык", ['en', 'it', 'ru'])
t = translations[lang]

def main():
    is_mobile = 'true'

    st.title(t['title'])

    # INPUT FIELDS

    P = st.number_input(t['loan_amount'], min_value=1000, value=200000, step=1000)
    annual_rate = st.number_input(t['annual_rate'], min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    years = st.number_input(t['loan_term'], min_value=1, max_value=50, value=30, step=1)
    start_date = st.date_input(t['start_date'], value=datetime.now().date())

    # Set default representation based on device type
    default_representation = t['image'] if is_mobile else t['interactive']
    representation = st.radio(t['representation'], [t['interactive'], t['image']],
                              index=[t['image'], t['interactive']].index(default_representation))

    if st.button(t['calculate']):
        payment, r, n = calculate_monthly_payment(P, annual_rate, years)
        payments, interest_totals, principal_totals = calculate_amortization(P, payment, r, n)

        # Generate dates for each payment
        dates = [start_date + timedelta(days=30 * i) for i in range(int(n))]

        if representation == t['interactive']:
            st.divider()
            st.warning(t['warning'])
            st.write(f"# {t['payment_total']} {sum(interest_totals) + sum(principal_totals):.2f}")
            st.write(f"# {t['monthly_payment']}{payment:.2f}")

            # Create and display interactive plots
            fig = create_interactive_plots(payments, interest_totals, principal_totals, int(n))
            st.plotly_chart(fig)

            # Create and display interactive plots2
            fig = create_interactive_plots2(dates, payments, interest_totals, principal_totals)
            st.plotly_chart(fig)

            # Display amortization schedule
            st.subheader(t['amortization_schedule'])
            df = pd.DataFrame({
                t['date']: dates,
                t['payment_amount']: payments,
                t['principal']: principal_totals,
                t['interest']: interest_totals,
                t['remaining_balance']: P - np.cumsum(principal_totals)
            })
            st.dataframe(df)
        else:
            st.divider()
            st.write(f"# {t['payment_total']}{sum(interest_totals) + sum(principal_totals):.2f}")
            st.write(f"# {t['monthly_payment']}{payment:.2f}")

            # Image representation
            fig = plot_graphs(payments, interest_totals, principal_totals, int(n))
            st.pyplot(fig)

            # Create and display interactive plots2
            fig = create_interactive_plots2(dates, payments, interest_totals, principal_totals)
            st.plotly_chart(fig)

            # Display amortization schedule
            st.subheader(t['amortization_schedule'])
            df = pd.DataFrame({
                t['date']: dates,
                t['payment_amount']: payments,
                t['principal']: principal_totals,
                t['interest']: interest_totals,
                t['remaining_balance']: P - np.cumsum(principal_totals)
            })
            st.dataframe(df)


def calculate_monthly_payment(P, annual_rate, years):
    r = annual_rate / 100 / 12  # monthly interest rate
    n = years * 12  # number of monthly payments
    payment = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return payment, r, n


def calculate_amortization(P, payment, r, n):
    payments = []
    interest_totals = []
    principal_totals = []
    balance = P
    for _ in range(int(n)):
        interest = balance * r
        principal = payment - interest
        balance -= principal
        payments.append(payment)
        interest_totals.append(interest)
        principal_totals.append(principal)
    return payments, interest_totals, principal_totals

def plot_graphs(payments, interest_totals, principal_totals, n):
    months = np.arange(1, n + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Line graph
    ax1.plot(months, np.cumsum(interest_totals), label=t['total_interest'], color='red')
    ax1.plot(months, np.cumsum(principal_totals), label=t['total_capital'], color='blue')
    ax1.plot(months, np.cumsum(payments), label=t['total_paid'], color='green', linestyle='--')

    ax1.set_xlabel('Payment Number')
    ax1.set_ylabel(t['amount'])
    ax1.set_title(t['mp'])
    ax1.legend()
    ax1.grid(True)

    # Pie chart
    total_interest_paid = np.sum(interest_totals)
    total_principal_repaid = np.sum(principal_totals)

    labels = [f'{t['interest']}: {round(sum(interest_totals), 2)}{money}',
              f'{t['principal']}: {round(sum(principal_totals), 2)}{money}']
    sizes = [total_interest_paid, total_principal_repaid]
    colors = ['red', 'blue']
    explode = (0.1, 0)

    ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax2.set_title(f'{t['tot']}: {round(sum(payments), 2)}{money}')

    plt.tight_layout()
    return fig

def create_interactive_plots(payments, interest_totals, principal_totals, n):
    months = np.arange(1, n + 1)

    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=(t['mp'], t['tp']),
                        specs=[[{"type": "xy"}, {"type": "domain"}]])

    # Line chart
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(interest_totals), name=t['total_interest'], line=dict(color='red')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(principal_totals), name=t['total_capital'], line=dict(color='blue')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(payments), name=t['total_paid'], line=dict(color='green', dash='dash')),
        row=1, col=1
    )

    # Update line chart layout
    fig.update_xaxes(title_text="Payment Number", row=1, col=1)
    fig.update_yaxes(title_text=t['amount'], row=1, col=1)

    # Pie chart
    total_interest_paid = np.sum(interest_totals)
    total_principal_repaid = np.sum(principal_totals)

    fig.add_trace(
        go.Pie(
            labels=[t['interest'], t['principal']],
            values=[total_interest_paid, total_principal_repaid],
            textinfo='label+percent',
            insidetextorientation='radial',
            marker=dict(colors=['red', 'blue']),
            hole=0.3
        ),
        row=1, col=2
    )

    # Update layout
    fig.update_layout(height=600, width=1000, title_text=t['ma'])

    return fig

def create_interactive_plots2(dates, payments, interest_totals, principal_totals):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=(t['payment_breakdown'], t['balance_over_time']))

    # Payment breakdown
    fig.add_trace(go.Scatter(x=dates, y=principal_totals, name=t['principal'], fill='tozeroy'), row=1, col=1)
    fig.add_trace(go.Scatter(x=dates, y=interest_totals, name=t['interest'], fill='tonexty'), row=1, col=1)

    # Balance over time
    balance = [sum(payments) - sum(principal_totals[:i + 1]) for i in range(len(payments))]
    fig.add_trace(go.Scatter(x=dates, y=balance, name=t['remaining_balance']), row=2, col=1)

    fig.update_layout(height=700, title_text=t['mam'])
    return fig


if __name__ == "__main__":
    main()
