import streamlit as st

st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

tabs = st.tabs(['Write a ticket', 'Ticket Status and Analytics'])

with tabs[0]:
  st.write('File a new ticket')

  with st.form('addition'):
    a = st.text_area('Description of issue')
    b = st.text_input('Cost center')
    deadline = st.date_input('Deadline', value=None)
    submit = st.form_submit_button('Submit')

  if submit:
      st.write('Ticket submitted!')

with tabs[1]:
  st.write('Check the status of your ticket')
