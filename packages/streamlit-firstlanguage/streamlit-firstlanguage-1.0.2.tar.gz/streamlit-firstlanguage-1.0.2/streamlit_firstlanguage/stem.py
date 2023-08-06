from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st




def get_stem_with_txt(text, apiKey, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to calculate stem provided")

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
    # Get Advanced API client which Stemmer is part of
    basic_api_controller = client.basic_api
    # Call the Stemmer API
    result = basic_api_controller.get_stemmer(body)
    stemDict = {"originalText": [], "stemmedText": []}

    # loop through text and create string array  
    for stem in result:   
        stemDict["originalText"].append(stem.original_text)
        stemDict["stemmedText"].append(stem.stem)
    
    return stemDict

def get_stem_with_url(url, apiKey,contentType, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate stem provided")
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
    # Get Advanced API client which Stemmer is part of
    basic_api_controller = client.basic_api
    # Call the Stemmer API
    result = basic_api_controller.get_stemmer(body)
    # loop through text and create string array
    stemDict = {"originalText": [], "stemmedText": []}

    # loop through text and create string array  
    for stem in result:   
        stemDict["originalText"].append(stem.original_text)
        stemDict["stemmedText"].append(stem.stem)
    
    return stemDict

def stem(name, apiKey, stemText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showTable=True, helpText=None, height=None, 
                      showLang=True, langLabel= None, key=None):
    returnValue={"originalText": [], "stemmedText": []}
    if stemText:
        with st.container():
            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your content here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="stem_text_area")
            label="Enter language ISO code:"
            if langLabel is not None:
                label = langLabel
            if showLang:
                langSelected = st.text_input(label, value="en",
                               max_chars=2, key="stem_lang1")

            if st.button("Submit", key="stem_submit"):
                if txt != "":
                    result = get_stem_with_txt(
                        txt, apiKey, lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showTable is True:
                        with st.expander("Output", expanded=True):                   
                            st.table(result)
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
            label="Enter language ISO code:"
            if langLabel is not None:
                label = langLabel
            if showLang:
                langSelected = st.text_input(label, value="en",
                               max_chars=2, key="stem_lang2")

            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="stem_select_content_type")

            if st.button('Submit', key="stem_submit_1"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_stem_with_url(
                        txt, apiKey, contentType,lang=langSelected)
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showTable is True:                    
                        with st.expander("Output", expanded=True):                   
                            st.table(result)
                            st.markdown("  ", unsafe_allow_html=True)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue