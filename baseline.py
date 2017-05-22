# coding:utf-8
import sys
import struct
import math
import numpy as np
import os
import jieba

#reload(sys)
#sys.setdefaultencoding( "utf-8" )

max_w = 50
float_size = 4

def load_vectors(input):
    print "begin load vectors"
    input_file = open(input, "rb")
    words_and_size = input_file.readline()
    words_and_size = words_and_size.strip()
    words = long(words_and_size.split(' ')[0])
    size = long(words_and_size.split(' ')[1])
    print "words =", words
    print "size =", size
    word_vector = {}
    for b in range(0, words):
        a = 0
        word = ''
        while True:
            c = input_file.read(1)
            word = word + c
            if False == c or c == ' ':
                break
            if a < max_w and c != '\n':
                a = a + 1
        word = word.strip()
        vector = np.empty([200])
        for index in range(0, size):
            m = input_file.read(float_size)
            (weight,) = struct.unpack('f', m)
            vector[index] = weight
        word_vector[word.decode('utf-8')] = vector
    input_file.close()
    print "load vectors finish"
    return word_vector



def search_vector(d,word):
    if word!='\n':
        try:
            return d[word]
        except:
            return [0]*200
    return [0]*200


def sentence_to_matrix(d,sentence):
    vec=[]
    for word in sentence :
        vec.append(search_vector(d,word))
    return vec

def same(word_1,word_2):
    re=0
    for i in range(0,200):
        re=re+word_1[i]*word_2[i]
    return re

def similarity(question_vec,sentence_vec):
    result = 0.00
    i=0
    for word_1 in sentence_vec :
        tmp=0.00
        for word_2 in question_vec:
            #print word_1
            #print word_2
            if word_1!=None and word_2!=None:
                tmp=max( tmp , same(word_2,word_1))
        i=i+1
        result_=result+tmp
    return result/i


def _main():
    print "ok\n"
    d = load_vectors("vectors_train.bin")
    print "ok\n"
    question_file=open("questions.txt",'r')
    print "ok\n"
    document_file=open("document.txt",'r')
    print "ok\n"
    baseline_result=open("baseline_result.txt",'w')
    while 1:
        question_text=question_file.readline()
        document_text=document_file.readline()
        if (not question_text) or (not document_text):
            break
        question_vec=[[0]*200]*1000
        sentence_vec=[[0]*200]*1000
        question_text=jieba.cut(question_text)
        document_text=jieba.cut(document_text)
        question_vec=sentence_to_matrix(d,question_text)
        sentence_vec=sentence_to_matrix(d,document_text)
        evaluation=0.0
        i=1
        for word_1 in sentence_vec:
            now_best=0.0
            for word_2 in question_vec:
                tmp=0.0
                word_1_size=0.0
                word_2_size=0.0
                for i in range(0,200):
                    tmp+=word_1[i]*word_2[i]
                    word_1_size+=word_1[i]*word_1[i]
                    word_2_size+=word_2[i]*word_2[i]
                if word_1_size!=0 and word_2_size!=0:
                    tmp=tmp/(math.sqrt(word_1_size)*math.sqrt(word_2_size))
                now_best=max(now_best,tmp)
            i=i+1
            evaluation=evaluation+now_best
        evaluation=evaluation/i
        baseline_result.write('%f' % evaluation)
        #print evaluation
        #print '\t'
        #print question_text
        #print '\t'
        #print document_text
        baseline_result.write('\n')



_main()

