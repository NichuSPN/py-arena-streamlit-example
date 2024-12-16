import streamlit as st

st.title("CORONA")
st.subheader("A Simple Project Showcasing py-arena and Streamlit Integration")

# New content about Streamlit
st.header("What is Streamlit?")
st.write("""
Streamlit is an open-source Python framework designed for data scientists and AI/ML engineers to create dynamic data applications with minimal effort. 
With just a few lines of code, you can build and deploy powerful data apps in minutes. Streamlit allows you to visualize data, build dashboards, 
and create user interfaces without extensive web development skills.

### Key Features of Streamlit:
- **Simplicity**: Write your app in pure Python, and Streamlit handles the rest.
- **Real-time Updates**: Automatically update your app as you change your code.
- **Interactive Widgets**: Easily add sliders, buttons, and text inputs to enhance user experience.
- **Integration**: Seamlessly integrate with popular data science libraries like NumPy, Pandas, and Matplotlib.
- **Deployment**: Use Streamlit Community Cloud to deploy your apps easily and share them with others.

For more information, visit the [Streamlit Documentation](https://docs.streamlit.io/get-started).
""")

# New content about py-arena
st.header("What is py-arena?")
st.write("""
**py-arena** is an API and Relational Engine for Network Applications. 
This package serves as a data and API access layer, providing a unified interface for interacting with various database systems and APIs. 
It simplifies the process of database management and API interactions, making it easier for developers to build robust applications.

### Key Features of py-arena:
- **Unified API**: Interact with multiple database systems (PostgreSQL, MySQL, SQLite) through a single interface.
- **API Handler**: An easy-to-use handler for making HTTP requests, allowing for seamless integration with external APIs.
- **Template-based SQL Query Resolution**: Simplifies the creation of SQL queries by using templates, reducing the risk of errors.
- **Callback Functions**: Support for callback functions on API requests, enabling better handling of asynchronous operations.

With py-arena, developers can focus on building their applications without worrying about the complexities of database interactions and API management.
For Source code visit [py-arena Repository](https://github.com/NichuSPN/py-arena)
""")

# Credits for data source
st.markdown("""
### Data Source
This application uses data from the [COVID Tracking Project](https://covidtracking.com/data/api).
""")
