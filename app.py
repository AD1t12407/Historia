# app.py
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Process the frame here (optional)
        return frame

def main():
    st.title("Webcam Image Capture")
    
    st.header("Capture Image from Webcam")
    
    webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
    
    if webrtc_ctx.video_transformer:
        if st.button("Capture Image"):
            # Convert the frame to a PIL image (or process it as needed)
            image = webrtc_ctx.video_transformer.last_frame.copy()
            
            # Display the captured image
            st.image(image, caption='Captured Image', use_column_width=True)
        st.title("Google Maps Street View Embedding")
    
    st.header("Embedding Google Maps Street View")
    
    # Latitude and Longitude for a specific location (e.g., New York City)
    location_lat = 40.730610
    location_lon = -73.935242
    
    # Google Maps Street View URL with parameters
    street_view_url = f"https://www.google.com/maps/embed/v1/streetview?location={location_lat},{location_lon}&key=YOUR_API_KEY"
    
    # Embedding the Street View iframe using HTML component
    st.components.v1.html(f'<iframe width="600" height="450" frameborder="0" style="border:0" src="{street_view_url}" allowfullscreen></iframe>', height=450)
    

if __name__ == "__main__":
    main()
