import BeautifulSoup
from selenium import webdriver

baseURL = 'https://snoopsnoo.com/u/'

summary = ''
synopsis = ''
userInfo = {}
userGuesses = {}

def search(user):
    browser = webdriver.PhantomJS()
    browser.get(baseURL + user)
    doc = BeautifulSoup.BeautifulSoup(browser.page_source)
    global summary
    summary = doc.find('div', {"id": "summary"})
    global synopsis
    synopsis = doc.find('div', {"id": "synopsis-data"})
    parseSummary()
    parseSynopsis()

def parseSummary():
    global userInfo
    #Redditor since
    userInfo['signUpDate'] = summary.find('span', {"id": "data-signup_date"}).string
    #Longest period between two consecutive posts
    userInfo['lurkPeriodHumanized'] = summary.find('span', {"id": "data-lurk_period_humanized"}).string
    userInfo['lurkPeriodDates'] = summary.find('span', {"id": "data-lurk_period_dates"}).string
    #Gilded
    userInfo['gildedPosts'] = summary.find('span', {"id": "data-submissions_gilded"}).string
    userInfo['gildedComments'] = summary.find('span', {"id": "data-comments_gilded"}).string
    #Submission karma
    userInfo['postKarma'] = summary.find('span', {"id": "data-submission_karma"}).string
    userInfo['totalPosts'] = summary.find('span', {"id": "data-total_submissions"}).string
    userInfo['karmaPerPost'] = summary.find('span', {"id": "data-average_submission_karma"}).string
    userInfo['comparePostKarma'] = summary.find('span', {"id": "data-compare_submission_karma"}).string
    #Comment karma
    userInfo['commentKarma'] = summary.find('span', {"id": "data-comment_karma"}).string
    userInfo['totalComments'] = summary.find('span', {"id": "data-total_comments"}).string
    userInfo['karmaPerComment'] = summary.find('span', {"id": "data-average_comment_karma"}).string
    userInfo['compareCommentKarma'] = summary.find('span', {"id": "data-compare_comment_karma"}).string
    #Best comment
    bestComment = summary.find('span', {"id": "data-best_comment"}).parent.parent
    userInfo['bestCommentText'] = bestComment.findAll('p')[1].string
    userInfo['bestCommentLink'] = bestComment.find('a').get('href')
    #Worst comment
    worstComment = summary.find('span', {"id": "data-worst_comment"}).parent.parent
    userInfo['worstCommentText'] = worstComment.findAll('p')[1].string
    userInfo['worstCommentLink'] = worstComment.find('a').get('href')
    #Best post
    bestPost = summary.find('span', {"id": "data-best_submission"})
    userInfo['bestPostText'] = bestPost.contents[0]
    userInfo['bestPostLink'] = bestPost.find('a').get('href')
    #Worst post
    worstPost = summary.find('span', {"id": "data-worst_submission"})
    userInfo['worstPostText'] = worstPost.contents[0]
    userInfo['worstPostLink'] = worstPost.find('a').get('href')

def parseSynopsis():
    global userGuesses
    rows = synopsis.findAll('div', {"class": "row"})
    for row in rows:
        print(row.contents[0].string)
