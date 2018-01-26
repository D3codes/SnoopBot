from __future__ import print_function
import BeautifulSoup
from selenium import webdriver
import time
import sys

BROWSER = webdriver.PhantomJS()
BASE_URL = 'https://snoopsnoo.com/u/'

userSummary = {}
userSynopsis = {}

def search(user):
    try:
        page = getPage(BASE_URL + user)
        waitCounter = 0
        print('Waiting for page to load')
        print('[*', end='')
        sys.stdout.flush()
        while page.find('div', {"class": "loading-progress"}):
            time.sleep(15)
            print('*', end='')
            sys.stdout.flush()
            waitCounter+=1
            page = getPage(BASE_URL + user)
            if waitCounter >= 8:
                break
        print(']')
        summary = page.find('div', {"id": "summary"})
        synopsis = page.find('div', {"id": "synopsis-data"})
        parseSummary(summary)
        parseSynopsis(synopsis)
    except:
        printError('No user found')

def getPage(url):
    BROWSER.get(url)
    return BeautifulSoup.BeautifulSoup(BROWSER.page_source)

def parseSummary(summary):
    global userSummary
    userSummary = {}
    #Redditor since
    userSummary['signUpDate'] = summary.find('span', {"id": "data-signup_date"}).string
    #Longest period between two consecutive posts
    userSummary['lurkPeriodHumanized'] = summary.find('span', {"id": "data-lurk_period_humanized"}).string
    userSummary['lurkPeriodDates'] = summary.find('span', {"id": "data-lurk_period_dates"}).string
    #Gilded
    userSummary['gildedPosts'] = summary.find('span', {"id": "data-submissions_gilded"}).string
    if userSummary['gildedPosts'] == None:
        userSummary['gildedPosts'] = summary.find('span', {"id": "data-submissions_gilded"}).find('a').string
    userSummary['gildedComments'] = summary.find('span', {"id": "data-comments_gilded"}).string
    if userSummary['gildedComments'] == None:
        userSummary['gildedComments'] = summary.find('span', {"id": "data-comments_gilded"}).find('a').string
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

def parseSynopsis(synopsis):
    global userSynopsis
    userSynopsis = {}
    rows = synopsis.findAll('div', {"class": "row"})
    for row in rows:
        key = row.contents[0].string
        contents = row.contents[1].findAll('span', {"class": "content"})
        contents += row.contents[1].findAll('span', {"class": "likely"})
        values = []
        if key in userSynopsis:
            values = userSynopsis[key]
        for content in contents:
            values.append(content.string)
        userSynopsis[key] = values

def printUserSynopsis():
    for key in userSynopsis:
        print(key.upper())
        for value in userSynopsis[key]:
            print(value)
        print('--------------------------------')

def printUserSummary():
    for key in userSummary:
        print(key.upper())
        print(userSummary[key])
        print('--------------------------------')

def printError(message):
    print('--------------------------------')
    print('ERROR: ' + message)
    print('--------------------------------')
