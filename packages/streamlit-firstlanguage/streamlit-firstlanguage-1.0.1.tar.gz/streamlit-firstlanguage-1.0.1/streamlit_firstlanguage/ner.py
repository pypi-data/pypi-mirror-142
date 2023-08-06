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
    "DATE": "#a5129e",
    "Cuisine": "#fe0b44",
    "Dish": "#cc979a",
    "Hours": "#52a26d",
    "Price": "#05dddc",
    "Rating": "#4f5b9d",
    "Restaurant": "#e59607",
    "Amenity": "#448939",
    "PER": "#927d09",
    "ORG": "#839663",
    "LOC": "#c5a331"
}

data = {
  "LANGUAGES" : ["English", "Arabic", "Chinese", "Dutch", "French", "German", "Italian", "Latvian", "Portuguese", "Spanish"],
   "ISOCODE" :["en", "ar", "zh", "nl","fr", "de", "it", "lv", "pt","es"] 
}

lang = pd.DataFrame(data, index = ["English", "Arabic", "Chinese", "Dutch", "French", "German", "Italian", "Latvian", "Portuguese", "Spanish"])


def get_ner_with_txt(text, apiKey, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to calculate NER provided")

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
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_ner(body)
    # loop through text and create string array    
    splits = text.split()
    for index, split in enumerate(splits):
        splits[index] = annotation(split , font_size=em(1.1),padding_right=".01rem", padding_left=".01rem",background="#ffffff")
        for ner in result:
            if split == ner.word:
                taggedWord = annotation(split, ner.entity_group, colors[ner.entity_group], font_size=em(1.1), font_weight="bold")
                splits[index] = taggedWord
    return splits

def get_ner_with_url(url, apiKey,contentType, lang="en"):
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
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_ner(body)
    # loop through text and create string array
    text_array = []
    
    for ner in result:    
        taggedWord = annotation(ner.word, ner.entity_group, colors[ner.entity_group], font_size=em(1.1), font_weight="bold")
        text_array.append(taggedWord)
       
    return text_array

def ner(name, apiKey, nerText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showAnnotated=True, helpText=None, height=None, 
                      showLang=True, overRideColor=None, selectLabel= None, key=None):
    returnValue=[]
    
    if nerText:
        with st.container():
            if overRideColor is not None:
                global colors; colors = overRideColor


            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your content here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="ner_area_1")
            label="Select your language:"
            if selectLabel is not None:
                label = selectLabel
            if showLang:
                langSelected = st.selectbox(label, lang, key="ner_text_input")

            if st.button('Submit',key="ner_button_1"):
                if txt != "":
                    result = get_ner_with_txt(
                        txt, apiKey, lang=lang.loc[langSelected]["ISOCODE"])
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
                global colors; colors = overRideColor

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
                langSelected = st.selectbox(label, lang, key="url_input_ner")
            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="select_content_type_ner")

            if st.button('Submit',key="url_button_ner"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_ner_with_url(
                        txt, apiKey, contentType,lang=lang.loc[langSelected]["ISOCODE"])
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