from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import os
from django.http import JsonResponse

# Create your views here.
# def first_page(request):
#     return render(request, "polls/first_page.html")

def get_three_col(df):
    young = []
    working = []
    elderly = []

    for i in range(len(df)):
        young.append(list(df.iloc[i, 1:3]))
        working.append(list(df.iloc[i, 2:4]))
        elderly.append(list(df.iloc[i, 3:5]))

    return young, working, elderly

def make_100(temp_list):
    for i in range(len(temp_list)):
        if temp_list[i][1] >= 100.0:
            temp_list[i][1] = 100.0

    return temp_list

def get_cnty_file(request):

    name=request.GET.get('myinput')
    print('get_cnty_file: ', name)

    new_pop_list = os.listdir('new_pop')

    temp_df = pd.read_csv("new_pop/" + name+"_new_pop.csv")
    temp_young, temp_working, temp_elderly = get_three_col(temp_df)
    temp_elderly = make_100(temp_elderly)

    context = {'name': name, 'temp_young': temp_young, 'temp_working': temp_working, \
               'temp_elderly': temp_elderly, 'year': [i for i in range(1960, 2019)]}
    return JsonResponse(context)

    # for i in range(len(new_pop_list)):
    #     if name == None:
    #         pass
    #
    #     elif name in new_pop_list[i]:
    #         print('get_cnty_file', 'yes')
    #         temp_df = pd.read_csv("C:/Users/dbwls/Desktop/ㄹㅇ옮기기/공부/2학기/시각화/시각화 프로젝트/new_pop/" + new_pop_list[i])
    #         temp_young, temp_working, temp_elderly = get_three_col(temp_df)
    #
    #         context={'name': name, 'temp_young':temp_young, 'temp_working':temp_working, 'temp_elderly':temp_elderly}
    #         return JsonResponse(context)

def first_page(request):

    if request.method=="POST":
        print('first_page의 post')
        input=request.POST.get('input')
        print('first page의 post:', input)
        #
        # kor_df = pd.read_csv('new_pop/KOR_new_pop.csv')
        # # jpn_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/JPN_pop.csv')
        # # oecd_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/OECD_pop.csv')
        # # usa_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/USA_pop.csv')
        #
        # kor_young, kor_working, kor_elderly = get_three_col(kor_df)
        # kor_elderly=make_100(kor_elderly)
        # jpn_young, jpn_working, jpn_elderly=get_three_col(jpn_df)
        # oecd_young, oecd_working, oecd_elderly=get_three_col(oecd_df)
        # usa_young, usa_working, usa_elderly=get_three_col(usa_df)
        return render(request, 'polls/first_page.html')
        # return render(request, 'polls/first_page.html', {'year': [i for i in range(1960, 2019)], \
        #                                                          'kor_young': kor_young, 'kor_working': kor_working, \
        #                                                          'kor_elderly': kor_elderly,
        #                                                          # 'temp_young':temp_young, 'temp_working':temp_working,\
        #                                                          # 'temp_elderly':temp_elderly
        #                                                          # 'jpn_young': jpn_young,\
        #                                                          # 'jpn_working':jpn_working, 'jpn_elderly': jpn_elderly,\
        #                                                          # 'oecd_young': oecd_young, 'oecd_working': oecd_working,\
        #                                                          # 'oecd_elderly': oecd_elderly, 'usa_young': usa_young,\
        #                                                          # 'usa_working':usa_working, 'usa_elderly': usa_elderly
        #                                                          })

    elif request.method=="GET":
        print('first_page의 get')
        input=request.GET.get('input')
        print('first page의 get:', input)

        # kor_df = pd.read_csv('new_pop/KOR_new_pop.csv')
        # # jpn_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/JPN_pop.csv')
        # # oecd_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/OECD_pop.csv')
        # # usa_df=pd.read_csv('C:/Users/dbwls/django/vis_project0526/pop_data/USA_pop.csv')
        #
        # kor_young, kor_working, kor_elderly = get_three_col(kor_df)
        # kor_elderly = make_100(kor_elderly)
        # jpn_young, jpn_working, jpn_elderly=get_three_col(jpn_df)
        # oecd_young, oecd_working, oecd_elderly=get_three_col(oecd_df)
        # usa_young, usa_working, usa_elderly=get_three_col(usa_df)
        return render(request, 'polls/first_page.html')
        # return render(request, 'polls/first_page.html', {'year': [i for i in range(1960, 2019)], \
        #                                                  'kor_young': kor_young, 'kor_working': kor_working, \
        #                                                  'kor_elderly': kor_elderly,
        #                                                  # 'temp_young':temp_young, 'temp_working':temp_working,\
        #                                                  # 'temp_elderly':temp_elderly
        #                                                  # 'jpn_young': jpn_young,\
        #                                                  # 'jpn_working':jpn_working, 'jpn_elderly': jpn_elderly,\
        #                                                  # 'oecd_young': oecd_young, 'oecd_working': oecd_working,\
        #                                                  # 'oecd_elderly': oecd_elderly, 'usa_young': usa_young,\
        #                                                  # 'usa_working':usa_working, 'usa_elderly': usa_elderly
        #                                                  })





