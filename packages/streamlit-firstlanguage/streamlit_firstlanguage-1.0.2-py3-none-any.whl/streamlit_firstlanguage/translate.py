from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
import pandas as pd
from annotated_text import annotated_text
from annotated_text import annotation
import tempfile
import os.path
import time


def get_translate_with_txt(text, apiKey,lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No flattable for the questions")
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"text":"" ,"lang": ""} }'
    body = jsonpickle.decode(reqbody)
    
    
    body["input"]["text"] = text
    body["input"]["lang"] = lang

    
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the TableQA API
    result = advanced_api_controller.get_translate(body)
                  
    return result.generated_text

def get_translate_with_url(url, apiKey,lang,contentType,preserveFormat, pathToTmpFile):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate answers provided")
    if contentType == "Select Content Type":
        raise Exception("No content type selected")
   
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"preserveFormat":"false","url": "","contentType":"", "lang":""} }'
    body = jsonpickle.decode(reqbody)
   
    body["input"]["url"] = decoded_url
    body["input"]["lang"] = lang
    body["input"]["contentType"] = contentType
    body["input"]["preserveFormat"] = preserveFormat
    
    

    # Get Advanced API client which Translate is part of
    advanced_api_controller = client.advanced_api
    # Call the Translate API
    result = advanced_api_controller.get_translate(body)

    if preserveFormat == "true":        
        with open(pathToTmpFile, 'wb') as f:
            f.write(result.text)
        f.close()    
        return pathToTmpFile
    
    if contentType != "pdf" and contentType != "docx":
        result = result.generated_text

    return result



def translate(name, apiKey, translateText=True, title=None, inputLabel=None,
                      resTitle=None, showResult=True, helpText=None, height=None, 
                      showLang=True, langLabel=None,pathToTmpFile=None ,key=None):
    returnValue={}
    
    if translateText:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if inputLabel is None:
                inputLabel = "Enter text to translate"
            
            if helpText is None:
                helpText = "Enter text to translate"

            txt = st.text_area(inputLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="translate_1")
            
            label="Enter ISO Language code:"
            if langLabel is not None:
                label = langLabel
            if showLang:
                lang = st.text_input(label, value="ta"
                        , max_chars=2, key="translate_label_1")                                  

                      
            if st.button('Submit', key="translate_button_1"):
                if txt != "":
                    result = get_translate_with_txt(
                        txt, apiKey, lang) 
                    
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showResult is True:
                        with st.expander("Output", expanded=True):     
                            st.write(result)
                            st.markdown("  ", unsafe_allow_html=False)
    else:
        with st.container():            

            if title is not None:
                st.subheader(title)
            
            if inputLabel is None:
                inputLabel = "Enter URL of the file to translate"
            
            if helpText is None:
                helpText = "Enter URL of the file to translate"

            url = st.text_input(inputLabel, value="https://docs.google.com/document/d/1p8ER__mGPlu59zCrqH1PxNNao92qBsq-/export?format=docx",
                               max_chars=1000, help=helpText)

            label="Enter ISO Language code:"
            if langLabel is not None:
                label = langLabel
            lang = st.text_input(label, value="ta", max_chars=2, key="translate_label_2")

            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), 
                    key="translate_select_content_type", index=4)
            if contentType == "pdf" or contentType == "docx":                
                preserveFileFormat = st.radio(
                    "Select if you want to preseve the file format",
                    ('true', 'false'), index=0)            
            else:
                preserveFileFormat = "false"

            
                        
            ts = int(time.time())
            if contentType == "pdf":
                fileName = str(ts)+'output.pdf'
            elif contentType == "docx":
                fileName = str(ts)+'output.docx'                
                
            if pathToTmpFile is not None and preserveFileFormat == "true":
                pathToTmpFile = pathToTmpFile + fileName
                
            if st.button('Submit', key="translate_button_2"):
                if url != "":
                    if pathToTmpFile is None and preserveFileFormat == "true":
                        with tempfile.TemporaryDirectory() as td:
                            pathToTmpFile = os.path.join(td,fileName )
                            result = get_translate_with_url(
                                url, apiKey, lang,contentType, preserveFileFormat, pathToTmpFile)
                            
                            if resTitle is not None:
                                st.subheader(resTitle)

                            if showResult is True:
                                f = open(pathToTmpFile, "rb") 
                                if contentType == "pdf":                                                        
                                    st.download_button(
                                        label="Download translated file",
                                        data=f,
                                        file_name='output.pdf',
                                        mime='application/pdf',
                                    )
                                if contentType == "docx":                                                        
                                    st.download_button(
                                        label="Download translated file",
                                        data=f,
                                        file_name='output.docx',
                                        mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                    )
                                st.markdown("  ", unsafe_allow_html=False)
                            returnValue = result
                    else:
                        result = get_translate_with_url(
                        url, apiKey, lang,contentType, preserveFileFormat, pathToTmpFile)
                    
                        if resTitle is not None:
                            st.subheader(resTitle)
                        if showResult is True:
                                        
                                with st.expander("Output", expanded=True):                   
                                    st.write(result)
                                    st.markdown("  ", unsafe_allow_html=False)
                        
                        returnValue = result
    return returnValue