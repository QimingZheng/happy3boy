# coding:utf-8
import sys
import struct
import math
import numpy as np
import os

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
    print d[word]
    return 1


def sentence_to_matrix(d,sentence):
    vec=[]
    for word in sentence :
        vec.append(search_vector(d,word))
    return vec

def same(word_1,word_2):
    for i in range(0,200):
        if(word_1[i]!=word_2[i]):
            return False
    return True

def similarity(question_vec,sentence_vec):
    result = 0.00
    i=0
    for word_1 in sentence_vec :
        tmp=0.00
        for word_2 in question_vec:
             tmp=max(tmp,same(word_2,word_1))
        i=i+1
        result_=tmp
    return result/i


def _main():
    print "ok\n"
    d = load_vectors("vectors_dev.bin")
    print "ok\n"
    question_file=open("questions.txt",'r')
    print "ok\n"
    document_file=open("document.txt",'r')
    print "ok\n"
    baseline_result=open("baseline_result.txt",'w')
    question_text=question_file.read()
    document_text=document_file.read()
    question_vec=[[0]*200]*1000
    sentence_vec=[[0]*200]*1000
    i=0
    for question in question_text:
        sentence=document_text[i]
        print question
        print sentence
        i=i+1
        question_vec=sentence_to_matrix(d,question.encode("utf8"))
        sentence_vec=sentence_to_matrix(d,sentence.encode("utf8"))
        baseline_result.write(similarity(question_vec,sentence_vec))
        baseline_result.write('\n')
    return


_main()









