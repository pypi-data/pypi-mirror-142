<a href="https://www.firstlanguage.in"><img src="https://img.firstlanguage.in/img/Original_9M3zC4lrHRd.webp?tr=w-150" width="100" height="100" align="right" />
</a>

# streamlit-firstlanguage: Streamlit Components to access FirstLanguage NLP API


This package provides interactive Streamlit components to access FirstLanguage NLP API. For full FirstLanguage API documentation, please visit our site [FirstLanguage API](https://firstlanguage.in)

For direct SDK options, please visit:

[Python SDK](https://github.com/FirstLanguage/firstlanguage_python)

[TypeScript SDK](https://github.com/FirstLanguage/firstlanguage-typescript)

## 🚀 Quickstart

You can install streamlit-firstlanguage from PyPi using pip:
```bash
pip install streamlit-firstlanguage
```

You will need API Key to access our API. Please register with us to get your life-time FREE API Key. Credit Card not required!!!

[Regsitration Page Link](https://www.firstlanguage.in/auth/create-account)


You can then access our API with one line of code.

For example, you can implement a Named Entity Recognition App with below code

```python
#ner.py
import streamlit_firstlanguage as fl

fl.firstlanguage_ner(name="fl_ner",apiKey="<Your_API_Key>")
```

You can then run your app with 
```bash
streamlit run ner.py
```
The app should pop up in your web browser.

Below is a list of NLP Tasks that you can access with our API,



| NLP Task    | Streamlit Component   |
|--------------|------------|
|  Stemmer      |  firstlanguage_stem()        |
|  Lemmatizer     |  firstlanguage_lemma()        |
|  Morphological Analyzer      |  firstlanguage_morph()        |
|  POSTagger      |  firstlanguage_postag()        |
|  Text Classification       |  firstlanguage_classify()        |
|  Question Answering     |  firstlanguage_qa()        |
|  Table Question Answering     |  firstlanguage_tableqa()        |
|  Image Captioning     |  firstlanguage_imagecaption()        |
|  Named Entity Recognition     |  firstlanguage_ner()        |
|  Summarization     |  firstlanguage_summary()        |
|  Translation     |  firstlanguage_translate()        |


Name and APIKey is the only required params to access the component. Most of the component elements are configurable.



# API Details


### firstlanguage_postag

```python
def firstlanguage_postag(name, apiKey, posText=True, title=None, txtAreaLabel=None
```


This component is used to generate part of speech tags for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 posText |  bool | If True, the component will render a text area for the user to enter text to determine the POSTag. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to determine POSTag.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showAnnotated |  bool | If True, the component will display the annotated text in the result. If False, the component will just return the list of strings and tuples for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language dropdown in the frontend. If false, the dropdown will not be visible and the default value of 'en' will be passed to the API.
 overRideColor |  Dict | Pass the Dict object given below with different colors to over-ride the default color values for the POSTags annotation. The default dict object is as follows: {"ADJ":"#a5129e","ADP":"#fe0b44","ADV":"#cc979a","AUX":"#52a26d","CONJ":"#05dddc","CCONJ":"#4f5b9d","DET":"#e59607","INTJ":"#448939","NOUN":"#927d09","NUM":"#839663","PART":"#c5a331","PRON":"#d66fba","PROPN":"#fee57f","PUNCT":"#1abe47","SCONJ":"#5e5d97","SYM":"#ed5786","VERB":"#f7ce22","X":"#2da640","EOL":"#5e5d97","SPACE":"#a9cf46"}
 selectLabel |  str | The label for the language dropdown to display in the frontend.
 lineBreak |  int | The number of words after which to introduce a line break. This helps in fitting the output inside the container. Default value is 4.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | list | The component will return a list of tuples and strings with annotation details and postags.





### firstlanguage_ner

```python
def firstlanguage_ner(name, apiKey, nerText=True, title=None, txtAreaLabel=None
```




This component is used to generate Named Entity Recognition (NER) for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 nerText |  bool | If True, the component will render a text area for the user to enter content to determine the NER. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to determine NER.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showAnnotated |  bool | If True, the component will display the annotated text in the result. If False, the component will just return the list of strings and tuples for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language dropdown in the frontend.If false, the dropdown will not be visible and the default value of 'en' will be passed to the API.
 overRideColor |  Dict | Pass the Dict object given below with different colors to over-ride the default color values for the NER annotation. The default dict object is as follows: {"DATE":"#a5129e","Cuisine":"#fe0b44","Dish":"#cc979a","Hours":"#52a26d","Price":"#05dddc","Rating":"#4f5b9d","Restaurant":"#e59607","Amenity":"#448939","PER":"#927d09","ORG":"#839663","LOC":"#c5a331"}
 selectLabel |  str | The label for the language dropdown to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | list | The component will return a list of tuples and strings with annotation details and NER entities.





### firstlanguage_stem

```python
def firstlanguage_stem(name, apiKey, stemText=True, title=None, txtAreaLabel=None
```




This component is used to generate Stemming for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 stemText |  bool | If True, the component will render a text area for the user to enter content to stem. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to stem the words.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showTable |  bool | If True, the component will display the stemmed text in the result. If False, the component will just return the dict with stemmed words for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend. If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict in the format {"originalText": [], "stemmedText": []} with originalText list and stemmedText list filled in.





### firstlanguage_lemma

```python
def firstlanguage_lemma(name, apiKey, lemmaText=True, title=None, txtAreaLabel=None
```




This component is used to generate Lemmatization for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 lemmaText |  bool | If True, the component will render a text area for the user to enter content to lemmatize. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to lemmatize the words.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showTable |  bool | If True, the component will display the lemmatize text in the result. If False, the component will just return the dict with lemmatized words for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict in the format {"originalText": [], "lemmatizedText": []} with originalText list and lemmatizedText list filled in.





### firstlanguage_classify

```python
def firstlanguage_classify(name, apiKey, classifyText=True, title=None, txtAreaLabel=None
```




This component is used to classify a given text or text from an url against a given set of labels.


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 classifyText |  bool | If True, the component will render a text area for the user to enter content to classify. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to classify.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showGraph |  bool | If True, the component will display the classification output as a graph. If False, the component will just return the dict with classification results for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.
 showLabels |  bool | Show the lebels to be classified in the frontend.
 labelTitle |  str | The title of the labels section to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict in the format {"Labels": [], "Scores": []}  with Labels list and Scores list filled in.





### firstlanguage_morph

```python
def firstlanguage_morph(name, apiKey, morphText=True, title=None, txtAreaLabel=None
```




This component is used to generate Morphological Analysis for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 morphText |  bool | If True, the component will render a text area for the user to enter content to find morphological features. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to find morphological features.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showTable |  bool | If True, the component will display the morphological featuresin the result.If False, the component will just return the dict with morphological features for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict in the format {"originalText": [], "morphFeatures": []} with originalText list and morphFeatures list filled in.





### firstlanguage_qa

```python
def firstlanguage_qa(name, apiKey, qaText=True, title=None, txtAreaLabel=None
```




This component is used to generate QA for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 qaText |  bool | If True, the component will render a text area for the user to enter context to find answers for the questions passed. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to pass as the context.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showAnnotated |  bool | If True, the component will display the highlighted answer in the result. If False, the component will just return the dict with answer for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.
 qLabel |  str | The label for the question text field to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict in the original API response format.





### firstlanguage_imagecaption

```python
def firstlanguage_imagecaption(name, apiKey, showURL=True, title=None, urlInputLabel=None
```




This component is used to generate image caption for a given image url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 showURL |  bool | If True, the component will render a text input for the user to enter the image url to caption. If False, the component will not render the input
 title |  str | The title of the component to display in the frontend.
 urlInputLabel |  str | The label for the url input to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showImage |  bool | If True, the component will display the image with the generated caption.If False, the component will just return a string with the generated caption.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | string | The component will return the generated caption as a string.





### firstlanguage_summary

```python
def firstlanguage_summary(name, apiKey, summaryText=True, title=None, txtAreaLabel=None
```




This component is used to generate summary for a given text or text from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 summaryText |  bool | If True, the component will render a text area for the user to enter context to summarize. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to summarize.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showSummaryResult |  bool | If True, the component will display the summary result.If False, the component will just return a string with the summary for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | sring | The component will return the summary as a string.





### firstlanguage_tableqa

```python
def firstlanguage_tableqa(name, apiKey, flatTableInput=True, title=None, inputLabel=None
```




This component is used to generate answers from a given table data from text area or CSV file from an url


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 flatTableInput |  bool | If True, the component will render a text area for the user to enter a flattable in JSON format. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract table from a CSV file
 title |  str | The title of the component to display in the frontend.
 inputLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showResult |  bool | If True, the component will display the qa result.If False, the component will just return a string with the answers for questions for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showQuestions |  bool | If True, the component will display the questions text box in the frontend.If false, the text box will not be visible.
 qLabel |  str | The label for the language text box to display in the frontend.
 sendBackRows |  bool | If True, the component will send back the rows of the table corresponding to the answer. If False, the component will not send back the rows of the table corresponding to the answer

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | dict | The component will return a dict with questions,answers,rows and aggregrate used in the format {"Questions": [], "Anwsers": [], "Rows": [], "Aggregrate": "[]"}





### firstlanguage_translate

```python
def firstlanguage_translate(name, apiKey, translateText=True, title=None, txtAreaLabel=None
```




This component is used to generate translation for a given text or text from an url or translate a PDF or DOCX


#### Parameters

 Parameter  | Type  | Doc
-----|----------|-----
 name |  str | A short name for the component to identify it.
 key |  str or None | An optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state.
 apiKey |  str | The API key for the FirstLanguage API. This is required to use the component. You can get a FREE API key from https://www.firstlanguage.in
 translateText |  bool | If True, the component will render a text area for the user to enter text to translate. If False, the component will render an input field and contenType dropdown for the user to enter URL from which the API will extract the text to translate.
 title |  str | The title of the component to display in the frontend.
 txtAreaLabel |  str | The label for the text area to display in the frontend.
 resTitle |  str | The title of the result section to display in the frontend.
 showResult |  bool | If True, the component will display the translation result. Applicable only for Text Translation.If False, the component will just return a string with the summary for the developer to process it further.
 helpText |  str | Help text for the Text Area to display in the frontend.
 height |  int | The height of the text area to display in the frontend.
 showLang |  bool | If True, the component will display the language text box in the frontend.If false, the text box will not be visible and the default value of 'en' will be passed to the API.
 langLabel |  str | The label for the language text box to display in the frontend.
 pathToTmpFile |  str | Temproray output dir for translation by URL with contentType as PDF or DOCX.Dir path should end with /. No need to pass the file name.File name will be automatically generated with the format <timestamp>output.pdf or <timestamp>output.docx.If value is not provided, the component will create a temp file in the system temp dir

#### Returns

 Return Variable  | Type  | Doc
-----|----------|-----
 Unknown | sring | The component will return the translated text as a string. This applies for text transaltion and URL translation with preserveFormat flag set to False.For preserveFormat flag set to True, the component will return the translated file as pdf or docx format.


