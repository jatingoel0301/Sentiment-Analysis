# Sentiment-Analysis

## What is Sentiment Analysis?

It is a way to evaluate written or spoken language to determine if the expression is favorable, unfavorable, or neutral, and to what degree.
*	Movie:  is this review positive or negative?
*	Products: what do people think about the new iPhone?
*	Politics: what do people think about this candidate or issue?

Thus, sentiment analysis can be extended to any field to judge how people are perceiving things and its results can be used to make a better product.

## What this project aims to do?

This project aims to implements sentiment analysis on a user defined corpus by using a predefined set of weights given to specific words. The final score is predicted by summing all the individual weights of the words found in the document. A score in the negative implies that the document was a generally negative review while a score in the positive implies that the review was generally favourable.

## Steps involved

A collection of raw documents is usually transformed into an easily accessible representation. This process is called indexing. Most indexing techniques involves identifying good descriptors for the documents , such as keywords or terms, which describes the information content of  document and differentiates one document from other.

An automatic method of obtaining indexed representation of documents consists of following steps:
1.	Tokenization
2.	Stop words elimination
3.	Stemming
4.	Term weighting  

Pre-processing: The pre-processing involves 2 tasks:
1.	Loading our dataset into a python dictionary so that it can be accessed for weight references.
2.	Loading our corpus on which we want to perform the sentiment analysis.

Tokenization:
1.	This steps extracts individual terms from the document, converts them to lower case and removes punctuation marks.
2.	The output of this step is representation of documents as a stream of terms.

First we tokenize the sentence i.e. extract sentences out of a paragraph, and then we tokenize the words i.e. extract words out of a given sentence.

Stop Words Elimination:

1.	Stop words are high frequency words which have little semantic weight and are thus not useful in retrieval.
2.	These words play useful grammatical role such as formation of phrases but do not contribute in keyword-based representation.
3.	Eliminating stop words considerably reduces the index terms size.

Here, we do not need to eliminate stop words as they are absent from our dataset and would not be given any weightage, thus they will not affect the final output. Thus, here, there is no need to eliminate them explicitly, but we need to do so in case we are using a classifier. 

Stemming:

1.	After stop words removal, the morphological variant word forms are stemmed to their root word.
2.	Stemming helps in solving the problem of vocabulary mismatch and reduction in size of index terms.

Here, there is no need of stemming as well because our dataset already contains weights for different morphological variants of the word, so we don’t necessarily need to find the root stem.

Term Weighting:

In this step, weights are assigned to stemmed terms according to their importance in the document, in the collection, or combination of both.

## Final Output:

The weights of each word in the document are then summed up to predict the final score of the document and to classify whether the document has a ‘positive sentiment’ or a ‘negative sentiment’.

## Technology Used:

`Python 3.6.5` has been used to develop this project along with the `Natural Language Toolkit (NLTK) version 3.3`.

## Working Video

The video below details the working of this project:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/gBKYxLe6DQE/0.jpg)](https://www.youtube.com/watch?v=gBKYxLe6DQE)
