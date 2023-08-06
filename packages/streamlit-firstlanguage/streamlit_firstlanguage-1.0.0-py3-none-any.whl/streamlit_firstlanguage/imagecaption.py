from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
from annotated_text import annotated_text
from annotated_text import annotation
import pandas as pd

def get_image_with_url(url, apiKey):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate NER provided")
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"url": ""} }'
    body = jsonpickle.decode(reqbody)

    
    body["input"]["url"] = decoded_url
    
    # Get Advanced API client which Image Caption is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_image_caption(body)
    # loop through text and create string array    
       
    return result.generated_caption

def imagecaption(name, apiKey, showURL=True, title=None, urlInputLabel=None,
                      resTitle=None, showImage=True, key=None):
    returnValue=""
    
    if showURL:
        with st.container():
            if title is not None:
                st.subheader(title)
            
            if urlInputLabel is None:
                urlInputLabel = "Enter URL here to fetch the image"

            url = st.text_input(urlInputLabel, value="",
                               max_chars=1000, help="Enter Image URL here", key="image_url_1")
            
            if st.button('Submit', key="image_url_1_submit"):
                if url != "":
                    result = get_image_with_url(
                        url, apiKey)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showImage is True:   
                        with st.expander("Output", expanded=True):                 
                            st.image(url, caption=result, use_column_width='auto')
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue