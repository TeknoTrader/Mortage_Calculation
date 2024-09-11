import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

money = "$"

def calculate_monthly_payment(P, annual_rate, years):
    r = annual_rate / 12 / 100  # Monthly interest rate
    n = years * 12  # Total number of payments
    payment = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return payment, r, n

def calculate_amortization(P, payment, r, n):
    remaining_principal = P
    payments = []
    interest_totals = []
    principal_totals = []

    for _ in range(int(n)):
        interest = remaining_principal * r
        principal = payment - interest
        remaining_principal -= principal

        payments.append(payment)
        interest_totals.append(interest)
        principal_totals.append(principal)

    return payments, interest_totals, principal_totals

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

def main():
    st.title("Interactive Mortgage Calculator")

    # Input fields
    P = st.number_input("Loan amount ($)", min_value=1000, value=200000, step=1000)
    annual_rate = st.number_input("Annual interest rate (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    years = st.number_input("Loan term (years)", min_value=1, max_value=50, value=30, step=1)

    if st.button("Calculate"):
        payment, r, n = calculate_monthly_payment(P, annual_rate, years)
        payments, interest_totals, principal_totals = calculate_amortization(P, payment, r, n)

        st.divider()
        st.write(f"# Payment total: {money}{sum(interest_totals) + sum(principal_totals):.2f}")
        st.write(f"# Monthly Payment: {money}{payment:.2f}")

        # Create and display interactive plots
        fig = create_interactive_plots(payments, interest_totals, principal_totals, int(n))
        st.plotly_chart(fig)

        # Display amortization schedule
        st.subheader("Amortization Schedule (all in " + money + ")")
        df = pd.DataFrame({
            "Payment": range(1, int(n)+1),
            "Payment Amount": payments,
            "Principal": principal_totals,
            "Interest": interest_totals,
            "Remaining Balance": P - np.cumsum(principal_totals)
        })
        st.dataframe(df)

if __name__ == "__main__":
    main()
