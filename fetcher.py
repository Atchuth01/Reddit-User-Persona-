def fetch_user_data(reddit, username):
    user = reddit.redditor(username)
    posts, comments = [], []

    for post in user.submissions.new(limit=100):
        posts.append({
            'title': post.title,
            'text': post.selftext,
            'subreddit': str(post.subreddit),
            'permalink': "https://www.reddit.com" + post.permalink
        })

    for comment in user.comments.new(limit=100):
        comments.append({
            'body': comment.body,
            'subreddit': str(comment.subreddit),
            'permalink': "https://www.reddit.com" + comment.permalink
        })

    return posts, comments
