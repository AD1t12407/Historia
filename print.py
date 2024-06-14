import streamlit as st
import json

# Function to read JSON data from the specified path
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        st.error(f"Error reading JSON file: {e}")
        return None

# Function to display the JSON data in Streamlit
def display_data(data):
    if data:
        st.header(data.get("Place", "Unknown Place"))
        
        st.subheader("History")
        st.write(data.get("history", "No history available."))
        
        st.subheader("Ecological Relevance")
        st.write(data.get("Ecological Relevance", "No ecological relevance available."))
        
        st.subheader("Timeline of Major Events")
        timeline = data.get("timeline", [])
        if timeline:
            for event in timeline:
                st.write(f"**{event.get('Year', 'Unknown Year')}**: {event.get('Details', 'No details available.')}")
        else:
            st.write("No major events available.")
    else:
        st.write("No data to display.")

# Streamlit application
def main():
    st.title('Historical Data Viewer')

    data = read_json("./data/petra.json")
    display_data(data)
   
if __name__ == "__main__":
    main()
