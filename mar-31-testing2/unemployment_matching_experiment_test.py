from collections import namedtuple
import unittest
from unemployment_matching_experiment import build_comment_portfolio


def test_bcp_empty():
    user_comments = []
    user_comment_data = []
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == []

#user_comment_data.append(
# [comment.author, comment.created_utc, comment.id, comment.body, 
# comment.subreddit,
# comment.score, comment.parent_id, comment.is_submitter])

class Empty :
    pass

def test_real_comment() :
    comment = Empty()
    comment.author = 1
    comment.created_utc = 1
    comment.id = 1
    comment.body = 1
    comment.subreddit = 1
    comment.score = 1
    comment.parent_id = 1
    comment.is_submitter = 1 
    user_comment_data = []
    user_comments = [comment]
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == [[1,1,1,1,1,1,1,1]]

class Comment :
    def __init__(self, author, created_utc, id, body, subreddit, score, parent_id, is_submitter) :
        self.author = author
        self.created_utc = created_utc
        self.id = id
        self.body = body
        self.subreddit = subreddit
        self.score = score
        self.parent_id = parent_id
        self.is_submitter = is_submitter

def test_real_commentClass() :
    comment = Comment(1,1,1,1,1,1,1,1)
    user_comment_data = []
    user_comments = [comment]
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == [[1,1,1,1,1,1,1,1]]

def test_twocomments() :
    comment1 = Comment(1,1,1,1,1,1,1,1)
    comment2 = Comment(2,1,1,1,1,1,1,1)
    user_comment_data = []
    user_comments = [comment1, comment2]
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == [[1,1,1,1,1,1,1,1], [2,1,1,1,1,1,1,1]]

def test_runtwice() :
    comment1 = Comment(1,1,1,1,1,1,1,1)
    comment2 = Comment(2,1,1,1,1,1,1,1)
    user_comment_data = []
    user_comments = [comment1]
    build_comment_portfolio(user_comments,user_comment_data)
    user_comments = [comment2]
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == [[1,1,1,1,1,1,1,1], [2,1,1,1,1,1,1,1]]

def test_real_commentTuple() :
    Comment = namedtuple("Comment", "author created_utc id body subreddit score parent_id is_submitter")
    user_comment_data = []
    user_comments = [Comment(1,1,1,1,1,1,1,1)]
    build_comment_portfolio(user_comments,user_comment_data)
    assert user_comment_data == [[1,1,1,1,1,1,1,1]]