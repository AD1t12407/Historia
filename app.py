# app.py
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from apiCalls import callGPT3
import requests
from dotenv import load_dotenv
import os
from maps import get_autocomplete_results, get_map_url, get_place_details, get_street_view_url, image
from print import read_json, display_data




def main():
    input_text = st.text_input("Enter a location", "VNR VJIET")
    
    if input_text:
        autocomplete_results = get_autocomplete_results(input_text)
        
        if autocomplete_results['status'] == 'OK':   
            #image(autocomplete_results=autocomplete_results)
            st.write("Images render")
        else:
            st.error("Autocomplete failed. Please try again.")

    # Location textbox
    user_input = autocomplete_results["predictions"][0]["description"]
    st.write(user_input)
    if st.button('Submit'):
        res = callGPT3(loc=user_input)
        print(res)
        data = read_json("./response.json")
        display_data(data)
    
 
    
  
    

if __name__ == "__main__":
    main()
