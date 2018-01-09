#!/usr/bin/env python3
import markovify
import time


def make_corpus():
    global corpus
    with open("speeches.txt") as speeches:
        #print("reading speeches.txt")
        trump_speeches = markovify.NewlineText(
            speeches, retain_original=False, )

    with open("trumptweets.txt") as tweets:
        #print("reading trumptweets.txt")
        trump_tweets = markovify.NewlineText(
            tweets, retain_original=False, )
    #print("Combining corpi?")
    corpus = markovify.combine([trump_speeches, trump_tweets],)
    #print("Corpi combined")

    return corpus


def make_tweet():
    tweet = corpus.make_short_sentence(280, tries=100)
    print(tweet)


def main():
    make_corpus()

    while True:
        make_tweet()
        print("[Sleeping for 10 seconds]")
        time.sleep(10)


if __name__ == '__main__':
    main()
