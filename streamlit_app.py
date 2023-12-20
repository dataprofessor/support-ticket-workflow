import streamlit as st

st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-top: 1rem;
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

## Generate 100 rows of data
data = {
    'ID': ['TICKET-{}'.format(i) for i in range(1000, 1100)],
    'Issue': [generate_issue() for _ in range(100)],
    'Status': np.random.choice(['Open', 'In Progress', 'Resolved', 'Closed'], size=100),
    'Priority': np.random.choice(['High', 'Medium', 'Low'], size=100)
}

## Create DataFrame
df = pd.DataFrame(data)

# Tabs for app layout
tabs = st.tabs(['Write a ticket', 'Ticket Status and Analytics'])

with tabs[0]:
  st.write('File a new ticket')

  with st.form('addition'):
    cost_center_list = ['HR001 Human Resources',
                        'IT002 Information Technology',
                        'MKT003 Marketing',
                        'FIN004 Finance',
                        'OPS005 Operations']
    issue = st.text_area('Description of issue')
    cost_center_selection = st.selectbox('Cost center', cost_center_list)
    deadline = st.date_input('Deadline', value=None)
    submit = st.form_submit_button('Submit')

  if submit:
      s = pd.Series()
      st.write('Ticket submitted!')

with tabs[1]:
  st.write('Check the status of your ticket')
