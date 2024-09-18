# Differenze percentuali rispetto allo scenario iniziale
st.subheader("Differenze Percentuali rispetto allo Scenario Iniziale")
diff_avg = (avg_final_cost - loan_amount) / loan_amount * 100
diff_best = (best_scenario_cost - loan_amount) / loan_amount * 100
diff_worst = (worst_scenario_cost - loan_amount) / loan_amount * 100

st.write(f"Scenario Medio: {diff_avg:.2f}% ({'+' if diff_avg > 0 else ''}€{avg_final_cost - loan_amount:,.2f})")
st.write(f"Miglior Scenario: {diff_best:.2f}% ({'+' if diff_best > 0 else ''}€{best_scenario_cost - loan_amount:,.2f})")
st.write(f"Peggior Scenario: {diff_worst:.2f}% ({'+' if diff_worst > 0 else ''}€{worst_scenario_cost - loan_amount:,.2f})")

# Considerazioni sugli scenari
st.subheader("Considerazioni sugli Scenari")
st.write(f"""
Miglior Scenario:
- Il tasso di interesse potrebbe scendere fino al {best_scenario_rate:.2f}%.
- In questo caso, il costo totale del mutuo sarebbe di €{best_scenario_cost:,.2f}, con un potenziale risparmio di €{loan_amount - best_scenario_cost:,.2f}.

Peggior Scenario:
- Il tasso di interesse potrebbe salire fino al {worst_scenario_rate:.2f}%.
- In questo caso, il costo totale del mutuo salirebbe a €{worst_scenario_cost:,.2f}, con un aumento di €{worst_scenario_cost - loan_amount:,.2f}.

La maggior parte degli scenari si collocherà tra questi due estremi, con una tendenza verso il tasso medio finale del {avg_final_rate:.2f}%.
""")

if page == "Dati Storici":
    st.subheader("Dati Storici Utilizzati")
    st.line_chart(historical_rates.set_index('date')['value'])
    st.write(f"Nota: I dati storici mostrati sono i rendimenti del Treasury a 13 settimane degli ultimi {historical_years} anni. Questi dati sono stati utilizzati per calcolare la volatilità storica e il tasso iniziale per la simulazione.")
