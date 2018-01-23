import BeautifulSoup
from selenium import webdriver

baseURL = 'https://snoopsnoo.com/u/'

summary = ''
synopsis = ''

def search(user):
    browser = webdriver.PhantomJS()
    browser.get(baseURL + user)
    doc = BeautifulSoup.BeautifulSoup(browser.page_source)
    global summary
    summary = doc.find('div', {"id": "summary"})
    global synopsis
    synopsis = doc.find('div', {"id": "synopsis-data"})

def signUpDate():
    return summary.find('span', {"id": "data-signup_date"}).string

def lurkPeriodHumanized():
    return summary.find('span', {"id": "data-lurk_period_humanized"}).string

def lurkPeriodDates():
    return summary.find('span', {"id": "data-lurk_period_dates"}).string

def gildedPosts():
    return summary.find('span', {"id": "data-submissions_gilded"}).string

def gildedComments():
    return summary.find('span', {"id": "data-comments_gilded"}).string

def postKarma():
    return summary.find('span', {"id": "data-submission_karma"}).string

def totalPosts():
    return summary.find('span', {"id": "data-total_submissions"}).string

def karmaPerPost():
    return summary.find('span', {"id": "data-average_submission_karma"}).string

def comparePostKarma():
    return summary.find('span', {"id": "data-compare_submission_karma"}).string

def commentKarma():
    return summary.find('span', {"id": "data-comment_karma"}).string

def totalComments():
    return summary.find('span', {"id": "data-total_comments"}).string

def karmaPerComment():
    return summary.find('span', {"id": "data-average_comment_karma"}).string

def compareCommentKarma():
    return summary.find('span', {"id": "data-compare_comment_karma"}).string

def bestCommentText():
    bestComment = summary.find('span', {"id": "data-best_comment"}).parent.parent
    return bestComment.findAll('p')[1].string

def bestCommentLink():
    bestComment = summary.find('span', {"id": "data-best_comment"}).parent.parent
    return bestComment.find('a').get('href')

def worstCommentText():
    worstComment = summary.find('span', {"id": "data-worst_comment"}).parent.parent
    return worstComment.findAll('p')[1].string

def worstCommentLink():
    worstComment = summary.find('span', {"id": "data-worst_comment"}).parent.parent
    return worstComment.find('a').get('href')

def bestPostText():
    bestPost = summary.find('span', {"id": "data-best_submission"})
    print(bestPost.split('<small>')[0])
    return bestPost.string

def bestPostLink():
    bestPost = summary.find('span', {"id": "data-best_submission"})
    return bestPost.find('a').get('href')

def worstPostText():
    worstPost = summary.find('span', {"id": "data-worst_submission"})
    return worstPost.findAll('p')[1].string

def worstPostLink():
    worstPost = summary.find('span', {"id": "data-worst_submission"})
    return worstPost.find('a').get('href')

def parseSummary():
    #Redditor since
    signupDate = summary.find('span', {"id": "data-signup_date"}).string
    #Longest period between two consecutive posts
    lurkPeriodHumanized = summary.find('span', {"id": "data-lurk_period_humanized"}).string
    lurkPeriodDates = summary.find('span', {"id": "data-lurk_period_dates"}).string
    #Gilded
    gildedPosts = summary.find('span', {"id": "data-submissions_gilded"}).string
    gildedComments = summary.find('span', {"id": "data-comments_gilded"}).string
    #Submission karma
    postKarma = summary.find('span', {"id": "data-submission_karma"}).string
    totalPosts = summary.find('span', {"id": "data-total_submissions"}).string
    karmaPerPost = summary.find('span', {"id": "data-average_submission_karma"}).string
    comparePostKarma = summary.find('span', {"id": "data-compare_submission_karma"}).string
    #Comment karma
    commentKarma = summary.find('span', {"id": "data-comment_karma"}).string
    totalComments = summary.find('span', {"id": "data-total_comments"}).string
    karmaPerComment = summary.find('span', {"id": "data-average_comment_karma"}).string
    compareCommentKarma = summary.find('span', {"id": "data-compare_comment_karma"}).string
    #Best comment
    bestComment = summary.find('span', {"id": "data-best_comment"}).parent.parent
    bestCommentText = bestComment.findAll('p')[1].string
    bestCommentLink = bestComment.find('a').get('href')
    #Worst comment
    worstComment = summary.find('span', {"id": "data-worst_comment"}).parent.parent
    worstCommentText = worstComment.findAll('p')[1].string
    worstCommentLink = worstComment.find('a').get('href')
    #Best post
    bestPost = summary.find('span', {"id": "data-best_submission"})
    bestPostText = bestPost.find('p')
    bestPostLink = bestPost.find('a').get('href')
    #Worst post
    worstPost = summary.find('span', {"id": "data-worst_submission"})
    worstPostText = worstPost.find('p')
    worstPostLink = worstPost.find('a').get('href')
