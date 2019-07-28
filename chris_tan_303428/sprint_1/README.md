
# csda 1050

### Sprint #1 for Capstone Project
**Abstract for the Capstone Project**: This is for the fulfillment of the York University’s Advanced Analytics Course Capstone Project. The aim of this project is to uncover insights from the social media spacethrough programmatic means

**Project Scope**
Here are the boundaries of the project:
1.	Social media channel: Twitter (to include Facebook if time permits)
2.	Social media scope: Major Canadian Financial Institutions (FI) like BMO, CIBC, RBC, Scotiabank, TD (to include digital banks like Simplii, Tangerine, EQ if time permits)
3.	Comparison of the following insights across the above FIs: Sentiment Analysis (polarity and categorical); Word Cloud (conversation drivers); Key-word dendrogram (blend of sentiment and conversation drivers); Network Analysis (demographics and product segmentation). Paraphrases of these insights are given in the “Research Questions” section below

**Research Questions**
Here are the research questions for this project:
1.	Which bank has the most favourable / unfavourable trending opinion?
2.	What are the current financial products being discussed?
3.	What are the current emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) towards each bank?
4.	What are the current sentiments towards trending financial product segments / categories (and the general network of terms being tweeted)?

**Sprint#1 Objectives**
1.  Collect Twitter data
2.  Conduct Exploratory Data Analysis on the Twitter data
3.  Evaluate feasibility of research questions

What is needed to be done to run it
1.	Go to http://apps.twitter.com to register for a developer's account
2.	Once approved, Twitter will provide four OAuth parameters to you:
	a.	API Key
	b.	API Token
	c.	Access Token
	d.	Access Token Secret
	These four parameters help you tap into Twitter's APIs to gather the tweets
3.	You will also need an R IDE (I use RStudio) to run the R codes

**Results/findings**
Based on this exploratory data analysis (EDA), the author assessed whether the stated research questions are feasible, and as such, whether an edit of the research question is needed

*Research Q#1*. Which bank has the most favourable / unfavourable trending opinion?
*Comments*: About 1,623 tweets have been collected since July 7th, 2019, with close 5,500 terms. The collection will increase in the next several weeks. It should be feasible to answer this research question. The main drawback is for the low count of CIBC tweets (40 tweets) versus that of Scotia Bank (661 tweets).  The wide difference will skew the analysis, especially that of CIBC's

*Research Q#2*. What are the current financial products being discussed?
*Comments*: The EDA shows that frequent terms related to banking products are generic ones like, stock, charges, account. Unless we have a much more collection of tweets, it will be difficult to objectibely address this reserach question

*Research Q#3*. What are the current emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) towards each bank?
*Comments*: Not shown in this Sprint#1 report as the codes are still experimental, the author managed to "see" these emotional terms at the AllBanks level.  Again, due to the low tweet count for CIBC, it may be difficult to pin down the sentiments, especially in these 8 categories towards CIBC

*Research Q#4*. What are the current sentiments towards trending financial product segments / categories (and the general network of terms being tweeted)?
*Comments*: As stated above, frequent terms related to banking products are generic ones, hence it will be difficult to assess sentiments towards product segments. Network of terms is certainly a possibility
