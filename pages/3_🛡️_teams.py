import streamlit as st

st.set_page_config(page_title='Fifa 23', page_icon=':soccer:', layout='wide')

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index.tolist()
club = st.sidebar.selectbox('Clube', clubes)

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f'## {club}')

columns = ['Age', 'Position', 'Photo', 'Flag', 'Overall', 'Value(£)', 'Wage(£)', 'Release Clause(£)', 'Height(cm.)', 'Weight(lbs.)']
st.dataframe(df_filtered[columns], column_config={
    "Overall": st.column_config.ProgressColumn(
        "Overall", min_value=0, max_value=100, format='%d'
    ), 
    "Wage(£)": st.column_config.ProgressColumn(
        "Wage(£)", min_value=0, max_value=df_filtered['Wage(£)'].max(), format='€%d'
    ),
    "Photo": st.column_config.ImageColumn(), 
    "Flag": st.column_config.ImageColumn('Country'), 
    
    })