import streamlit as st

st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

tab1, tab2 = (['Write a ticket', 'Ticket Status and Analytics'])

with tab1:
  st.write('File a new ticket')

  with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

  if submit:
      col2.title(f'{a+b:.2f}')

with tab2:
  st.write('Check the status of your ticket')
