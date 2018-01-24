import BeautifulSoup
from selenium import webdriver

baseURL = 'https://snoopsnoo.com/u/'

summary = ''
synopsis = ''
userSummary = {}
userSynopsis = {}

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
    global userSummary
    #Redditor since
    userSummary['signUpDate'] = summary.find('span', {"id": "data-signup_date"}).string
    #Longest period between two consecutive posts
    userSummary['lurkPeriodHumanized'] = summary.find('span', {"id": "data-lurk_period_humanized"}).string
    userSummary['lurkPeriodDates'] = summary.find('span', {"id": "data-lurk_period_dates"}).string
    #Gilded
    userSummary['gildedPosts'] = summary.find('span', {"id": "data-submissions_gilded"}).string
    userSummary['gildedComments'] = summary.find('span', {"id": "data-comments_gilded"}).string
    #Submission karma
    userSummary['postKarma'] = summary.find('span', {"id": "data-submission_karma"}).string
    userSummary['totalPosts'] = summary.find('span', {"id": "data-total_submissions"}).string
    userSummary['karmaPerPost'] = summary.find('span', {"id": "data-average_submission_karma"}).string
    userSummary['comparePostKarma'] = summary.find('span', {"id": "data-compare_submission_karma"}).string
    #Comment karma
    userSummary['commentKarma'] = summary.find('span', {"id": "data-comment_karma"}).string
    userSummary['totalComments'] = summary.find('span', {"id": "data-total_comments"}).string
    userSummary['karmaPerComment'] = summary.find('span', {"id": "data-average_comment_karma"}).string
    userSummary['compareCommentKarma'] = summary.find('span', {"id": "data-compare_comment_karma"}).string
    #Best comment
    bestComment = summary.find('span', {"id": "data-best_comment"}).parent.parent
    userSummary['bestCommentText'] = bestComment.findAll('p')[1].string
    userSummary['bestCommentLink'] = bestComment.find('a').get('href')
    #Worst comment
    worstComment = summary.find('span', {"id": "data-worst_comment"}).parent.parent
    userSummary['worstCommentText'] = worstComment.findAll('p')[1].string
    userSummary['worstCommentLink'] = worstComment.find('a').get('href')
    #Best post
    bestPost = summary.find('span', {"id": "data-best_submission"})
    userSummary['bestPostText'] = bestPost.contents[0]
    userSummary['bestPostLink'] = bestPost.find('a').get('href')
    #Worst post
    worstPost = summary.find('span', {"id": "data-worst_submission"})
    userSummary['worstPostText'] = worstPost.contents[0]
    userSummary['worstPostLink'] = worstPost.find('a').get('href')

def parseSynopsis():
    global userSynopsis
    rows = synopsis.findAll('div', {"class": "row"})
    for row in rows:
        key = row.contents[0].string
        contents = row.contents[1].findAll('span', {"class": "content"})
        values = []
        if key in userSynopsis:
            values = userSynopsis[key]
        for content in contents:
            values.append(content.string)
        userSynopsis[key] = values

def getSynopsis():
    for key in userSynopsis:
        print(key)
        print(userSynopsis[key])
