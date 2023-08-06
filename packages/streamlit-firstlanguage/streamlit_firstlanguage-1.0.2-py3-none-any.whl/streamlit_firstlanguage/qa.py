from firstlanguage_python.firstlanguage_client import Client
from firstlanguage_python.configuration import Environment
import jsonpickle
import streamlit as st
import pandas as pd
from annotated_text import annotated_text
from annotated_text import annotation


def get_qa_with_txt(text, apiKey,question, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if text is None:
        raise Exception("No text to calculate NER provided")
    #check if labels has value
    if question is None:
        raise Exception("No question provided")

    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)
    # prepare API input
    reqbody = '{"input":{"lang":"","context": "", "question":""} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["context"] = text
    body["input"]["question"] = question

    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_qa(body)
                
    return result

def get_qa_with_url(url, apiKey,contentType,question, lang="en"):
    # check if apikey has value
    if apiKey is None:
        raise Exception("No API Key provided")
    # check if text has value
    if url is None:
        raise Exception("No text to calculate NER provided")
    if contentType == "Select Content Type":
        raise Exception("No content type selected")
    #check if labels has value
    if question is None:
        raise Exception("No labels provided")
    
    # Initalize FirstLanguage Client
    client = Client(
        apikey=apiKey,
        environment=Environment.PRODUCTION)

    decoded_url = bytes(url, "utf-8").decode("unicode_escape") 
    
    
    # prepare API input
    reqbody = '{"input":{"lang":"","url": "","contentType":"", "question":""} }'
    body = jsonpickle.decode(reqbody)

    body["input"]["lang"] = lang
    body["input"]["url"] = decoded_url
    body["input"]["contentType"] = contentType
    body["input"]["question"] = question
    # body = jsonpickle.decode(json.dumps(reqbody))
    # Get Advanced API client which NER is part of
    advanced_api_controller = client.advanced_api
    # Call the NER API
    result = advanced_api_controller.get_qa(body)
    
    return result

def highlightPortion(context, start, end, totalLen,answer, frameSize=50 ) : #defaults to 50 frameSize
    newStart = start - frameSize
    
    markDownString=""

    if newStart < 0 :
        newStart = 0
    else :
        markDownString = markDownString + "......"
    if frameSize > totalLen :
        newEnd = totalLen
    else :
        newEnd = end + frameSize
        if newEnd > totalLen :
            newEnd = totalLen
    
    str = context[newStart:newEnd]
    markDownString = markDownString + str           
    if newEnd != totalLen :
        markDownString = markDownString + "......"

    split = markDownString.split(answer)
    returnValue = []
    for i, word in enumerate(split):
        if word == '':
            returnValue.append(annotation(answer, "answer", "#fff000"))
        else:
            returnValue.append(annotation(word, background="#ffffff"))
        if(i != len(split)-1) and word != '':
            returnValue.append(annotation(answer, "answer", "#fff000"))    

    return tuple(returnValue)

def qa(name, apiKey, qaText=True, title=None, txtAreaLabel=None,
                      resTitle=None, showAnnotated=True, helpText=None, height=None, 
                      showLang=True, langLabel=None, qLabel=None, key=None):
    returnValue={}
    
    if qaText:
        with st.container():            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter your context for the question here"

            txt = st.text_area(txtAreaLabel, height=height,value="",
                               max_chars=1000000, help=helpText, key="qa_text_area")
            
            label="Enter the question to find answer:"
            if qLabel is not None:
                label = qLabel
            question = st.text_input(label, value="", max_chars=1000, key="qa_label_1")

            labelISO="Enter language ISO code:"
            
            if langLabel is not None:
                labelISO = langLabel
            
            if showLang:
                langSelected = st.text_input(labelISO, value="en", max_chars=2, key="qa_lang1")

            
            returnValue= '{"score":"","start": "","end":"", "answer":""}'
            returnValue = jsonpickle.decode(returnValue)
            if st.button('Submit',key="qa_button"):
                if (txt != "" and question != ""):
                    result = get_qa_with_txt(
                        txt, apiKey, question=question, lang=langSelected)
                    if result is not None:
                        returnValue['score'] = result.score
                        returnValue['start'] = result.start
                        returnValue['end'] = result.end
                        returnValue['answer'] = result.answer

                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showAnnotated is True:
                        with st.expander("Output", expanded=True):     
                            tup = highlightPortion(txt,result.start, result.end, len(txt), result.answer)                                   
                            annotated_text(*tup)
                            st.markdown("  ", unsafe_allow_html=False)
    else:
        with st.container():
            
            if title is not None:
                st.subheader(title)
            
            if txtAreaLabel is None:
                txtAreaLabel = "Enter URL here to extract context"

            txt = st.text_input(txtAreaLabel, value="",
                               max_chars=1000, help=helpText)
            qLabel="Enter the question to find answer:"
            if qLabel is not None:
                label = qLabel
            question = st.text_input(label, value="", max_chars=1000, key="qa_label_2")

            label="Enter language ISO code:"
            if langLabel is not None:
                label = langLabel
            if showLang:
                langSelected = st.text_input(label, value="en",
                               max_chars=2, key="qa_lang2")

            contentType= st.selectbox("Select content type", ("Select Content Type", "html", "plaintext", "pdf", "docx"), key="select_content_type_qa")

            
            returnValue= '{"score":"","start": "","end":"", "answer":""}'
            returnValue = jsonpickle.decode(returnValue)
            if st.button('Submit',key="qa_button_2"):
                if (txt != "" and contentType != "Select Content Type"):
                    result = get_qa_with_url(
                        txt, apiKey, contentType,question=question, lang=langSelected)
                    if result is not None:
                        returnValue['score'] = result.score
                        returnValue['start'] = result.start
                        returnValue['end'] = result.end
                        returnValue['answer'] = result.answer

                    if resTitle is not None:
                        st.subheader(resTitle)
                    if showAnnotated is True:                    
                        with st.expander("Output", expanded=True):                   
                            st.markdown(result.answer, unsafe_allow_html=False)
                            st.markdown("  ", unsafe_allow_html=False)
                        returnValue = result
                    else:
                        returnValue = result
    return returnValue