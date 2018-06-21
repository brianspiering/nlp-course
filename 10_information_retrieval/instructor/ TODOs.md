-----

- [Python package to build a search enginge](http://whoosh.readthedocs.io/en/latest/quickstart.html)

add to information retrieval https://www.youtube.com/watch?v=skccNnBtR4Y

----
Next Time
----
- Rewrite exercises
  + see ir_system_solutions_rewritten.py
  + to match lecture / wikipedia
  + add more comments and better docstrings
  + see below
  - Add unit tests to exercises
  - - add more info about index
  - is get_posting need?
  - convert to matrix from a dictionary of dictionary
- create toy examples
  - tf-idf
  -  cosine similary 
- add smaller unit
  + algorithm based, then run intergration tests
- rewrite solutions
  + add reduce solutions set solutions
    * 

-----
- Add Why IR is important?
    + more data
    + more savey user
- 
- Then add
    - Create woreked example of library system about "gardening books"
        - term/doc matrix
        - index
        -  boolean queries
        - evaluate precision
-  <img src="http://www.nature.com/nmeth/journal/v8/n6/images_article/nmeth.1619-F1.jpg" style="width: 400px;"/>
    Besides information retrieval, what are other applications of document similarity? 

- improve exercise
    +  ‘boolean_retrieve’ - this name confuses me. i got the right answer working, i’m not getting where the boolean comes. wouldn’t all search imply that they the returns contain’s (one or more) of your words? ‘contains all words’ not a better description?

   def boolean_retrieve(self, query):
       """
       Given a query in the form of a list of *stemmed* words, this returns
       the list of documents in which *all* of those words occur (ie an AND
       query).
       Return an empty list if the query does not return any documents.
       """
       
       # TODO: Implement Boolean retrieval. You will want to use your inverted index that you created in index().
       # XXX: Right now this just returns all the possible documents!
       docs = []
       q_list = set(self.inv_index[query[0]])
       for n,q in [(n,q) for n,q in enumerate(query) if n>0]:
           inv_index_answer = self.inv_index[q]
           q_list.intersection_update(inv_index_answer)
       q_list = set(q_list)
       return sorted(q_list)