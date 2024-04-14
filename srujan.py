import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def plot_bar_graph_features(filtered_data, feature_type):
    st.subheader(f"Number of Victims: Analysis by {feature_type}")
    # Count occurrences of the selected feature type
    feature_counts = filtered_data[feature_type].value_counts().sort_index()
    # Sort the values in descending order and select the top 10 values
    top_features = feature_counts.sort_values(ascending=False).head(10)
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(top_features.index, top_features.values)
    plt.xlabel(feature_type)
    plt.ylabel('Number of Victims')
    plt.title(f'Top 10 {feature_type} with Highest Number of Victims')
    plt.xticks(rotation=45)
    # Display the plot in Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def main():
    
    st.title('Spatial Analysis of Victim Database')

    file_path = 'modified_file.csv'
    data = pd.read_csv(file_path)

    # Widgets for selecting year and month
    selected_district = st.selectbox('Select District', [''] + sorted(data['District_Name'].unique()))
    
    # Filter data based on selected year and month
    filtered_data = data
    if selected_district:
        
        filtered_data = filtered_data[filtered_data['District_Name'] == selected_district]
        units_in_district = sorted(filtered_data['UnitName'].unique())
        selected_unit = st.selectbox('Select Unit Name', [''] + units_in_district)
        
        if not selected_unit:
                
            unit_counts = filtered_data['UnitName'].value_counts().sort_index()
            st.subheader(f"Number of Victims in {selected_district}")
            plt.figure(figsize=(10, 6))
            plt.bar(unit_counts.index, unit_counts.values)
            plt.xlabel('UNITS')
            plt.ylabel('Number of Victims')
            plt.xticks(unit_counts.index, rotation=45)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            

        if selected_unit:
            filtered_data = filtered_data[filtered_data['UnitName'] == selected_unit]
            feature_type = st.radio("Select Feature", [""] + ["Sex", "Caste", "Profession", "PersonType", "InjuryType", "PresentCity", "PresentState", "Nationality_Name", "age"])
            # Plot bar graph for selected feature type and filtered data
            if feature_type:
                plot_bar_graph_features(filtered_data, feature_type)
            if not feature_type:
                st.subheader(f'Number of Victims per year in {selected_district}-{selected_unit}')
                year_counts = filtered_data['Year'].value_counts()
                plt.figure(figsize=(10, 6))
                plt.bar(year_counts.index, year_counts.values)
                plt.xlabel('Year')
                plt.ylabel('Number of Victims')
                plt.title('Number of Victims each year')
                plt.xticks(year_counts.index, rotation=45)
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()


if __name__ == "__main__":
    main()