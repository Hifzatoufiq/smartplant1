import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os




st.set_page_config(
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

# ... Your existing code ...

# Custom CSS for styling
custom_css = """
<style>
/* Add your custom CSS styles here */

/* Example styles for the sidebar */
.sidebar .sidebar-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.sidebar img {
    margin-bottom: 10px; /* Add margin to the bottom of the image */
    border-radius: 50%;
}

/* Example styles for the tables */
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #5C5E62;
    color: white;
}
.st-emotion-cache-79elbk eczjsme10{
  background-color: #5C5E62;
}

/* Add more styles as needed */

</style>
"""




st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://scontent.fkhi21-1.fna.fbcdn.net/v/t39.30808-6/302424089_549936696883486_6803970556109482786_n.png?_nc_cat=101&ccb=1-7&_nc_sid=efb6e6&_nc_ohc=e_SxF0pGy4QAX_Se-wS&_nc_ht=scontent.fkhi21-1.fna&oh=00_AfAiX2AcKzaUBArx7z3foEyZgvJMvfVvKXetVCXlR3Hsig&oe=65AE4A60');
                background-repeat: no-repeat;
               background-size: 120px;
                padding-top: 120px;
                background-position: 20px 20px;
            }
           
           
        </style>
        """,
        unsafe_allow_html=True,
    )








st.markdown("<div style='text-align: center; font-size: 40px; font-weight: bold;'>Schedule production work order</div>", unsafe_allow_html=True)

def main():
    # Define a list of robots
    robot_options = ["Robot1", "Robot2", "Robot3", "Robot4"]

    # Create a single line for selecting a robot and date range
    selected_robot, start_date, end_date = st.columns([1, 1, 1])

    # Dropdown menu to select a robot
    selected_robot = selected_robot.selectbox("Select a Robot", robot_options)

    # Date range inputs for start and end dates
    default_end_date = datetime.now().date()
    default_start_date = default_end_date - timedelta(days=7)  # Default to a 7-day range
    start_date = start_date.date_input("Start Date", default_start_date)
    end_date = end_date.date_input("End Date", default_end_date)

    # Display the selected robot and date range
    #st.write(f"You selected: {selected_robot}, Start Date: {start_date}, End Date: {end_date}")


if __name__ == "__main__":
    main()
    data2 = {
        'order id ': ['1', '2'],
        'Order name<br>(Part description)': ['PICKUP FRAME', 'V6_Gate_Tail'],
        'weekly Quantity': ['50', '50'],
        #'Robot ID': ['yakshawa 3', 'yakshawa 4'],
    }

    # second dataframe
    df2 = pd.DataFrame(data2)

    styled_df2 = df2.style.hide(axis="index").set_table_styles([
        {'selector': '', 'props': [('background-color', '#FFFFFF'), ('color', 'Black')]},
        {'selector': 'th', 'props': [('background-color', '#FFFFFF'), ('color', 'black')]},
    ])

    # Convert the styled DataFrame to HTML
    html_code = styled_df2.to_html(escape=False)

    # Manipulate the HTML string to include the width property
    html_code = html_code.replace('<table', '<table style="width:1000px;"')

    st.markdown(html_code, unsafe_allow_html=True)

    # Add a horizontal rule with black color
    st.markdown("<hr style='border: 2px solid #D5D9E4;'>", unsafe_allow_html=True)

    data2 = {
        'order id ': ['1', '1', '1'],
        'child component<br> name)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790'],
        #'Quantity<br> (needed per Father)': ['1', '1', '1'],
        'Quantity to be produced': ['50', '50', '50'],
    }

    df2 = pd.DataFrame(data2)

    styled_df2 = df2.style.hide(axis="index").set_table_styles([
        {'selector': '', 'props': [('background-color', '#FFFFFF'), ('color', 'black')]},
        {'selector': 'th', 'props': [('background-color', '#FFFFFF'), ('color', 'black')]},
    ])

    # Convert the styled DataFrame to HTML
    html_code = styled_df2.to_html(escape=False)

    # Manipulate the HTML string to include the width property
    html_code = html_code.replace('<table', '<table style="width:1000px;"')

    st.markdown(html_code, unsafe_allow_html=True)
     

# Create the columns
col1, col2, col3, col4, col5 = st.columns(5)

# Add content to each column
with col1:
    # Add content to col1 if needed
    pass

with col2:
    # Add content to col2 if needed
    pass

with col3:
    # Apply inline styling to create a button
    st.markdown(
        """
        <button style="
            background-color: #3498db;
            color: #ffffff;
            width: 200px;
            height: 50px;
            margin-top: 20px;
            border-color:#3498db;
            border-radius: 2%;
            border: 1px solid #3498db ;
            ">
            Send Order to Robot
        </button>
        """,
        unsafe_allow_html=True
    )

with col4:
    # Add content to col4 if needed
    pass

with col5:
    # Add content to col5 if needed
    pass




