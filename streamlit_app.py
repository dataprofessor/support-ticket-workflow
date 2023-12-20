import streamlit as st

st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

tabs = (['Write a ticket', 'Ticket Status and Analytics'])

with tabs[0]:
  st.write('File a new ticket')



with tabs[1]:
  st.write('Check the status of your ticket')
