from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
import pandas as pd
from annotated_text import annotated_text
from annotated_text import annotation


def get_tableqa_with_txt(text, apiKey,question, lang="en", sendBackRows=False):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No flattable for the questions")
    #check if labels has value
    if question is None:
        raise Exception("No questions provided")

    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"flattable":false ,"questions": [], "sendBackRows":false} }'
    body = jsonpickle.decode(reqbody)
    
    quest = []
    for i in question.split(","):        
        quest.append(i)
    

    decoded_table = jsonpickle.decode(text)

    body["input"]["flattable"] = decoded_table
    body["input"]["questions"] = quest
    if sendBackRows:
        body["input"]["sendBackRows"] = True

    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the TableQA API
    result = advanced_api_controller.get_table_qa(body)
    

    ansDict = {"Questions": [], "Aggregrate": [],"Anwsers": [], "Rows": None}

    ansDict["Questions"] = quest
    if body["input"]["sendBackRows"] == True:
        ansDict["Rows"] = []
        for item in result:
            if item.rows is not None:
                ansDict["Rows"].append(item.rows)
                
    for item in result:
        if item.answer is not None:
            for ans in item.answer:
                split = ans.split("=")
                ansDict["Aggregrate"].append(split[0])
                ansDict["Anwsers"].append(split[1])
                
    return ansDict

def get_tableqa_with_url(url, apiKey,question,sendBackRows):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate answers provided")
    
    #check if labels has value
    if question is None:
        raise Exception("No questions provided")
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"sendBackRows":false,"url": "","questions":[]} }'
    body = jsonpickle.decode(reqbody)
    quest = []

    for i in question.split(","):
        quest.append(i)

    if sendBackRows:
        body["input"]["sendBackRows"] = True
    body["input"]["url"] = decoded_url
    
    body["input"]["questions"] = quest
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_table_qa(body)

    ansDict = {"Questions": [], "Aggregrate": [],"Anwsers": [], "Rows": None}

    ansDict["Questions"] = quest
    if body["input"]["sendBackRows"] == True:
        ansDict["Rows"] = []
        for item in result:
            if item.rows is not None:
                ansDict["Rows"].append(item.rows)
                
    for item in result:
        if item.answer is not None:
            for ans in item.answer:
                split = ans.split("=")
                ansDict["Aggregrate"].append(split[0])
                ansDict["Anwsers"].append(split[1])
                
    return ansDict



def tableqa(name, apiKey, flatTableInput=True, title=None, inputLabel=None,
                      resTitle=None, showResult=True, helpText=None, height=None, 
                      showQuestions=True, qLabel=None, key=None):
    returnValue={}
    
    if flatTableInput:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if inputLabel is None:
                inputLabel = "Enter a flattable in JSON format"
            
            if helpText is None:
                helpText = "Enter a flattable in JSON format"

            txt = st.text_area(inputLabel, height=height,value='{"Cities":["Paris, France","London, England","Lyon, France"],"Inhabitants":["2.161","8.982","0.513"]}',
                               max_chars=1000000, help=helpText, key="flattable_1")
            
            qLabel="Enter comma seperated questions to find answers:"
            if qLabel is not None:
                label = qLabel
            if showQuestions:
                question = st.text_input(label, value="How many inhabitants in France,How Many inhabitants in England"
                        , max_chars=1000, key="tableqa_label_1")
                      
            sendBackRows = st.radio(
                "Select if you want the rows corresponding to the answer to be returned",
                ('True', 'False'))
            if sendBackRows == "True":
                sendBackRows = True
            else:
                sendBackRows = False

            
            
            if st.button('Submit', key="tableqa_submit_1"):
                if (txt != "" and question != ""):
                    result = get_tableqa_with_txt(
                        txt, apiKey, question=question, sendBackRows=sendBackRows) 
                    
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showResult is True:
                        with st.expander("Output", expanded=True):     
                            st.table(result)
                            st.markdown("  ", unsafe_allow_html=False)
    else:
        with st.container():
            
            if title is not None:
                st.subheader(title)
            
            if inputLabel is None:
                inputLabel = "Enter URL to the CSV file"
            
            if helpText is None:
                helpText = "Enter a URL to the CSV file"

            url = st.text_input(inputLabel, value="https://drive.google.com/uc?id=1IpBFNs4FlRRbDzL_XPtmGHou_Rvc5Mvq",
                               max_chars=1000, help=helpText)

            qLabel="Enter comma seperated questions to find answers:"
            if qLabel is not None:
                label = qLabel
            question = st.text_input(label, value="How many inhabitants in France,How Many inhabitants in England", max_chars=1000, key="tableqa_label_2")

            sendBackRows = st.radio(
                "Select if you want the rows corresponding to the answer to be returned",
                ('True', 'False'))

            if sendBackRows == "True":
                sendBackRows = True
            else:
                sendBackRows = False

            if st.button('Submit', key="tableqa_submit_2"):
                if url != "":
                    result = get_tableqa_with_url(
                        url, apiKey, question=question, sendBackRows=sendBackRows)
                    
                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showResult is True:                    
                        with st.expander("Output", expanded=True):                   
                            st.table(result)
                            st.markdown("  ", unsafe_allow_html=False)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue