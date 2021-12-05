
import praw
import pandas as pd
import json

reddit_read_only = praw.Reddit(client_id="05YBTvie-hXYa1753iEoOw",         # your client id
                               client_secret="tiYXGZXoAjAx7Kn5ubLSctw4za_Ltw",      # your client secret
                               user_agent="Chrome",
                                ratelimit_seconds=10)        # your user agent

subreddit = reddit_read_only.subreddit("productivity")

# Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
# print("Title:", subreddit.title)
                              
# print("Description:", subreddit.description)
# print("-------------------------------------------------------------------")
# for submission  in subreddit.hot(limit=10):
#   print(submission.title)
#   print(submission.score)
#   print(submission.author)
#   # print(submission.body)
#   print("-------------------------------------------------------------------")


# print("-------------------------------------------------------------------")

posts = subreddit.top("year")
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)
 
top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv('FILENAME.csv', index=True) 


# json_object = json.dumps(posts_dict) 
# print(json_object)
