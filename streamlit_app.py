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
      st.write('Ticket submitted!')

with tabs[1]:
  st.write('Check the status of your ticket')
