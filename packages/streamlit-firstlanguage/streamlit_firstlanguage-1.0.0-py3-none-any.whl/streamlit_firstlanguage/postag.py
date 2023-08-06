from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
from annotated_text import annotated_text
from annotated_text import annotation
import pandas as pd
from htbuilder.units import unit

# Only works in 3.7+: from htbuilder.units import px, rem, em
px = unit.px
rem = unit.rem
em = unit.em



colors = {
    "ADJ": "#a5129e",
    "ADP": "#fe0b44",
    "ADV": "#cc979a",
    "AUX": "#52a26d",
    "CONJ": "#05dddc",
    "CCONJ": "#4f5b9d",
    "DET": "#e59607",
    "INTJ": "#448939",
    "NOUN": "#927d09",
    "NUM": "#839663",
    "PART": "#c5a331",
    "PRON":"#d66fba",
    "PROPN": "#fee57f",
    "PUNCT": "#1abe47",
    "SCONJ": "#5e5d97",
    "SYM": "#ed5786",
    "VERB": "#f7ce22",
    "X": "#2da640",
    "EOL": "#5e5d97",
    "SPACE": "#a9cf46",
}

data = {
  "LANGUAGES" : ["English", "Tamil", "Chinese", "Dutch", "Lithuanian", "German", "Italian", "Polish", "Romanian"],
   "ISOCODE" :["en", "ta", "zh", "nl","lt", "de", "it", "pl", "ro"] 
}

lang = pd.DataFrame(data, index = ["English", "Tamil", "Chinese", "Dutch", "Lithuanian", "German", "Italian", "Polish", "Romanian"])


def get_postag_with_txt(text, apiKey, lang="en", lineBreak=4):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to calculate POSTag provided")

    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"lang":"","text": ""} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["text"] = text
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Basic API client which POSTag is part of
    basic_api_controller = client.basic_api
    # Call the POSTAG API
    result = basic_api_controller.get_postag(body)
    # loop through text and create string array    
    text_array = []
    count = 0
    for postag in result:    
        count +=1
        taggedWord = annotation(postag.original_text, postag.postag, colors[postag.postag], font_size=em(1.1), font_weight="bold")
        text_array.append(taggedWord)
        if count == lineBreak:
            text_array.append("  ")
            count = 0
        
    return text_array

def get_postag_with_url(url, apiKey,contentType, lang="en", lineBreak=4):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate POSTag provided")
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
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Basic API client which POSTag is part of
    basic_api_controller = client.basic_api
    # Call the POSTAG API
    result = basic_api_controller.get_postag(body)
    # loop through text and create string array
    text_array = []
    count = 0
    for postag in result:    
        count +=1
        taggedWord = annotation(postag.original_text, postag.postag, colors[postag.postag], font_size=em(1.1), font_weight="bold")
        text_array.append(taggedWord)
        if count == lineBreak:
            text_array.append("  ")
            count = 0
       
    return text_array

def postag(name, apiKey, posText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showAnnotated=True, helpText=None, height=None, 
                      showLang=True, overRideColor=None, selectLabel= None,lineBreak=4, key=None):
    returnValue=[]
    if posText:
        with st.container():
            if overRideColor is not None:
                colors = overRideColor


            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your content here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="postag_text_area")
            label="Select your language:"
            if selectLabel is not None:
                label = selectLabel
            if showLang:
                langSelected = st.selectbox(label, lang, key="postag_text_input")

            if st.button('Submit',key="postag_submit"):
                if txt != "":
                    result = get_postag_with_txt(
                        txt, apiKey, lang=lang.loc[langSelected]["ISOCODE"], lineBreak=lineBreak)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showAnnotated is True:
                        with st.expander("Output", expanded=True):                   
                            annotated_text(*result)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result
                    else:
                        returnValue = result
            
    else:
        with st.container():
            if overRideColor is not None:
                colors = overRideColor

            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter URL here to extract content"

            txt = st.text_input(txtAreaLabel, value="",
                               max_chars=1000, help=helpText)
            label="Select your language:"
            if selectLabel is not None:
                label = selectLabel
            if showLang:
                langSelected = st.selectbox(label, lang, key="url_input_postag")
            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="select_content_type_postag")
            if st.button('Submit',key="url_submit_postag"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_postag_with_url(
                        txt, apiKey, contentType,lang=lang.loc[langSelected]["ISOCODE"], lineBreak=lineBreak)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showAnnotated is True: 
                        with st.expander("Output", expanded=True):                   
                            annotated_text(*result)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue