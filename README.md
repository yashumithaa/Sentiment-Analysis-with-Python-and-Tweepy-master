# Sentiment-Analysis
<br>Aim : </b>Sentiment Analysis of Tweets taken from Twitter Database

# Abstract : <br />
The trend of feedback and opinion sharing has changed since a few years. With the launch of Social Medias people have a better platform to spread their opinion on any topic by the use of hashtag feature. Hashtags makes it easier to extract content related to a specific topic of interest.<br />
Sentiment Analysis Project focuses on fetching tweets from Twitter Database with a specific hashtag provided by the user. The content of the hashtag is analyzed to draw conclusion if the general public has a Positive, Negative or Neutral view about the topic.

# Setting up the project : <br/>

<p>The following libraries needs to be installed to execute the program in Windows Environment</p>
  <ul>
  <li>Tweepy</li>
  <li>TextBlob</li>
  <li>Colorama</li>
  </ul>
  
<ul>
  <b>Setting up Twitter Account</b>
  <li>Log into your <a href="https://www.twitter.com">Twitter Account</a></li>
  <li>Navigate to the url <a href="https://developer.twitter.com">Twitter Developer</a></li>
  <li>On the top right click on your account name and select apps</li>
  <li>Once the page is loaded click create an app option</li>
  <li>Fill in the details and create the application</li>
  <li>Once the app is created Twitter will notify you via email</li>
  <li>Again browse to the apps page and click on details on right side of app name</li>
  <li>Take a note of <b>Consumer Key and Secret</b>, <b>Access key and secret</b>
  <li>In the file sentiment.py navigate to line 17 and replace the variable values with the values copied from website</li>
  </ul>
  
  # Running the program : <br/>
  Run the file using Python Interpreter. When prompted give the hashtag name and number of Tweets required.
