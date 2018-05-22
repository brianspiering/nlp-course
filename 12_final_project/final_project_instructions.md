Natural Language Processing Final Project
------

Due date: 2018-06-29 at 9am
Purpose: Build an end-to-end system to model meaning in text.

### Learning Outcomes:

- Formulate a meaningful and answerable Data Science research question
- Clean raw text data from the web
- Create and tune a machine learning model
- Write working and well-organized code

You should follow the Data Science Workflow:

1. Ask the right question
2. Acquire the relevant data
3. Process the data: Understand, clean, and organize
4. Model: Apply Statistics, Machine Learning, and Deep Learning
5. Deliver: Create a poster presentation or report

These steps are iterative (do a little preprocessing, do a little modeling, redo the preprocessing, …).

This project will become a part of your public Data Science portfolio, thus all data must be public data.  

----
1. Ask the right question
----

This is your individual project so it is up to you to develop the right question. See `examples` and `quantitative rubric` for guidance about types of questions.

----
2. Acquire the relevant data
----

It is best if you pick an unique dataset. Just make sure the data is apporiate, it needs to be approved by the instructor. Acquiring data should not take away from the other aspects of the project. See `datasets` for pre-approved datasets.

----
3. Process the data
----

### Exploratory Data Analysis (EDA):

- What specific munging issues do you have to address (e.g., encoding, missing data, or data to exclude)?
- What descriptive/summary statistics are useful for understanding your data?
- What figures provide insight into your data?

### Preprocessing: 

- How did you tokenize words? Is “didn’t” one token or two? Why did you make that choice?
- Did you normalize your tokens in any way (case, stemming, lemmatization)? If so, how? Why or why not?
- Explore the frequency counts. Are there any terms that should be removed from your feature set? Why or why not?
- Does removing stop-wording or hapaxes help?
- Did you segment sentences? If so, why and how?

### Vectorizing:

- How did different vectorizations effect the modeling step?
- Did choosing between binary, count, tf-idf, or embeddings have an effect? Why or why not?

----
3. Model
----

Pick at least 1 type of modeling:

### Classification / Sentiment Analysis:

- How noisey were the labels? How did you handle mislabeled or unlabeled data?
- How did you handle class imbalance?
- How did Naive Bayes, Logistic Regression, and SVM compare?
- What were the most common misclassifications? What are possible reasons?

### Clustering / Topic Modeling:

- How "clean" were the clusters?
- How did changing the number of clusters effect your results?
- What insights did clustering give you into the data?

See `quantitative rubric` for modeling standards.

For each step, I want both an empirical and a logical justification for the choices you made. That is: show us that the choice you picked is empirically superior to the alternative (better F1 score, etc.) and explain why you think that is.  

----
5. Deliver
-----

You'll create either a poster presentation or report. Pick only one. Both are due at the beging of the last day of class. The performed format for a report is a Jupyter Notebook in GitHub. The poster presentation will also have an associated GitHub repo. The presentation and organization of your repo and code style will be scored. 

More details to come.

----
Extra Credit
----

Explore advanced options of your choosing. Suggestions:  

- Did you search the hyperparameters of your models (i.e., optimization)?  
- Did ensembling improve your model's performance?
- Can you explore your data or models through advanced visualizations (e.g., t-sne or network analysis)?
- Can you fit your model to elements within the entire corpus? Can you assign sentiment to individual topics within the review (e.g., “great food, lousy service”)?   
- How would you turn your project in a data product?
- Create automated pipelines to put your project into production.

----
Hints
----

- Make it run, make it right, make it fast. (in that order)
- Go end-to-end as quickly possible. From raw data -> simple model -> evaluation. Then explore options for each stage.
- [Tips if model is not working](https://blog.slavv.com/37-reasons-why-your-neural-network-is-not-working-4020854bd607)
- How do get a "A"? Do something groundbreaking (seriously). Either ground-breaking for the field or for the class.
    + For example, fit evaluation metrics not covered in class - "[Beyond Accuracy, F-score and ROC...](http://transsearch.iro.umontreal.ca/rali/sites/default/files/publis/EvAAAI06finMay10.pdf)"
