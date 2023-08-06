from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
from annotated_text import annotated_text
from annotated_text import annotation



def get_summary_with_txt(text, apiKey, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to generate summary")

    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"lang":"","text": ""} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["text"] = text
    
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_summary(body)
    
    return result.summary

def get_summary_with_url(url, apiKey,contentType, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate NER provided")
    if contentType == "Select Content Type":
        raise Exception("No content type selected")
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"lang":"","url": "", "contentType":""} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["url"] = decoded_url
    body["input"]["contentType"] = contentType
    
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_summary(body)
          
    return result.summary

def summary(name, apiKey, summaryText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showSummaryResult=True, helpText=None, height=None, 
                      showLang=True, langLabel=None, key=None):
    returnValue=""
    
    if summaryText:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your text here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="sum_text_area")
            
            labelISO="Enter language ISO code:"
            
            if langLabel is not None:
                labelISO = langLabel

            if showLang:
                langSelected = st.text_input(labelISO, value="en", max_chars=2, key="sum_lang1")

            if st.button('Submit', key="sum_submit"):
                if txt != "":
                    result = get_summary_with_txt(
                        txt, apiKey, lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showSummaryResult is True:
                        with st.expander("Output", expanded=True):                   
                            st.write(result)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result                    
                    else:
                        returnValue = result
    else:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter URL here to extract content"

            txt = st.text_input(txtAreaLabel, value="",
                               max_chars=1000, help=helpText)
            labelISO="Enter language ISO code:"
            
            if langLabel is not None:
                labelISO = langLabel

            if showLang:
                langSelected = st.text_input(labelISO, value="en", max_chars=2, key="sum_lang2")

            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="select_content_type_sum")

            if st.button('Submit', key="sum_submit_1"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_summary_with_url(
                        txt, apiKey, contentType,lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showSummaryResult is True:                    
                        with st.expander("Output", expanded=True):                   
                            st.write(result)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue