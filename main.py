import streamlit as st
import cohere
import pandas as pd
import pygsheets
import config
import os
import numpy as np
from dotenv import load_dotenv
from cohere.classify import Example
load_dotenv()

examples = [
            Example("you are hot trash", "Toxic"),
            Example("go to hell", "Toxic"), 
            Example("f*a*g*o*t", "Toxic"), 
            Example("stop being a pussy dude", "Toxic"), 
            Example("get rekt moron", "Toxic"), 
            Example("get a brain and use it", "Toxic"), 
            Example("say what you mean, you jerk.", "Toxic"),
            Example("Are you really this stupid", "Toxic"),
            Example("I will honestly kill you", "Toxic"),
            Example("yo how are you", "Benign"), 
            Example("I'm curious, how did that happen", "Benign"), 
            Example("Try that again", "Benign"), 
            Example("Hello everyone, excited to be here", "Benign"), 
            Example("I think I saw it first", "Benign"), 
            Example("That is an interesting point", "Benign"), 
            Example("I love this", "Benign"), 
            Example("We should try that sometime", "Benign"), 
            Example("You should go for it", "Benign")
            ]

# Classify a text for toxicity
def classify_text(text):
  classifications = co.classify(
    model='large',
    inputs=[text],
    examples=examples,
    )
  predicted_class = classifications.classifications[0].prediction
  benign_conf = classifications.classifications[0].confidence[1].confidence
  return predicted_class, benign_conf


# Paste your API key here. Remember to not share it publicly 

API_KEY = os.environ['API_KEY']
ENV=os.environ['ENV']

co = cohere.Client(API_KEY)

st.write("# co:detox")
with st.form("my_form"):
    text = st.text_area("Text to be classified")
    submitted = st.form_submit_button("Submit")

if submitted:
    response_class, response_conf = classify_text(text)
    st.write("Classification:  " + response_class)
