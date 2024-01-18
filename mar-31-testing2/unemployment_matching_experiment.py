
def build_comment_portfolio(user_comments,user_comment_data, expected_author):
    #iterate through all the comments for a given user
    for comment in user_comments:
        if(expected_author == comment.author) :
            user_comment_data.append(
            [comment.author, comment.created_utc, comment.id, comment.body, comment.subreddit, comment.score, comment.parent_id, comment.is_submitter])
        else :
            # throw an exception
            # skip it
                # print debugging information
                # log stuff
                # ...
            # mark the data as suspicious
            # assigning a default value
            # computing a value based on neighbors