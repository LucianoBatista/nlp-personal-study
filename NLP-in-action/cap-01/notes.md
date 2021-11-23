# TOC

<!-- vscode-markdown-toc -->
* 1. [What is Natural Lenguage Processing?](#WhatisNaturalLenguageProcessing)
* 2. [What is a Natural Language Processing System?](#WhatisaNaturalLanguageProcessingSystem)
* 3. [What about the speech recognition systems?](#Whataboutthespeechrecognitionsystems)
* 4. [Afirmatives](#Afirmatives)
	* 4.1. [**Applications:**](#Applications:)
	* 4.2. [Language through a computer's 'eyes'](#Languagethroughacomputerseyes)
	* 4.3. [A brief overflight of hyperspace](#Abriefoverflightofhyperspace)
	* 4.4. [Testse](#Testse)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='WhatisNaturalLenguageProcessing'></a>What is Natural Lenguage Processing?

Area of reasearch in computer science and AI concerned with processing natural languages such as Portuguese or Mandarim. This processing generally involves translating natural language into data (numbers).


##  2. <a name='WhatisaNaturalLanguageProcessingSystem'></a>What is a Natural Language Processing System?

Is often referred to as a **pipeline because it usually involves several stages** of processing where natural language flows in one end and the processed output flows out the other.


##  3. <a name='Whataboutthespeechrecognitionsystems'></a>What about the speech recognition systems?

Requires a lot of high quality labeled data, voice recordings annotated with their phonetic spellings, and natural language transcriptions aligned with the audio files. **The data collecting to build this kind of system is a very important step.**


##  4. <a name='Afirmatives'></a>Afirmatives

- Natural Languages can't be directly translated into a precise set of mathematical operations, but they do contain information and instructions that can be extracted.
- Machines are better to recognize sarcasm in a isolated twitter message than humans.
- Humans are better within an ongoing dialog, **ability to maintain information about the context of statement.**
- Semantic analysis, along with stats, can help resolve the ambiguity of natural language.
- There is no **'theory of mind'** you can point to in an NLP pipeline. Theory of mind is like a human that have sufficient knowlodge about something and is possible to answer based on very little information.


###  4.1. <a name='Applications:'></a>**Applications:**

- An estimated 20% of the tweets about the 2016 US presidential election were composed by chatbots.
- Many reviews are the creation of autonomous NLP pipelines that have never set foot in a movie theater.


###  4.2. <a name='Languagethroughacomputerseyes'></a>Language through a computer's 'eyes'

- An FSM -> regular expression
- Regular Expressions are simples comparing to NLP state-of-art solutions, but those can be useful to recognize a key phrase or command to unlock a particular action or behavior.
- A machine that processes this kind of language (regular expressions) can be thought of as a formal mathematical object called a **finite state machine** or **deterministic finite automation**.

Natural languages:

- Are not regular
- Are not context-free
- Can't be defined by any formal grammar

>to see a simple chatbot goes to `simple-chatbot.py`

Earlier approach to NLP was called of pattern-based, because of the limitations of computational resources. Example: **Porter stemmer** or **Treebank tokenizer**. 

When we use character sequence matches t o measure distance between natural language phrases, we'll often get it wrong. Some words may be similar, like bar and bad, on counting distance, but in real are very different.

Distance metrics designed for numerical sequences and vectors are useful for a few NLP applications, like _spelling correctors and recognizing proper nouns_.

In NLP we use vector representations of natural language words and text and some **distance metrics for those vectors**.

This collection of documents is called a **corpus**, and the collection of words or sequences we've listed in our index is called a lexicon.

Counting all words that appear in a sentence, can end up in losing information. A count of each possible word in your language, without any sequence or order associated with those words are not very helpful (bag of words). 

>SORTER AFTER TOKENIZER!

All the different ways that words could be combined to create these vectors is called a **vector space**. And relationship between these vectors in this space are what make up our model.

- What is the closest bag of words in our database to a bag-of-words vector provided by the user?
  - Searching on google about "how to draw like a pro?". The **answer may be the page** with the closest bag-of-word available.

These vector space can be, and normally is, very high-dimensional. It's possible to have millions of dimensions.


###  4.3. <a name='Abriefoverflightofhyperspace'></a>A brief overflight of hyperspace


###  4.4. <a name='Testse'></a>Testse