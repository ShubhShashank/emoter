#!/usr/bin/python
# -*- coding: utf-8-*-
import os 

import time
import sys

import operator                  

import gc
import re
from nltk.tokenize import sent_tokenize
import re, math
from collections import Counter
from collections import OrderedDict
from difflib import SequenceMatcher
from string import punctuation

# Import emote library
from emote import emote

class Emoter(object):

    # Emoter script is not yet written as a library or module
    # emoterClassOn = False    # Is Emote being used as a library or modules? 
    runningScript = False   # Or is Emote being run as a script directly?
    firstTime = True     # Emote running for the first time?


    # Tone Clusters (grouping related tones to create clusters, so that categorizations are more general, and accurate)

    negative_tones_cluster = [
                                "negative", "vulgarity"
                             ]

    positive_tones_cluster = [
                                "positive", "love", "joy", "admiration", "pride"
                             ]

    joy_tones_cluster = [
                            "positive", "love", "joy", "admiration"
                        ]   

    anger_tones_cluster = [
                            "anger", "hate", "accusative", "vulgarity"
                          ]

    sad_tones_cluster = [                  
                            "regret", "negative"
                        ]

    # tones that make up questions cluster (is the user asking a question?)
    question_tones_cluster = [
                                "inquisitive", "confusion", "challenging"
                             ] 

    # tones that make up answers cluster (is the user saying something certain, factual, emphatic / analytical)
    fact_tones_cluster = [
                            "emphatic", "calm", "certainty"
                         ]

                          
    user_msg_analysis = {}


    # different types of messages and response pairs for various conversations                                                                   
    texts_encouragement_needed = []
    texts_criticism_needed = []
    texts_apologetic = []
    texts_questions = []
    texts_facts = []
    texts_greetings = []
    texts_salutations = []
    texts_all = {}


    # counter of conversation so far
    num_total_messages = 0
    num_user_messages = 0
    num_bot_messages = 0

    # overall tone levels of the conversation
    # not yet added
    overall_conv_tone_lvls = {}

    # has the bot found a response yet? (while looping in database)
    response_found = False

    # has the bot eliminated the default greetings and salutations texts?
    default_eliminated = False


    def __init__(self, message = "", 
                 ):

        self.train = train
        self.train = []

    

    def getInput(message):
        global firstTime
        global runningScript

        global num_total_messages
        global num_user_messages
        global response_found
        global default_eliminated

        if runningScript == True:
            if firstTime == False:
                response_found = False
                default_eliminated = False
                message = input('\n\n\t  Y O U: ')
                num_total_messages+=1
                num_user_messages+=1
                msg_results = emote.runAnalysis(message)
                os.system('cls')
                print('\n\tEmoter Agent Analysis Report',)
                # print('\n\tOverall Conversation Levels: ', )
                print('\n\tYour message was: ', message)
                parseMessage(message, msg_results) 
            else: 
                os.system('cls')
                print("""\n\n\tNow starting Emoter, the chatbot with emotional intelligence.""")
                print("""\n\n\tTraining database with loaded Emoter module: """, "fitness coach")
                print("""\n\n\tStarting conversation.. """)
                firstTime = False
                getInput(message)
        else:
            # This would be for Emoter running as a module or library. This Emoter script does not yet return any values as a library or class
            pass
            # if firstTime == True:
                # print("\n\n\tRunning Emoter as a module / library..")
                # emoterClassOn = True
            # else:
                # emoterClassOn = False


    def trainDatabase():
       global texts_all; global texts_encouragement_needed; global texts_criticism_needed; global texts_questions; global texts_facts;  global texts_apologetic;
       global texts_tasks; global texts_greetings; global texts_salutations;
       
       # See emoter_fitness_coach.py for an example on conversation texts
       # Texts should be a list of tuples. First element of the tuple should be a user message, and the second element is the paired bot response.
       # Add more conversations / texts as needed for every Emoter agent persona

       texts_encouragement_needed = [

                                    ]  
                             
       texts_criticism_needed = [

                                ]

       texts_questions = [

                         ]

       texts_facts =     [

                         ]

       texts_tasks =    [
                        
                        ]


       texts_apologetic =    [

                             ]



       texts_greetings = [
                       
                         ]


       texts_salutations = [

                           ]
       
       texts_all['all'] = [
        
                          ]

       texts_all['encouragement_needed'] = texts_encouragement_needed; texts_all['criticism_needed'] = texts_criticism_needed; texts_all['questions'] = texts_questions; texts_all['facts'] = texts_facts;
       texts_all['tasks'] = texts_tasks;  texts_all['apologetic'] = texts_apologetic; texts_all['greetings'] = texts_greetings; texts_all['salutations'] = texts_salutations

       return texts_all


    def parseMessage(message, msg_results):

        tone_1 = ""; tone_2 = ""; tone_3 = ""; tone_4 = ""; tone_5 = ""; tone_6 = ""; tone_7 = ""; tone_8 = ""
        tone_1_val = 0; tone_2_val = 0; tone_3_val = 0; tone_4_val = 0; tone_5_val = 0; tone_6_val = 0; tone_7_val = 0; tone_8_val = 0
        tone_1 = msg_results[0][0][0]; tone_1_val = msg_results[0][0][1]; 
        tone_2 = msg_results[0][1][0]; tone_2_val = msg_results[0][1][1] 
        tone_3 = msg_results[0][2][0]; tone_3_val = msg_results[0][2][1] 
        tone_4 = msg_results[0][3][0]; tone_4_val = msg_results[0][3][1] 
        tone_5 = msg_results[0][4][0]; tone_5_val = msg_results[0][4][1] 
        tone_6 = msg_results[0][5][0]; tone_6_val = msg_results[0][5][1] 
        tone_7 = msg_results[0][6][0]; tone_7_val = msg_results[0][6][1] 
        tone_8 = msg_results[0][7][0]; tone_8_val = msg_results[0][7][1] 
        msg_results_dict_full = {}
        msg_results_dict_full['tone_1'] = [tone_1, tone_1_val]; msg_results_dict_full['tone_2'] = [tone_2, tone_2_val]; 
        msg_results_dict_full['tone_3'] = [tone_3, tone_3_val]; msg_results_dict_full['tone_4'] = [tone_4, tone_4_val]; 
        msg_results_dict_full['tone_5'] = [tone_5, tone_5_val]; msg_results_dict_full['tone_6'] = [tone_6, tone_6_val]; 
        msg_results_dict_full['tone_7'] = [tone_7, tone_7_val]; msg_results_dict_full['tone_8'] = [tone_8, tone_8_val]; 
        # print("\n\tMessage results analysis full dictionary: ", msg_results_dict_full)
        msg_results_dict_strong = {}
        msg_results_dict_strong['tone_1'] = [tone_1, tone_1_val]; msg_results_dict_strong['tone_2'] = [tone_2, tone_2_val]; 
        msg_results_dict_strong['tone_3'] = [tone_3, tone_3_val]; msg_results_dict_strong['tone_4'] = [tone_4, tone_4_val]; 
        # msg_results_dict_strong['tone_5'] = [tone_5, tone_5_val]

        print("\n\tStrongest tones detected: ", "\n\t\t", msg_results[0][0][0], msg_results[0][0][1], "\t", msg_results[0][1][0], msg_results[0][1][1], "\t", msg_results[0][2][0], msg_results[0][2][1],
              "\n\t\t", msg_results[0][3][0], msg_results[0][3][1], "\t", msg_results[0][4][0], msg_results[0][4][1])

        strongest_detected_tone = str(msg_results_dict_strong['tone_1'][0])
        strongest_detected_tone_val = str(msg_results_dict_strong['tone_1'][1])
        classifyToneClusters(message, msg_results_dict_strong)

        return msg_results_dict_strong


    def classifyToneClusters(message, msg_results_dict_strong):
        global texts_greetings
        print("\n\tCalculating tone cluster weights..")
        positive_tones_cluster_weight = 1; negative_tones_cluster_weight = 1; joy_tones_cluster_weight = 1; anger_tones_cluster_weight = 1;
        sad_tones_cluster_weight = 1; question_tones_cluster_weight = 1; fact_tones_cluster_weight = 1;
        for tone, value in msg_results_dict_strong.items():
            for i in range(len(positive_tones_cluster)):
                if value[0] == positive_tones_cluster[i]:
                    positive_tones_cluster_weight = positive_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tPositive tones cluster weight: ", (round(positive_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(negative_tones_cluster)):
                if value[0] == negative_tones_cluster[i]:
                    negative_tones_cluster_weight = negative_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tNegative tones cluster weight: ", (round(negative_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(joy_tones_cluster)):
                if value[0] == joy_tones_cluster[i]:
                    joy_tones_cluster_weight = joy_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tJoy tones cluster weight: ", (round(joy_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(anger_tones_cluster)):
                if value[0] == anger_tones_cluster[i]:
                    anger_tones_cluster_weight = anger_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tAnger tones cluster weight: ", (round(anger_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(sad_tones_cluster)):
                if value[0] == sad_tones_cluster[i]:
                    sad_tones_cluster_weight = sad_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tSad tones cluster weight: ", (round(sad_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(question_tones_cluster)):
                if value[0] == question_tones_cluster[i]:
                    question_tones_cluster_weight = question_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tQuestions tones cluster weight: ", (round(question_tones_cluster_weight, 2)))
                else:
                    pass
            for i in range(len(fact_tones_cluster)):
                if value[0] == fact_tones_cluster[i]:
                    fact_tones_cluster_weight = fact_tones_cluster_weight * math.sqrt(value[1])
                    # print("\t\t\tFacts tones cluster weight: ", (round(fact_tones_cluster_weight, 2)))
                else:
                    pass

        tone_clusters_weights_dict = {'positive': positive_tones_cluster_weight, 'negative': negative_tones_cluster_weight, 
                                      'joy': joy_tones_cluster_weight, 'anger': anger_tones_cluster_weight,
                                      'sad': sad_tones_cluster_weight, 'question': question_tones_cluster_weight
                                     }
        tone_clusters_weights_dict = sorted(tone_clusters_weights_dict.items(), key = operator.itemgetter(1),reverse = True)

        # print("\t  Tone cluster weights: ", tone_clusters_weights_dict)

        analyzeMessage(message, msg_results_dict_strong, tone_clusters_weights_dict)

        return tone_clusters_weights_dict


    def analyzeMessage(message, msg_results_dict_strong, tone_clusters_weights_dict):
        analysisResponse = ""
        strongest_tone_clusters = {}
        tone_cluster_1 = tone_clusters_weights_dict[0][0]; tone_cluster_1_val = tone_clusters_weights_dict[0][1];
        tone_cluster_2 = tone_clusters_weights_dict[1][0]; tone_cluster_2_val = tone_clusters_weights_dict[1][1];
        tone_cluster_3 = tone_clusters_weights_dict[2][0]; tone_cluster_3_val = tone_clusters_weights_dict[2][1];
        tone_cluster_4 = tone_clusters_weights_dict[3][0]; tone_cluster_4_val = tone_clusters_weights_dict[3][1];
        if tone_cluster_1_val > 1:
            strongest_tone_clusters['1'] = tone_cluster_1
        else:
            pass
        if tone_cluster_2_val > 1:
            strongest_tone_clusters['2'] = tone_cluster_2
        else:
            pass
        if tone_cluster_3_val > 1:
            strongest_tone_clusters['3'] = tone_cluster_3
        else:
            pass
        if tone_cluster_4_val > 1:
            strongest_tone_clusters['4'] = tone_cluster_4
        else:
            pass
        # print("\n\tStrongest tone clusters: ", tone_cluster_1, "\t", tone_cluster_2, "\t", tone_cluster_3, "\t")
        msg_results_dict_strong_sorted = sorted(msg_results_dict_strong.items(),key = operator.itemgetter(0))    
        # print("\n\tSorted strongest individual tones: ", msg_results_dict_strong_sorted)
        print("\n\tCreating analysis report based on tone grouping..")
        msg_is_positive = False; msg_is_negative = False; msg_is_question = False;  msg_is_fact = False; msg_is_anger = False; msg_is_joy = False; 
        msg_is_sad = False; msg_is_emphatic = False; msg_is_desire = False; msg_is_instructive = False; msg_is_certainty = False;
        msg_is_intensity = False; msg_is_challenging = False; msg_is_confusion = False; msg_is_accusative = False;  
        msg_analysis_description = ""

        # Some emotional classifications work better as clusters (joy, anger, negative, positive) because they're more encompassing, 
        # whereas other tones are significant enough on their own (emphatic, desire, instructive, etc.)
        for key, value in strongest_tone_clusters.items():
            print("\n\t\t", key, "\t", value)
            if value == 'positive':
                msg_is_positive = True
                # print("\t\tUser expresssed a positive sentiment.")
                msg_analysis_description+=("\n\t\tUser expresssed a positive sentiment. ")
            if value == 'negative': 
                msg_is_negative = True
                # print("\t\tUser expresssed a negative sentiment.")
                msg_analysis_description+=("\n\t\tUser expresssed a negative sentiment. ")
            if value == 'question':
                msg_is_question = True
                # print("\t\tUser is asking a question.")
                msg_analysis_description+=("\n\t\tUser is asking a question or expressing a request. ")
            if value == 'fact':
                msg_is_fact = True
                # print("\t\tUser is making a statement or opinion.")
                msg_analysis_description+=("\n\t\tUser is making a definite statement or opinion. ")
            if value == 'anger':
                msg_is_negative = True
                # print("\t\tUser is feeling angry or impatient or hateful.")
                msg_analysis_description+=("\n\t\tUser is feeling angry or impatient or hateful. ")
            if value == 'joy':
                msg_is_joy = True
                # print("\t\tUser is feeling joyous or enthusiastic.")
                msg_analysis_description+=("\n\t\tUser is feeling joyous or enthusiastic. ")
            if value == 'sad':
                msg_is_sad = True
                # print("\t\tUser is feeling unhappy or regretful.")
                msg_analysis_description+=("\n\t\tUser is feeling unhappy or regretful. ")
        for key, value in msg_results_dict_strong.items():
            if value[0] == 'emphatic':
                msg_is_emphatic = True
                # print("\tUser's sentiment is emphatic and / or analytical.")
                msg_analysis_description+=("\n\t\tUser's sentiment is emphatic and / or analytical. ")
            if value[0] == 'desire':
                msg_is_desire = True
                # print("\tUser is expressing desire, or wanting something.")
                msg_analysis_description+=("\n\t\tUser is expressing desire, or wanting something. ")
            if value[0] == 'instructive':
                msg_is_instructive = True
                # print("\tUser is being instructive.")
                msg_analysis_description+=("\n\t\tUser is being instructive or giving a task. ")
            if value[0] == 'certainty':
                msg_is_certainty = True
                # print("\tUser is certain about what was said.")
                msg_analysis_description+=("\n\t\tUser is certain about what was said. ")
            if value[0] == 'intensity':
                msg_is_intensity = True
                # print("\User is expressing strong feelings.")
                msg_analysis_description+=("\n\t\tUser is expressing strong feelings. ")
            if value[0] == 'challenging':
                msg_is_challenging = True
                # print("\User is expressing strong feelings.")
                msg_analysis_description+=("\n\t\tUser is being challenging, discouraging, or disagreeable. ")
            if value[0] == 'confusion':
                msg_is_confusion = True
                # print("\User is expressing strong feelings.")
                msg_analysis_description+=("\n\t\tUser is expressing uncertainty or confusion. ")
            if value[0] == 'accusative':
                msg_is_accusative = True
                # print("\User is expressing strong feelings.")
                msg_analysis_description+=("\n\t\tUser is expressing or asking something accusative in nature. ")
        print("\n\tMessage analysis description: ", msg_analysis_description)
        findMsgResponse(message,                                msg_is_positive, msg_is_negative, msg_is_question, msg_is_fact, msg_is_anger, msg_is_joy, msg_is_sad,
                        msg_is_emphatic, msg_is_desire, msg_is_instructive, msg_is_certainty, msg_is_intensity, msg_is_challenging, msg_is_confusion, msg_is_accusative)
        # Will need to keep track of overall number of messages and maintain appropriate overall conversation levels
        # print("\n\tNumber of messages in conversation: ", num_total_messages)
        return msg_is_positive, msg_is_negative, msg_is_question, msg_is_fact, msg_is_anger, msg_is_joy, msg_is_sad,
        msg_is_emphatic, msg_is_desire, msg_is_instructive, msg_is_certainty, msg_is_intensity, msg_is_challenging, msg_is_confusion, msg_is_accusative


    # Begin process for determining bot response
    def findMsgResponse(message, msg_is_positive, msg_is_negative, msg_is_question, msg_is_fact, msg_is_anger, msg_is_joy, msg_is_sad,
                        msg_is_emphatic, msg_is_desire, msg_is_instructive, msg_is_certainty, msg_is_intensity, msg_is_challenging, msg_is_confusion, msg_is_accusative):
        global texts_all
        print("\n\tNow determining best possible agent response..")
        # print("\n\tFull text database: ", texts_all)
        global response_found
        # Based on message tones (booleans), find the right database. nested branching structures
        # Add your own branches based on how the bot should respond
        if not response_found:
            if  msg_is_anger:
                text_database_to_search = []
                text_database_to_search = texts_all['apologetic']
                db_name = 'apologetic'
                searchDatabase(message, text_database_to_search, db_name)
            if  msg_is_sad or msg_is_challenging or msg_is_negative:
                text_database_to_search = []
                text_database_to_search = texts_all['encouragement_needed']
                db_name = 'encouragement_needed'
                searchDatabase(message, text_database_to_search, db_name)
            if msg_is_question or msg_is_instructive:
                text_database_to_search = []
                text_database_to_search = texts_all['tasks']
                db_name = 'tasks'
                searchDatabase(message, text_database_to_search, db_name)
            if msg_is_fact or msg_is_emphatic:
                text_database_to_search = []
                text_database_to_search = texts_all['facts']
                db_name = 'facts'
                searchDatabase(message, text_database_to_search, db_name)


    def searchDatabase(message, text_database_to_search, db_name):
        global texts_all
        global response_found
        global default_eliminated
        print("\n\tText database to search (eliminate: greetings, salutations) : \n", "\t\t*", db_name, "*\n")
        # print("\n\tComparing with original message now..: ", message, "\n")
        lastVal = 0
        comparedVal = 0
        matchingStatement = ""
        threshold = .99
        matchingStatementResponse = ""
        if not response_found and not default_eliminated:
            threshold = .99
            for each in texts_all['greetings']:
                message = message.lower()
                message = strip_punctuation(message)
                each_str = str(each[0])
                each_str = each_str.lower()
                each_str = strip_punctuation(each_str)
                lastVal = comparedVal
                comparedVal = compareSimilarities(message, each_str)
                if comparedVal > lastVal:
                    lastVal = comparedVal
                if lastVal >= threshold:
                    response_found = True
                    matchingStatementResponse = each[1]
                    print("\n\tBest possible response found.")
                    print("\n\n\t  Y O U : ", "\t", message)
                    print("\n\n\t  E M O T E R : ", "\t", matchingStatementResponse)
                    getInput(message)
                    return matchingStatementResponse
                # print("Compared val with: ", "\t", comparedVal, "\t", each[0])
                if lastVal <= threshold:
                    if threshold >= .70:
                        threshold -= .05
                        # print("\n\tNo matching response found.. lowering threshold.\t", threshold)
                    else:
                        # print("\n\tScanning other databases..")
                        response_found = False
                        default_eliminated = True
                        pass
        if not response_found and not default_eliminated:
            threshold = .99
            for each in texts_all['salutations']:
                # compareSimilarities(message, each[0])
                message = message.lower()
                message = strip_punctuation(message)
                each_str = str(each[0])
                each_str = each_str.lower()
                each_str = strip_punctuation(each_str)
                lastVal = comparedVal
                comparedVal = compareSimilarities(message, each_str)
                if comparedVal > lastVal:
                    lastVal = comparedVal
                if lastVal >= threshold:
                    response_found = True
                    matchingStatementResponse = each[1]
                    print("\tBest possible response found.")
                    print("\n\n\t  Y O U : ", "\t", message)
                    print("\n\n\t  E M O T E R  : ", "\t", matchingStatementResponse)
                    getInput(message)
                    return matchingStatementResponse
                # print("Compared val with: ", "\t", comparedVal, "\t", each[0])
                if lastVal <= threshold:
                    if threshold >= .70:
                        threshold -= .05
                        # print("\n\tNo matching response found.. lowering threshold.\t", threshold)
                    else:
                        # print("\n\tScanning other databases..")
                        response_found = False
                        default_eliminated = True
                        pass
        if not response_found:
            threshold = .99
            for each in texts_all[db_name]:
                message = message.lower()
                message = strip_punctuation(message)
                each_str = str(each[0])
                each_str = each_str.lower()
                each_str = strip_punctuation(each_str)
                lastVal = comparedVal
                comparedVal = compareSimilarities(message, each_str)
                if comparedVal > lastVal:
                    lastVal = comparedVal
                if lastVal >= threshold:
                    response_found = True
                    matchingStatementResponse = each[1]
                    print("\tBest possible response found.")
                    print("\n\n\t  Y O U : ", "\t", message)
                    print("\n\n\t  E M O T E R : ", "\t", matchingStatementResponse)
                    getInput(message)
                    return matchingStatementResponse
                if lastVal <= threshold:
                    if threshold >= .65:
                        threshold -= .05
                        # print("\n\tNo matching response found in:", db_name, "lowering threshold.\t", threshold)
                    else:
                        print("\n\tScanning other databases..")
                        response_found = False
                        pass
                    # getInput()
        # If resposne can't be found in matching database, just look through everything.
        # For now, it looks through "all" the texts, but eventually, it should look for second, third, or even fourth and fifth closest matching text / conversation.
        if not response_found:
            threshold = .99
            for each in texts_all['all']:
                message = message.lower()
                message = strip_punctuation(message)
                each_str = str(each[0])
                each_str = each_str.lower()
                each_str = strip_punctuation(each_str)
                lastVal = comparedVal
                comparedVal = compareSimilarities(message, each_str)
                if comparedVal > lastVal:
                    lastVal = comparedVal
                if lastVal >= threshold:
                    response_found = True
                    matchingStatementResponse = each[1]
                    print("\tBest possible response found.")
                    print("\n\n\t  Y O U : ", "\t", message)
                    print("\n\n\t  E M O T E R : ", "\t", matchingStatementResponse)
                    getInput(message)
                    return matchingStatementResponse
                if lastVal <= threshold:
                    if threshold >= .5:
                        threshold -= .05
                        # print("\n\tNo matching response found.. lowering threshold.\t", threshold)
                    else:
                        response_found = False
                        print("\n\n\tAgent failiure. Could not find response in database! Please try again.")
                        getInput(message)
                        # pass
        return matchingStatementResponse


    # Determine sentence similarities through Python's SequenceMatcher

    def compareSimilarities(inputted_user_msg, stored_user_msgs):
        # get_cosine(inputted_user_msg, stored_user_msg_match)
        # print("\n\tComparing: ", "\t", inputted_user_msg, "\t", stored_user_msgs)
        # val = get_cosine(inputted_user_msg, stored_user_msgs)
        val = similar(inputted_user_msg, stored_user_msgs)
        return val

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def strip_punctuation(s):
        return ''.join(c for c in s if c not in punctuation)

    # Custom code for determing sentence similarities

    # def get_cosine(vec1, vec2):
    #      intersection = set(vec1.keys()) & set(vec2.keys())
    #      numerator = sum([vec1[x] * vec2[x] for x in intersection])
    #      sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    #      sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    #      denominator = math.sqrt(sum1) * math.sqrt(sum2)
    #      if not denominator:
    #         return 0.0
    #      else:
    #         return float(numerator) / denominator

    # def text_to_vector(text):
    #      words = WORD.findall(text)
    #      return Counter(words)


if __name__ == '__main__':
    runningScript = True
    firstTime = True
    # emoter = Emoter()
    trainDatabase()
    message = ""
    getInput(message)

else:
    runningScript = False
    # emoterClassOn = True
    firstTime = True
