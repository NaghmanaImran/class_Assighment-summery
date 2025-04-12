import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

class GrowthMindsetApp:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
    
    def display_principles(self):
        st.title("🌱 Growth Mindset Principles")
        principles = [
            "Embrace Challenges: See obstacles as opportunities for growth.",
            "Learn from Criticism: Use feedback to improve and grow.",
            "Persist in the Face of Setbacks: Keep going even when things get tough.",
            "Effort Leads to Mastery: Hard work and dedication lead to success.",
            "Learn from Others' Success: Be inspired rather than discouraged by others' achievements."
        ]
        for principle in principles:
            st.markdown(f"- {principle}")
    
    def display_data(self):
        st.header("📊 Dataset Overview")
        st.write(self.df.head())
        
        # DataSweeper (Basic Filters)
        st.sidebar.header("🔍 Data Filters")
        column = st.sidebar.selectbox("Select Column to Filter", self.df.columns)
        unique_values = self.df[column].unique()
        selected_values = st.sidebar.multiselect("Select Values", unique_values, default=unique_values)
        filtered_df = self.df[self.df[column].isin(selected_values)]
        st.write(filtered_df)
    
    def visualize_data(self):
        st.header("📈 Data Visualization")
        chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])
        x_axis = st.selectbox("Select X-axis", self.df.columns)
        y_axis = st.selectbox("Select Y-axis", self.df.columns)
        
        plt.figure(figsize=(8, 5))
        if chart_type == "Bar Chart":
            sns.barplot(x=self.df[x_axis], y=self.df[y_axis])
        elif chart_type == "Line Chart":
            sns.lineplot(x=self.df[x_axis], y=self.df[y_axis])
        elif chart_type == "Scatter Plot":
            sns.scatterplot(x=self.df[x_axis], y=self.df[y_axis])
        
        st.pyplot(plt)
    
    def run(self):
        self.display_principles()
        self.display_data()
        self.visualize_data()

if __name__ == "__main__":
    st.sidebar.title("🚀 Growth Mindset App")
    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file is not None:
        app = GrowthMindsetApp(uploaded_file)
        app.run()
    else:
        st.warning("Please upload a CSV file to proceed.")
