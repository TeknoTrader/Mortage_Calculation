import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

money = "$"

def main():
    # JavaScript to detect mobile devices and set a URL parameter
    device_detector = """
    <script>
    function detectMobile() {
        return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    }
    if (detectMobile()) {
        window.location.href = window.location.href + (window.location.href.indexOf('?') > -1 ? '&' : '?') + 'is_mobile=true';
    }
    </script>
    """
    html(device_detector)

    # Check if the user is on a mobile device using st.query_params
    is_mobile = st.query_params.get('is_mobile') == 'true'

    st.title("Interactive Mortgage Calculator")

    # Input fields
    P = st.number_input("Loan amount ($)", min_value=1000, value=200000, step=1000)
    annual_rate = st.number_input("Annual interest rate (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    years = st.number_input("Loan term (years)", min_value=1, max_value=50, value=30, step=1)
    start_date = st.date_input("Starting date", value=datetime.now().date())

    # Set default representation based on device type
    default_representation = "Image" if is_mobile else "Interactive"
    representation = st.radio("Representation method: ", ["Interactive", "Image"],
                              index=["Interactive", "Image"].index(default_representation))

    if st.button("Calculate"):
        payment, r, n = calculate_monthly_payment(P, annual_rate, years)
        payments, interest_totals, principal_totals = calculate_amortization(P, payment, r, n)

        # Generate dates for each payment
        dates = [start_date + timedelta(days=30 * i) for i in range(int(n))]

        if representation == "Interactive":
            st.divider()
            st.write(f"# Payment total: ${sum(interest_totals) + sum(principal_totals):.2f}")
            st.write(f"# Monthly Payment: ${payment:.2f}")

            # Create and display interactive plots
            fig = create_interactive_plots(payments, interest_totals, principal_totals, int(n))
            st.plotly_chart(fig)

            # Create and display interactive plots2
            fig = create_interactive_plots2(dates, payments, interest_totals, principal_totals)
            st.plotly_chart(fig)

            # Display amortization schedule
            st.subheader("Amortization Schedule (all in $)")
            df = pd.DataFrame({
                "Date": dates,
                "Payment Amount": payments,
                "Principal": principal_totals,
                "Interest": interest_totals,
                "Remaining Balance": P - np.cumsum(principal_totals)
            })
            st.dataframe(df)
        else:
            st.divider()
            st.write(f"# Payment total: ${sum(interest_totals) + sum(principal_totals):.2f}")
            st.write(f"# Monthly Payment: ${payment:.2f}")

            # Image representation
            fig = plot_graphs(payments, interest_totals, principal_totals, int(n))
            st.pyplot(fig)

            # Create and display interactive plots2
            fig = create_interactive_plots2(dates, payments, interest_totals, principal_totals)
            st.plotly_chart(fig)

            # Display amortization schedule
            st.subheader("Amortization Schedule (all in $)")
            df = pd.DataFrame({
                "Date": dates,
                "Payment Amount": payments,
                "Principal": principal_totals,
                "Interest": interest_totals,
                "Remaining Balance": P - np.cumsum(principal_totals)
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
    ax1.plot(months, np.cumsum(interest_totals), label='Total Interest Paid', color='red')
    ax1.plot(months, np.cumsum(principal_totals), label='Total Principal Repaid', color='blue')
    ax1.plot(months, np.cumsum(payments), label='Total Amount Paid', color='green', linestyle='--')

    ax1.set_xlabel('Payment Number')
    ax1.set_ylabel(f'Amount ({money})')
    ax1.set_title('Mortgage Payment Breakdown')
    ax1.legend()
    ax1.grid(True)

    # Pie chart
    total_interest_paid = np.sum(interest_totals)
    total_principal_repaid = np.sum(principal_totals)

    labels = [f'Interest: {round(sum(interest_totals), 2)}{money}',
              f'Principal: {round(sum(principal_totals), 2)}{money}']
    sizes = [total_interest_paid, total_principal_repaid]
    colors = ['red', 'blue']
    explode = (0.1, 0)

    ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax2.set_title(f'Total Payment: {round(sum(payments), 2)}{money}')

    plt.tight_layout()
    return fig

def create_interactive_plots(payments, interest_totals, principal_totals, n):
    months = np.arange(1, n + 1)

    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Mortgage Payment Breakdown", "Total Payment Breakdown"),
                        specs=[[{"type": "xy"}, {"type": "domain"}]])

    # Line chart
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(interest_totals), name='Total Interest Paid', line=dict(color='red')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(principal_totals), name='Total Principal Repaid', line=dict(color='blue')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=months, y=np.cumsum(payments), name='Total Amount Paid', line=dict(color='green', dash='dash')),
        row=1, col=1
    )

    # Update line chart layout
    fig.update_xaxes(title_text="Payment Number", row=1, col=1)
    fig.update_yaxes(title_text=f"Amount ({money})", row=1, col=1)

    # Pie chart
    total_interest_paid = np.sum(interest_totals)
    total_principal_repaid = np.sum(principal_totals)

    fig.add_trace(
        go.Pie(
            labels=['Interest', 'Principal'],
            values=[total_interest_paid, total_principal_repaid],
            textinfo='label+percent',
            insidetextorientation='radial',
            marker=dict(colors=['red', 'blue']),
            hole=0.3
        ),
        row=1, col=2
    )

    # Update layout
    fig.update_layout(height=600, width=1000, title_text="Mortgage Analysis")

    return fig

def create_interactive_plots2(dates, payments, interest_totals, principal_totals):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=("Payment Breakdown", "Balance Over Time"))

    # Payment breakdown
    fig.add_trace(go.Scatter(x=dates, y=principal_totals, name="Principal", fill='tozeroy'), row=1, col=1)
    fig.add_trace(go.Scatter(x=dates, y=interest_totals, name="Interest", fill='tonexty'), row=1, col=1)

    # Balance over time
    balance = [sum(payments) - sum(principal_totals[:i + 1]) for i in range(len(payments))]
    fig.add_trace(go.Scatter(x=dates, y=balance, name="Remaining Balance"), row=2, col=1)

    fig.update_layout(height=700, title_text="Mortgage Amortization")
    return fig


if __name__ == "__main__":
    main()
