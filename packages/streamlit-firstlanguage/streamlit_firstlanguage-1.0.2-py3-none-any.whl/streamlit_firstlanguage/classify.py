from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
import pandas as pd


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


def get_classify_with_txt(text, apiKey,labels, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to calculate NER provided")
    #check if labels has value
    if labels is None:
        raise Exception("No labels provided")

    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"lang":"","text": "", "labels":[]} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["text"] = text
    labels = labels.split(',')
    for label in labels:
        body["input"]["labels"].append(label)

    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_classification(body)
    # loop through text and create string array    
    classifyDict = {"Labels": [], "Scores": []}

    # loop through text and create string array  
    for label in result.labels:   
        classifyDict["Labels"].append(label)
    for score in result.scores:
        classifyDict["Scores"].append(str(score))        
    
    return classifyDict

def get_classify_with_url(url, apiKey,contentType,labels, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate NER provided")
    if contentType == "Select Content Type":
        raise Exception("No content type selected")
    #check if labels has value
    if labels is None:
        raise Exception("No labels provided")
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"lang":"","url": "","contentType":"", "labels":[]} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["url"] = decoded_url
    body["input"]["contentType"] = contentType
    labels = labels.split(',')
    for label in labels:
        body["input"]["labels"].append(label)
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_classification(body)
    # loop through text and create string array          
    classifyDict = {"Labels": [], "Scores": []}

    # loop through text and create string array  
    for label in result.labels:   
        classifyDict["Labels"].append(label)
    for score in result.scores:
        classifyDict["Scores"].append(score)        
    
    return classifyDict

def classify(name, apiKey, classifyText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showGraph=True, helpText=None, height=None, 
                      showLang=True, langLabel=None, showLabels=True,labelTitle=None, key=None):
    returnValue={}


    
    if classifyText:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your content here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="clsy_text_area_1")
            
            labelTitle="Enter comma seperated labels to classify against:"
            if labelTitle is not None:
                label = labelTitle
            if showLabels:
                labels = st.text_input(label, value="positive,negative", max_chars=1000, key="classify_label_1")

            labelISO="Enter language ISO code:"
            
            if langLabel is not None:
                labelISO = langLabel
            
            if showLang:
                langSelected = st.text_input(labelISO, value="en", max_chars=2, key="classify_lang1")

            if st.button('Submit', key="classify_submit_1"):
                if txt != "":
                    result = get_classify_with_txt(
                        txt, apiKey,labels=labels, lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showGraph is True:
                        with st.expander("Output", expanded=True):                                        
                            st.vega_lite_chart(result, {
                                'mark': {'type': 'bar', 'tooltip': True,
                                            'color': '#839663'},
                                    'encoding': {'x': {'field': 'Labels', 'type': 'nominal'},
                                                'y': {'field': 'Scores', 'type': 'quantitative'},
                                                'color': {'field': 'Labels', 'type': 'nominal'}
                                                }
                                
                            },use_container_width=True)                                               
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
            labelTitle="Enter comma seperated labels to classify against:"
            if labelTitle is not None:
                label = labelTitle
            if showLabels:
                labels = st.text_input(label, value="positive,negative", max_chars=1000, key="classify_label_2")

            label="Enter language ISO code:"
            if langLabel is not None:
                label = langLabel
            if showLang:
                langSelected = st.text_input(label, value="en",
                               max_chars=2, key="classify_lang2")

            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="select_content_type_ner")

            if st.button('Submit',key="classify_submit_2"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_classify_with_url(
                        txt, apiKey, contentType,labels=labels, lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showGraph is True:                    
                        with st.expander("Output", expanded=True):                   
                            st.vega_lite_chart(result, {
                                'mark': {'type': 'bar', 'tooltip': True,
                                            'color': '#839663'},
                                    'encoding': {'x': {'field': 'Labels', 'type': 'nominal'},
                                                'y': {'field': 'Scores', 'type': 'quantitative'},
                                                'color': {'field': 'Labels', 'type': 'nominal'}
                                                }
                                
                            },use_container_width=True)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue