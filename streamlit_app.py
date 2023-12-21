import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='Support Ticket Workflow', page_icon='🎫', layout='wide')
st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-top: 1.2rem;
    padding-bottom: 0rem;
}

</style>
""", unsafe_allow_html=True)

# Generate data
## Set seed for reproducibility
np.random.seed(42)

## Function to generate a random issue description
def generate_issue():
    issues = [
        "Network connectivity issues in the office",
        "Software application crashing on startup",
        "Printer not responding to print commands",
        "Email server downtime",
        "Data backup failure",
        "Login authentication problems",
        "Website performance degradation",
        "Security vulnerability identified",
        "Hardware malfunction in the server room",
        "Employee unable to access shared files",
        "Database connection failure",
        "Mobile application not syncing data",
        "VoIP phone system issues",
        "VPN connection problems for remote employees",
        "System updates causing compatibility issues",
        "File server running out of storage space",
        "Intrusion detection system alerts",
        "Inventory management system errors",
        "Customer data not loading in CRM",
        "Collaboration tool not sending notifications"
    ]
    return np.random.choice(issues)

## Function to generate random dates
start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 12, 20)
id_values = ['TICKET-{}'.format(i) for i in range(1000, 1100)]
issue_list = [generate_issue() for _ in range(100)]

def generate_random_dates(start_date, end_date, id_values):
    date_range = pd.date_range(start_date, end_date).strftime('%m-%d-%Y')
    return np.random.choice(date_range, size=len(id_values), replace=False)

## Generate 100 rows of data
data = {'Issue': issue_list,
        'Status': np.random.choice(['Open', 'In Progress', 'Closed'], size=100),
        'Priority': np.random.choice(['High', 'Medium', 'Low'], size=100),
        'Date': generate_random_dates(start_date, end_date, id_values)
    }
df = pd.DataFrame(data)
df = df.sort_values(by='Date', ascending=True)
# df['ID'] = id_values
df.insert(0, 'ID', id_values)

## Create DataFrame
if 'df' not in st.session_state:
    st.session_state.df = df

# Tabs for app layout
tabs = st.tabs(['Write a ticket', 'Ticket Status and Analytics'])

recent_ticket_number = int(max(st.session_state.df.ID).split('-')[1])

with tabs[0]:
  st.write('File a new ticket')

  with st.form('addition'):
    issue = st.text_area('Description of issue')
    priority = st.selectbox('Priority', ['High', 'Medium', 'Low'])
    submit = st.form_submit_button('Submit')

  if submit:
      today_date = datetime.now().strftime('%m-%d-%Y')
      df2 = pd.DataFrame([{'ID': f'TICKET-{recent_ticket_number+1}',
                           'Issue': issue,
                           'Status': 'Open',
                           'Priority': priority,
                           'Date': today_date
                          }])
      st.write('Ticket submitted!')
      st.dataframe(df2, use_container_width=True, hide_index=True)
      st.session_state.df = pd.concat([st.session_state.df, df2], axis=0)

with tabs[1]:
  st.write('Check the status of your ticket')
  st.data_editor(st.session_state.df, use_container_width=True, hide_index=True, height=212,
                column_config={'Status': st.column_config.SelectboxColumn(
                                            'Status',
                                            help='Ticket status',
                                            options=[
                                                'Open',
                                                'In Progress',
                                                'Closed'
                                            ],
                                            required=True,
                                            ),
                               'Priority': st.column_config.SelectboxColumn(
                                           'Priority',
                                            help='Priority',
                                            options=[
                                                'High',
                                                'Medium',
                                                'Low'
                                            ],
                                            required=True,
                                            ),
                             })
  st.write(f'Number of tickets: `{len(st.session_state.df)}`')

  df_status = st.session_state.df
  # Convert "Date" to datetime format
  df_status['Date'] = pd.to_datetime(df_status['Date'])
    
  # Extract month and year from the "Date" column
  df_status['Month'] = df_status['Date'].dt.strftime('%b-%Y')
    
  # Group by Month and Status, then count occurrences
  df_status_grouped = df_status.groupby(['Month', 'Status']).size().reset_index(name='Count')
    
  # Create grouped bar chart with Altair
  status_plot = alt.Chart(df_status_grouped).mark_bar().encode(
        x='Month:T',
        y='Count:Q',
        color='Status:N'
  )
  st.altair_chart(status_plot)
  df_status_grouped
  
