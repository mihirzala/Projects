from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, pipeline
import shap

#PRETRAINED MODEL
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

#TOKENIZER 
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)

#EXPLAINER
explainer = shap.Explainer(classifier, tokenizer) 


#PUT THE SENTENCE YOU WANT ANALYZED INTO TEST_SENTENCES 
test_sentences =["How can you do something like this?", "I can't even look at you right now after what you did.",
"Why would you do this?","WHY WOULD YOU DO THIS?", "Wowww... good job buddy.", "You did a great job!", 
"The flight was sooooo bumpy. What a terrible experience!", "Why do I need all this paperwork when my luggage was damaged?",
"My JetBlue flight was cancelled. WHYYY????", "American Airlines had an amazing landing!", 
"The seats were so nice!", "This restaurant is so trashy", "All of you guys are fugasi", 
"He cooks a mean burger", "The Great Gatsby is a bad book."]

shap_values = explainer(test_sentences)

predictions = classifier.__call__(test_sentences)

#GRAPHING
for i in range(len(test_sentences)):
    print('SENTENCE: ' + str(i))
    print(predictions[i]['label'])
    shap.plots.text(shap_values[i])