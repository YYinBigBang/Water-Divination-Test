#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri


class NenTestContent:
    """A database for the Nen test."""
    ques_dict = {
        1: '有一天你走在路上看到兩隻被拋棄的黑貓，你會怎麼做？',
        2: '2承上題，理由是?',
        3: '3承上題，理由是?',
        4: '早上起床後發現天空烏雲密布，聽天氣預報說降雨概率為40%。你出門會帶傘嗎？',
        5: '和朋友約好出去玩，可是約定時間到了朋友卻沒有來。你大約會忍耐多久？',
        6: '情況相反，這次是你遲到了。對方似乎很生氣，你會怎麼做？',
        7: '早上醒來你發現自己變成動物了，是哪種動物？',
        8: '承上題，為什麼這麼想？',
        9: '你最擅長的科目是？',
        10: '你最討厭的科目是？',
        11: '如果你成為了盜賊，第一次想偷的什麼？',
        12: '你覺得自己的優點有？',
        13: '你覺得自己的缺點有？',
        14: '什麼樣的人會讓你真的起殺心？',
        15: '什麼情況下你會想哭？',
        16: '覺得魔術師很厲害嗎？',
        17: '用行動力逮捕犯人的警察是錯誤的？',
        18: '書架上的書順序排得亂七八糟的話會不舒服嗎？',
        19: '絕對不會花心嗎？',
        20: '只要自己好的話其他怎樣都無所謂嗎？',
        21: '不喜歡整理收拾嗎？'
    }
    ans_dict = {
        1: {'A': '帶牠們走', 'B': '不帶牠們走'},
        2: {'A': '無論如何都要養！', 'B': '雖然想養，但會有人反對，所以找別人來養', 'C': '不想自己養，會找別人來養', 'D': '其它的理由'},
        3: {'A': '因為家裡不能養寵物', 'B': '因為黑貓不吉利', 'C': '雖然很可愛，但總有一天會感到厭煩'},
        4: {'A': '覺得一定會下雨，因此帶傘出門', 'B': '似乎會下雨，帶摺疊傘出門', 'C': '不帶傘(賭它不會下雨)'},
        5: {'A': '無法忍耐', 'B': '5分鐘左右', 'C': '10分鐘左右', 'D': '15分鐘左右', 'E': '20分鐘左右', 'F': '一直等下去'},
        6: {'A': '道歉，並向朋友解釋清楚', 'B': '道歉，拚命取悅朋友', 'C': '道歉，以後提早20分到達',
            'D': '解釋，但不認錯', 'E': '解釋，並取悅朋友', 'F': '不會有這種事發生'},
        7: {'A': '綿羊', 'B': '黑豹', 'C': '猴子', 'D': '老虎', 'E': '狼', 'F': '珀伽索斯（希臘神話中的飛馬）', 'G': '獅子'},
        8: {'A': '因為動物占卜裡自己測出來是它', 'B': '因為喜歡這種動物', 'C': '因為想變成這種動物', 'D': '直覺'},
        9: {'A': '數理', 'B': '語言', 'C': '政治社會歷史', 'D': '音樂美術創作', 'E': '體育', 'F': '沒有特別擅長的科目'},
        10: {'A': '數理', 'B': '語言', 'C': '政治社會歷史', 'D': '音樂美術創作', 'E': '體育', 'F': '沒有特別討厭的科目'},
        11: {'A': '人命', 'B': '錢', 'C': '鑽石、寶石', 'D': '美術品', 'E': '古書', 'F': '絕對不會成為盜賊'},
        12: {'A': '規規矩矩', 'B': '有責任感', 'C': '被人信賴', 'D': '引人注目的特長', 'E': '對自己要求嚴格',
             'F': '有行動力', 'G': '有很多朋友', 'H': '反复無常難以捉摸', 'I': '擅長唱歌畫畫', 'J': '利己主義',
             'K': '擅長精細活', 'L': '隨自我的步調行事'},
        13: {'A': '協調性差', 'B': '粗心大意', 'C': '容易說謊', 'D': '討厭的人有10人以上', 'E': '對錢斤斤計較',
             'F': '覺得沒道理的事就無法接受', 'G': '自我中心、自大', 'H': '為達目的不擇手段', 'I': '容易焦躁', 'J': '心軟、淚點低',
             'K': '慢半拍', 'L': '意志不堅'},
        14: {'A': '殺了自己家人的人', 'B': '殺了自己喜歡的人的人', 'C': '給了自己最大屈辱的人', 'D': '想殺自己的人',
             'E': '在自己面前大量濫殺無辜的人', 'F': '背叛自己的人'},
        15: {'A': '重要的人死去', 'B': '覺得悲傷', 'C': '被甩時', 'D': '被求婚或結婚時', 'E': '覺得感動',
             'F': '達成重大目標時', 'G': '工作遇到大失敗的時候', 'H': '身邊長時間沒人時', 'I': '痛的時候', 'J': '自尊心受傷時',
             'K': '被朋友背叛', 'L': '通常都不太會哭'},
        16: {'O': '是', 'X': '否'},
        17: {'O': '是', 'X': '否'},
        18: {'O': '是', 'X': '否'},
        19: {'O': '是', 'X': '否'},
        20: {'O': '是', 'X': '否'},
        21: {'O': '是', 'X': '否'}
    }
    weight_dict = {
        1: {'A': '強放操+10', 'B': '變具特+10'},
        2: {'A': '強+30', 'B': '操+30', 'C': '放+30', 'D': '無+0'},
        3: {'A': '特+30', 'B': '具+30', 'C': '變+30'},
        4: {'A': '具操+15', 'B': '放特+15', 'C': '強變+15'},
        5: {'A': '放+30', 'B': '具+30', 'C': '強+30', 'D': '特+30', 'E': '變+30', 'F': '操+30'},
        6: {'A': '具+30', 'B': '放+30', 'C': '特+30', 'D': '變+30', 'E': '操+30', 'F': '強+30'},
        7: {'A': '放+30', 'B': '操+30', 'C': '具+30', 'D': '強+30', 'E': '變+30', 'F': '放+30', 'G': '特+30'},
        8: {'A': '具操+15', 'B': '強放+15', 'C': '變特+15', 'D': '全+5'},
        9: {'A': '具+35', 'B': '操+35', 'C': '放+30', 'D': '特+30', 'E': '強+30', 'F': '變+30'},
        10: {'A': '強+30', 'B': '特+30', 'C': '變+30', 'D': '操+30', 'E': '具+30', 'F': '放+30'},
        11: {'A': '變+30', 'B': '強+30', 'C': '放+30', 'D': '特+30', 'E': '具+30', 'F': '操+30'},
        12: {'A': '具+30', 'B': '強+30', 'C': '操+30', 'D': '特+30', 'E': '放+30', 'F': '強+30',
             'G': '放+30', 'H': '變+30', 'I': '特+30', 'J': '變+30', 'K': '具+30', 'L': '操+30'},
        13: {'A': '強+30', 'B': '放+30', 'C': '變+30', 'D': '具+30', 'E': '變+30', 'F': '操+30',
             'G': '特+30', 'H': '具+30', 'I': '放+30', 'J': '特+30', 'K': '操+30', 'L': '強+30'},
        14: {'A': '放+30', 'B': '強+30', 'C': '具+30', 'D': '操+30', 'E': '變+30', 'F': '特+30'},
        15: {'A': '強+30', 'B': '具+30', 'C': '具+30', 'D': '放+30', 'E': '操+30', 'F': '強+30',
             'G': '變+30', 'H': '變+30', 'I': '放+30', 'J': '特+30', 'K': '特+30', 'L': '操+30'},
        16: {'O': '變+30', 'X': '強放操特具+6'},
        17: {'O': '操+30', 'X': '強放特變具+6'},
        18: {'O': '具+30', 'X': '強放操特變+6'},
        19: {'O': '強+30', 'X': '放操特變具+6'},
        20: {'O': '特+30', 'X': '強放操變具+6'},
        21: {'O': '放+30', 'X': '強操特變具+6'}
    }
    nen_type_dict = {
        'enhancement': 0,
        'transmutation': 0,
        'conjuration': 0,
        'specialization': 0,
        'manipulation': 0,
        'emission': 0
    }


class NenTestControl(NenTestContent):
    """A context manager for Nen test."""
    def __init__(self):
        self.gen_question = self.question_flow()
        self.trigger = False
        self.ques1 = 'N'
        self.response = ''
        # The weights of Nen type
        self.nen_type_dict = {
            'enhancement': 0,
            'transmutation': 0,
            'conjuration': 0,
            'specialization': 0,
            'manipulation': 0,
            'emission': 0
        }

    def sum_nen_weight(self, ans_weights: str):
        """Get Nen weights from string and add up the weights."""
        items, weight = ans_weights.split('+')
        weight = int(weight)
        for item in items:
            if item == '強':
                self.nen_type_dict['enhancement'] += weight
            elif item == '變':
                self.nen_type_dict['transmutation'] += weight
            elif item == '具':
                self.nen_type_dict['conjuration'] += weight
            elif item == '特':
                self.nen_type_dict['specialization'] += weight
            elif item == '操':
                self.nen_type_dict['manipulation'] += weight
            elif item == '放':
                self.nen_type_dict['emission'] += weight
            elif item == '全':
                for nen_type in self.nen_type_dict:
                    self.nen_type_dict[nen_type] += weight
            else:
                continue

    def check_ans_available(self, index, user_ans):
        """Check if the user's answer is within the options."""
        if user_ans := user_ans.upper().replace(' ', ''):
            if index == 1:
                if user_ans in self.ans_dict[index].keys():
                    self.ques1 = user_ans
                    return True
                return False
            elif index <= 10:
                print(self.ans_dict[index].items())
                if user_ans in self.ans_dict[index].keys():
                    return True
                return False
            elif index > 14:
                user_ans = user_ans.replace('A', 'O').replace('B', 'X')
                if user_ans in self.ans_dict[index].keys():
                    return True
                return False
            else:
                for letter in user_ans:
                    if letter not in self.ans_dict[index].keys():
                        return False
                return True
        else:
            return False

    def question_flow(self):
        """A generator for filing the question and options of Nen."""
        for index in range(1, 22):  # loop through 20 Nen questions in order.
            if index == 2 and self.ques1 == 'B':
                continue
            if index == 3 and self.ques1 == 'A':
                continue
            user_ans = yield self.ques_dict[index], self.ans_dict[index]
            print(user_ans)
            while not self.check_ans_available(index, user_ans):
                user_ans = yield '請回答有效的選項!!', self.ans_dict[index]
            # sum the weight of each option.
            for w in user_ans:
                self.sum_nen_weight(self.weight_dict[index][w])
        return '測驗結束', str(self.gen_nen_chart())  # TODO: call function to generate chart

    def chat_monitor(self, user_txt):
        """Capture keywords to trigger/resume Nen test."""
        user_txt = user_txt.strip()
        print('=============')
        if self.trigger:
            if user_txt in '結束':
                self.trigger = False
                self.gen_question = self.question_flow()
                # TODO: recover the Nen test
            else:
                return self.gen_question.send(user_txt)
        elif user_txt in ['開始', 'start']:
            try:
                self.trigger = True
                return next(self.gen_question)
            except StopIteration:
                self.trigger = False
                return 'None'
        else:
            return '念能力測驗尚未開始!!'

    def gen_nen_chart(self):
        proportions = [x/200 for x in self.nen_type_dict.values()]
        print(list(self.nen_type_dict.values()))
        labels = ['Enhancement', 'Transmutation', 'Conjuration', 'Specialization', 'Manipulation', 'Emission']
        N = len(proportions)
        proportions = np.append(proportions, 1)
        theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
        x = np.append(np.sin(theta), 0)
        y = np.append(np.cos(theta), 0)
        triangles = [[N, i, (i+1) % N] for i in range(N)]
        triang_backgr = tri.Triangulation(x, y, triangles)
        triang_foregr = tri.Triangulation(x * proportions, y * proportions, triangles)
        colors = np.linspace(0, 18, N+1)
        plt.tripcolor(triang_backgr, colors, cmap='Spectral', shading='gouraud', alpha=0)
        plt.tripcolor(triang_foregr, colors, cmap='Spectral', shading='gouraud', alpha=0.9)
        plt.triplot(triang_backgr, color='black', lw=1)
        for label, color, xi, yi in zip(labels, colors, x, y):
            plt.text(xi * 1.05, yi * 1.05, label,  # color=cmap(color),
                     ha='left' if xi > 0.1 else 'right' if xi < -0.1 else 'center',
                     va='bottom' if yi > 0.1 else 'top' if yi < -0.1 else 'center')
        plt.axis('off')
        plt.gca().set_aspect('equal')
        plt.show()
        return self.nen_type_dict



if __name__ == "__main__":
    chatbot = NenTestControl()
    while True:
        txt = input('Input: ')
        if txt == '結束':
            break
        else:
            ret = chatbot.chat_monitor(txt)
            print(ret)
