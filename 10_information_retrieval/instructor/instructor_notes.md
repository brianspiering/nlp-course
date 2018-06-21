Information Retrieval, Introduction
-----

----
Agenda
----

1. OYO
1. Lecture
1. Lab
    - overall plan
    - Reread the whole thing
    - https://github.com/jupyterlab/jupyterlab as IDE

---
OYO
---

- Google
- Bing 
- Baidu
- Yahoo
- pintrest
- bloomberg
- indeed
- giphy
- slack

\*every tech company



----
Extra RAT questions
---



----

2) Given the incidence vectors for Facebook, Instagram, and Twitter:  

| Term | Incidence Vector  |  
|:-------:|:------:|
| Facebook | 110001 |
| Instagram | 100000 |  
| Twitter | 010000 |  

What is the incidence vector corresponding to the query “(Facebook or Instagram) and __not__ Twitter”?


facebook = [True, True, False, False, False, False, True]
instagram = [True, True, False, False, False, False, False]
twitter = [False, True, False, False, False, False, False]

[(facebook[i] or instagram[i]) and not twitter[i] for i in range(len(facebook))]

2) Brian's answer = `100001`

----

3) Define information retrieval query in Plain English. What are the most common challenges around parsing queries? Give an example of a well-defined and ill-defined query (A prize for best ill-defined query).

Example of ill-defined query:

> Hi Baidu, how are you? I ate noodles at a corner store last week and they were delicious. Do you think they’re on sale this weekend?

http://www.huffingtonpost.com/2015/05/13/andrew-ng_n_7267682.html
3) If the length of two postings lists are x and y, then what is the tightest upper bound on the running time of merging the postings lists in an OR query in this manner?<br>
&nbsp;&nbsp; A. O(max{x,y})  
&nbsp;&nbsp; B. O(min{x,y})  
&nbsp;&nbsp; C. O(x+y)  
&nbsp;&nbsp; D. O(xy) 

3) C
The merge takes O(x+y) time because in the best or worst case scenario you have to go through the entire postings list for each term (therefore it is also o(x+y) for best case.  


__2)__ If we have a corpus of:
- 1 million documents, each of length 2,000 words
- a total vocabulary size of 400,000

What is the approximate maximum size of the postings? <br>
<br>
What is the size of the (non-sparse) co-occurrence matrix (which contains a 1 in row i and column j if word i occurs in document j and a 0 otherwise)?
<br><br>

__ANSWER__
2. The maximum size of the postings is $2\times10^9$ <br>
The size of the (non-sparse) co-occurrence matrix is $4\times10^{11}$ <br>
<br>

<br>
<br> 
<br>

----
