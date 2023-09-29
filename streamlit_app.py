import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set the page title and icon
st.set_page_config(
    page_title="Phone Comparator App",
    page_icon="📱"
)

plt.style.use('dark_background') 
# Load the CSV file into a DataFrame

def load_data():
    return pd.read_csv("phone_data.csv")


soft_df = load_data()
display_df = soft_df.groupby(["Sno", "Name", "Processor"])[["Ram", "Performance", "Battery Capacity"]].sum().reset_index()
compare_df = soft_df.groupby(["Sno", "Name", "Processor"])[["Performance", "Battery Capacity", "Front Camera", "Back Camera", "Screen Size"]].sum().reset_index()


# Sidebar
st.sidebar.header("Phone Comparator")

# Main content
st.title("Phone Comparator App")

# Function to compare phones by Antutu score
# Function to compare phones by Antutu Score
def filter_by_antutu_score():
    antutu_filter_comp_df = soft_df.groupby(["Sno", "Name"])["Performance"].sum().reset_index()
    st.subheader("Antutu Score Comparison")
    st.dataframe(antutu_filter_comp_df)

    # Plot a bar chart
    fig, ax = plt.subplots(figsize=(20, 6))
    ax.bar(antutu_filter_comp_df["Name"], antutu_filter_comp_df["Performance"])
    plt.xticks(rotation=90)
    plt.xlabel("Name")
    plt.ylabel("Performance")
    st.pyplot(fig)

# Function to compare phones by Battery Capacity
def filter_by_battery():
    battery_filter_comp_df = soft_df.groupby(["Sno", "Name"])["Battery Capacity"].sum().reset_index()
    st.subheader("Battery Capacity Comparison")
    st.dataframe(battery_filter_comp_df)

    # Plot a bar chart
    fig, ax = plt.subplots(figsize=(20, 6))
    ax.bar(battery_filter_comp_df["Name"], battery_filter_comp_df["Battery Capacity"])
    plt.xticks(rotation=90)
    plt.xlabel("Name")
    plt.ylabel("Battery (mAh)")
    st.pyplot(fig)# Function to compare phones by company
def company_wise():
# Add a new text input for the brand name
        brand = st.text_input("Enter the company name you want to compare (e.g., Apple, Samsung, OnePlus, Google):")

        # Add a button to trigger the comparison
        if st.button("Compare"):
            # Check if the brand input is not empty
            if brand:
                brand = brand.lower()
                
                # Filter data based on the entered company name
                filtered_df = soft_df[soft_df["Company"].str.lower().str.contains(brand)]

                if not filtered_df.empty:
                    filtered_df = filtered_df.iloc[:, :-3]
                    st.subheader(f"Comparison for {brand.capitalize()} Phones")
                    st.dataframe(filtered_df)

                    # Create a bar chart for comparison
                    num_cols = filtered_df.select_dtypes(exclude=[object]).columns
                    df_grouped = filtered_df.groupby(["Name"])[num_cols].sum().round(1).reset_index()

                    fig = make_subplots(rows=4, cols=4,
                                        shared_xaxes=False,
                                        vertical_spacing=0.1,
                                        subplot_titles=num_cols)

                    i = j = 1
                    for col in num_cols:
                        fig.add_trace(go.Bar(x=df_grouped["Name"],
                                            y=df_grouped[col],
                                            text=df_grouped[col],
                                            textposition="inside",
                                            name=col), row=i, col=j)
                        j += 1
                        if j > 4:
                            j = 1
                            i += 1
                        if i > 4:
                            i = 1

                    fig.update_layout(height=2000, width=1500)
                    st.plotly_chart(fig)
                else:
                    st.error(f"No data available for {brand.capitalize()} phones.")
    
# Function to compare phones individually
def compare_phones():
    num_comparisons = st.selectbox("How many phones do you want to compare (Min: 1, Max: 5)?", [1, 2, 3, 4, 5], index=0)

    name_list = []
    for i in range(num_comparisons):
        phone_name = st.selectbox(f"Select Phone {i+1} for comparison:", compare_df["Name"].unique())
        name_list.append(phone_name)

    phones_to_compare = compare_df[compare_df["Name"].isin(name_list)]

    st.subheader("Phones to Compare")
    st.dataframe(phones_to_compare)

    if num_comparisons > 0:
        st.subheader("Comparison Radar Chart")
        phones_to_compare = phones_to_compare.set_index("Name")
        cols_for_radar = phones_to_compare[["Performance", "Battery Capacity", "Front Camera", "Back Camera", "Screen Size"]]

        # Normalize the data for radar chart
        max_vals = cols_for_radar.max()
        radar_data = cols_for_radar / max_vals

        # Create a radar chart
        fig = go.Figure()
        for index, row in radar_data.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.values,
                theta=row.index,
                fill='toself',
                name=index  # Use the phone name as the legend label
            ))

        fig.update_layout(
            bgcolor="#494b5a",
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=True,
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Set the paper background to black
            plot_bgcolor="rgba(0, 0, 0, 0)"
        )
    
        st.plotly_chart(fig)


# Main menu options
menu_option = st.sidebar.selectbox("Select an option:", ["Home", "Filter by Antutu Score", "Filter by Battery Capacity", "Company-wise Comparison", "Compare Phones"])

if menu_option == "Home":
    st.write("Welcome to the Phone Comparator App! Choose an option from the sidebar.")

elif menu_option == "Filter by Antutu Score":
    filter_by_antutu_score()

elif menu_option == "Filter by Battery Capacity":
    filter_by_battery()

elif menu_option == "Company-wise Comparison":
    company_wise()

elif menu_option == "Compare Phones":
    compare_phones()
