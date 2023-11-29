import streamlit as st
from PIL import Image
from CollectDataForTarget.CollectData import *

def main():
    
    # Create a title for your app
    st.title("Food Nutrition Analyzer")

    st.write("Welcome to our streamlit dashboard that takes food nutrition analysis and recommendation to the next level")
    
    st.title('Upload Photo')

    uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Photo', use_column_width=True)
        
    if st.button('Read Text'):
            try:
                text_result = read_text(image)
                
                st.subheader('Extracted Text:')
                for text in text_result:
                    st.write(text)  # Display the recognized text

            except Exception as e:
                st.error(f"Error: {e}")
                
    st.subheader('Extracted Info:')
    extracted_info = extract_info_from_text(text_result, 'meals')
    st.write(extracted_info)
    
    st.subheader('Organized Data for Analysis:')
    converted_df = convert_info_to_df(extracted_info)
    st.write(converted_df)
    

if __name__ == '__main__':
    main()
