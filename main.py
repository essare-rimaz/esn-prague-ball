import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# for the map, has to be installed (pip install streamlit_folium)
#from streamlit_folium import st_folium 
#import folium

css_path = Path("style.css").resolve()
css_path = str(css_path)

st.set_page_config(layout="wide", initial_sidebar_state='expanded')

with open(css_path) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# DEFAULTS
provider_percentage_default = 7.00
ticket_fee_default = 6.50
tax_ticket_default = 12

rent_default = 98000
tax_perc_default = 21

buffer_default = 50000
band_expense_default = 21000
other_expenses_default = 0

esner_ticket_price_default = 500
esncard_holder_ticket_price_default = 650
standard_ticket_price_default = 750


# SIDEBAR
st.sidebar.header('Settings') # `version 2`')

st.sidebar.subheader('Tickets')

bool_apply_fees = st.sidebar.checkbox('Apply fees', value=True)
provider_percentage_value = st.sidebar.number_input("Provider's share (%)", key="provider_percentage", min_value=0.00, max_value=100.00, value=provider_percentage_default, step=0.01, label_visibility = "visible")
ticket_fee_value = st.sidebar.number_input("Ticket fee (CZK)", key="ticket_fee", min_value=0.00, max_value=100.00, value=ticket_fee_default, step=0.01, label_visibility = "visible")
tax_on_ticket_value = st.sidebar.number_input("Tax on ticket (%)", key="ticket_tax", min_value=0, max_value=100, value=tax_ticket_default, step=1, label_visibility = "visible")

st.sidebar.subheader('Expenses')
rent_value = st.sidebar.number_input("Rent (CZK)", key="rent_cost", min_value=0, max_value=1000000, value=rent_default, step=1, label_visibility = "visible")
tax_on_rent_perc = st.sidebar.number_input("Tax (%)", key="rent_tax_percentage", min_value=0, max_value=100, value=tax_perc_default, step=1, label_visibility = "visible")
total_rent_value = rent_value * ((100 + tax_on_rent_perc)/100)

buffer_expense_value = st.sidebar.number_input("Buffer (CZK)", key="buffer_expense", min_value=0, max_value=1000000, value=buffer_default, step=1, label_visibility = "visible")
band_expense_value = st.sidebar.number_input("Band cost (CZK)", key="rent_expense", min_value=0, max_value=1000000, value=band_expense_default, step=1, label_visibility = "visible")
other_expenses_value = st.sidebar.number_input("Other expenses (CZK)", key="other_expenses", min_value=0, max_value=1000000, value=other_expenses_default, step=1, label_visibility = "visible")

total_fix_expenses = total_rent_value + buffer_expense_value + band_expense_value + other_expenses_value

st.sidebar.markdown('''
---
Created with ❤️ by Tomas Pycha.
''')

st.header("ESN Prague Ball - Financial Analysis")

# MAP??
#m = folium.Map(location =[50.0771239, 14.4399050], zoom_start=16)
#folium.Marker(
#    [50.0771239, 14.4399050], popup="Radio Palace", tooltip="Radio Palace"
#).add_to(m)

#st_data = st_folium(m, width=500, height=500)



max_participants = 4000 # Not really total, but it's easier like this to fix bugs:)
participants = np.linspace(1, max_participants, max_participants)
number_org=20
deposit = total_rent_value * 0.25

if not bool_apply_fees:
    provider_percentage_value = 0
    ticket_fee_value = 0


col1, col2, col3, col4, col21 = st.columns([1, 1, 2, 1, 1])
col5, col6, col7, col8, col22 = st.columns([1, 1, 2, 1, 1])
col9, col10, col11, col12, col23 = st.columns([1, 1, 2, 1, 1])
col13, col14, col15, col16, col24 = st.columns([1, 1, 2, 1, 1])
col17, col18, col19, col20, col25 = st.columns([1, 1, 2, 1, 1])


# UPDATE SLIDER AND NUMERIC INPUT
#"st.session_state object:" , st.session_state
def update_slider():
    st.session_state.slider_org = st.session_state.numeric_org
    st.session_state.slider_esner = st.session_state.numeric_esner
    st.session_state.slider_esncard = st.session_state.numeric_esncard
    st.session_state.slider_standard = st.session_state.numeric_standard
def update_numin():
    st.session_state.numeric_org = st.session_state.slider_org
    st.session_state.numeric_esner = st.session_state.slider_esner
    st.session_state.numeric_esncard = st.session_state.slider_esncard
    st.session_state.numeric_standard = st.session_state.slider_standard


# PARTICIPANTS SELECTOR
with st.container():

    with col1:
        st.write("Category")
    with col2:
        st.write("Price (CZK)")
    with col3:
        st.write("Number of tickets")
    with col4:
        st.write("")
    with col21:
        st.write("Extra expense per person (CZK)")
with st.container():

    with col5:
        bool_org = st.checkbox('Organizers', value=True)
    with col6:
        price_org = st.number_input("Price", key="ahoj", min_value=0, max_value=1000, value=0, step=1, label_visibility = "collapsed")
    with col7:
        number_org_slider = st.slider("Tickets", key="slider_org", min_value=0, max_value=1000, value=20, step=1, format=None, help=None, on_change=update_numin, label_visibility="collapsed")
    with col8:
        number_org_numin = st.number_input("Price", key="numeric_org", min_value=0, max_value=1000, value=number_org_slider, step=1, on_change=update_slider, label_visibility = "collapsed")
    with col22:
        extra_expense_org = st.number_input("Náklady na účastníka", key="extra_org", min_value=0, max_value=1000, value=0, step=1, label_visibility = "collapsed")
with st.container():
    with col9:
        bool_esner = st.checkbox('ESNers', value=True)
    with col10:
        price_esner = st.number_input("Price", key="ahojj", min_value=0, max_value=1000, value=esner_ticket_price_default, step=1, label_visibility = "collapsed")
    with col11:
        number_esner_slider = st.slider("Tickets", key="slider_esner", min_value=0, max_value=1000, value=100, step=1, format=None, help=None, on_change=update_numin, label_visibility="collapsed")
    with col12:
        number_esner_numin = st.number_input("Price", key="numeric_esner", min_value=0, max_value=1000, value=number_esner_slider, step=1, on_change=update_slider, label_visibility = "collapsed")
    with col23:
        extra_expense_esner = st.number_input("Náklady na účastníka", key="extra_esner", min_value=0, max_value=1000, value=0, step=1, label_visibility = "collapsed")
with st.container():
    with col13:
        bool_esncard = st.checkbox('ESNcard holders', value=True)
    with col14:
        price_esncard = st.number_input("Price", key="ahojjj", min_value=0, max_value=1000, value=esncard_holder_ticket_price_default, step=1, label_visibility = "collapsed")
    with col15:
        number_esncard_slider = st.slider("Tickets", key="slider_esncard", min_value=0, max_value=1000, value=300, step=1, format=None, help=None, on_change=update_numin, label_visibility="collapsed")
    with col16:
        number_esncard_numin = st.number_input("Price", key="numeric_esncard", min_value=0, max_value=1000, value=number_esncard_slider, step=1, on_change=update_slider, label_visibility = "collapsed")
    with col24:
        extra_expense_esncard = st.number_input("Náklady na účastníka", key="extra_esncard", min_value=0, max_value=1000, value=0, step=1, label_visibility = "collapsed")
with st.container():
    with col17:
        bool_standard = st.checkbox('Standard', value=True)
    with col18:
        price_standard = st.number_input("Price", key="ahojjjj", min_value=0, max_value=1000, value=standard_ticket_price_default, step=1, label_visibility = "collapsed")
    with col19:
        number_standard_slider = st.slider("Tickets", key="slider_standard", min_value=0, max_value=1000, value=200, step=1, format=None, help=None, on_change=update_numin, label_visibility="collapsed")
    with col20:
        number_standard_numin = st.number_input("Price", key="numeric_standard", min_value=0, max_value=1000, value=number_standard_slider, step=1, on_change=update_slider, label_visibility = "collapsed")
    with col25:
        extra_expense_standard = st.number_input("Náklady na účastníka", key="extra_standard", min_value=0, max_value=1000, value=0, step=1, label_visibility = "collapsed")



category_bools = [bool_org,
                  bool_esner,
                  bool_esncard,
                  bool_standard
]
n_tickets_by_category = [number_org_slider, 
                         number_esner_slider,
                         number_esncard_slider,
                         number_standard_slider
                         ]
price_by_category = [price_org,
                     price_esner,
                     price_esncard,
                     price_standard    
]
extra_expense_by_category = [extra_expense_org,
                             extra_expense_esner,
                             extra_expense_esncard,
                             extra_expense_standard
]


# CALCULATIONS
income_vector = []
variable_expense_vector = []
fees_vector = []
income_vector = np.array(income_vector)
variable_expense_vector = np.array(variable_expense_vector)
fees_vector = np.array(fees_vector)
tax_on_tickets_vector = np.array(fees_vector)

for i in range(len(price_by_category)):
    if category_bools[i]:
        if price_by_category[i] > 0:
            income_vector = np.append(income_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i])   ### * (1 - (provider_percentage_value/100) - (tax_on_ticket_value/100)) - ticket_fee_value)
            fees_vector = np.append(fees_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i] * (provider_percentage_value)/100 + ticket_fee_value)
            tax_on_tickets_vector = np.append(tax_on_tickets_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i] * (tax_on_ticket_value)/(100 + tax_on_ticket_value))
            variable_expense_vector = np.append(variable_expense_vector, np.ones(n_tickets_by_category[i])*extra_expense_by_category[i])
        else:
            income_vector = np.append(income_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i])
            fees_vector = np.append(fees_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i])
            tax_on_tickets_vector = np.append(tax_on_tickets_vector, np.ones(n_tickets_by_category[i]) * price_by_category[i])
            variable_expense_vector = np.append(variable_expense_vector, np.ones(n_tickets_by_category[i])*extra_expense_by_category[i])
            
income_vector = np.cumsum(income_vector)
variable_expense_vector = np.cumsum(variable_expense_vector)
fees_vector = np.cumsum(fees_vector)
tax_on_tickets_vector = np.cumsum(tax_on_tickets_vector)

expense_vector = variable_expense_vector + np.ones(len(variable_expense_vector)) * total_fix_expenses + fees_vector + tax_on_tickets_vector
print(expense_vector[-1], variable_expense_vector[-1], total_fix_expenses, fees_vector[-1], tax_on_tickets_vector[-1])
profit_vector = np.subtract(income_vector, expense_vector[:len(income_vector)])

total_balance = int(profit_vector[-1])

if total_balance < 0:
    dif_vector = np.linspace(int(total_balance), 0, abs(total_balance)+1)
    dif_line_color = 'rgb(256,00,00)'
else:
    dif_vector = np.linspace(0, total_balance, abs(total_balance)+1)
    dif_line_color = 'rgb(00,256 ,00)'


# BODY DOWN
col31, col32 = st.columns([5, 5])

# GRAPH
with col31:
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=participants, y=income_vector, mode='lines', name='NET income'))
    fig.add_trace(go.Scatter(x=participants, y=-expense_vector, mode='lines', name='Expenses', line=dict(color='rgb(243, 119, 0)')))
    fig.add_trace(go.Scatter(x=participants, y=profit_vector, mode='lines', name='Balance', line=dict(color='rgb(200, 195, 30)')))
    fig.add_trace(go.Scatter(x=np.ones(len(dif_vector))*len(profit_vector), y=dif_vector, mode='lines', name='Difference', line=dict(color=dif_line_color)))


    fig.update_layout(title='Financial result depending on number of participants',
                    xaxis_title = 'Number of participants', 
                    yaxis_title = 'Financial result',
                    xaxis=dict(
                        showline=False, 
                        showgrid=True, 
                        showticklabels=True,
                        zeroline=True,
                        range=[0, 1000]
                        ),
                    yaxis=dict(
                        showline=True, 
                        showgrid=True, 
                        showticklabels=True,
                        zeroline=True,
                        zerolinecolor='rgb(82, 82, 82)',
                        zerolinewidth=3,
                        range=[-400000, 400000]
                        
                        ),
                    hovermode="x unified",
                    height=800,
                    width = 300
                    )
    st.plotly_chart(fig, use_container_width=True)


# STATS
with col32:

    with st.container():
        st.header('Incomes')
        col41, col42 = st.columns([1,1])
        with col41:
            st.metric("Total income", f'{int(income_vector[-1]):,} CZK')


    with st.container():
        st.header('Expenses')
        col44, x = st.columns([1,1])
        with col44:
            st.metric("Total expenses", f'{int(expense_vector[-1]):,} CZK')

    
    with st.container():
        col45, col46 = st.columns([1,1])
        with col45:
            st.metric("Rent expenses", f'{int(total_rent_value):,} CZK', "with TAX", delta_color="off")
            #st.metric("Total fixed expenses", f'{int(total_fix_expenses):,} CZK')
        with col46:
            st.metric("Deposit", f'{int(deposit):,} CZK', "included in Rent expenses", delta_color="off")
            #st.metric("Total fixed expenses", f'{int(total_fix_expenses):,} CZK')


    with st.container():
        col46, col47 = st.columns([1,1])
        with col46:
            st.metric("Provider fees", f'{int(fees_vector[-1]):,} CZK')
        with col47:
            st.metric("Tax on tickets", f'{int(tax_on_tickets_vector[-1]):,} CZK')

    with st.container():
        col48, col49 = st.columns([1,1])
        with col48:
            st.metric("Band expenses", f'{int(band_expense_value):,} CZK')
        with col49:
            st.metric("Buffer expenses", f'{int(buffer_expense_value):,} CZK')

    with st.container():
        col50, col51 = st.columns([1,1])
        with col50:
            st.header('Balance')
            st.metric("Total balance", f'{int(total_balance):,} CZK')