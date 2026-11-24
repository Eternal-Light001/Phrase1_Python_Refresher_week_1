# STEP 1
# Import os to list the folders on my desktop
# Make it in form of list

# TEST TABLE
# Your desktop folders/ Files are:- C:\Users\SIWES/desktop
# Exists:- True
# ['A.txt', 'aegis-demo', 'aegis-demo.html', 'AI', 'app.py', 'as.txt', 'Backend', 'banking app.py', 'Cons', 'dashboard.py', 'desktop.ini', 'FONT  END &  BACK END', 'GitHub Desktop.lnk', 'Index.html', 'Java Program', 'Just Sales Web', 'LightCom_Project', 'LightSkillHub - Chrome.lnk', 'LightsURL', 'lighturl', 'main.py', 'Microsoft Edge.lnk', 'Mini AI', 'My Bank', 'MySchol code.txt', 'Oladipo - Chrome.lnk', 'Osun HTML', 'Portfolio', 'praise', 'promp', 'Python Tutorial for Programmers - Python Crash Course.mp4', 'Python_Automation_and_Scripting', 'python_bank', 'python_bank.zip', 'Python_Refresher', 'Qs_word2000', 'R 4.6.1.lnk', 'r small prompt.txt', 'RRG Games', 'Tele python', 'The Student Score & Grade Checker', 'Ton', 'Turtle', 'Visual Studio Code.lnk', 'VitalAid Connect', 'VSCode', 'website 1']
# Total items: 47
# - (0, 'A.txt')
# - (1, 'aegis-demo')
# - (2, 'aegis-demo.html')
# - (3, 'AI')
# - (4, 'app.py')
# - (5, 'as.txt')
# - (6, 'Backend')
# - (7, 'banking app.py')
# - (8, 'Cons')
# - (9, 'dashboard.py')
# - (10, 'desktop.ini')
# - (11, 'FONT  END &  BACK END')
# - (12, 'GitHub Desktop.lnk')
# - (13, 'Index.html')
# - (14, 'Java Program')
# - (15, 'Just Sales Web')
# - (16, 'LightCom_Project')
# - (17, 'LightSkillHub - Chrome.lnk')
# - (18, 'LightsURL')
# - (19, 'lighturl')
# - (20, 'main.py')
# - (21, 'Microsoft Edge.lnk')
# - (22, 'Mini AI')
# - (23, 'My Bank')
# - (24, 'MySchol code.txt')
# - (25, 'Oladipo - Chrome.lnk')
# - (26, 'Osun HTML')
# - (27, 'Portfolio')
# - (28, 'praise')
# - (29, 'promp')
# - (30, 'Python Tutorial for Programmers - Python Crash Course.mp4')
# - (31, 'Python_Automation_and_Scripting')
# - (32, 'python_bank')
# - (33, 'python_bank.zip')
# - (34, 'Python_Refresher')
# - (35, 'Qs_word2000')
# - (36, 'R 4.6.1.lnk')
# - (37, 'r small prompt.txt')
# - (38, 'RRG Games')
# - (39, 'Tele python')
# - (40, 'The Student Score & Grade Checker')
# - (41, 'Ton')
# - (42, 'Turtle')
# - (43, 'Visual Studio Code.lnk')
# - (44, 'VitalAid Connect')
# - (45, 'VSCode')
# - (46, 'website 1')


import os as o

desktop = o.path.expanduser("~/desktop")
print(f"Your desktop folders/ Files are:- {desktop}")

print(f"Exists:- {o.path.exists(desktop)}")

items = o.listdir(desktop)
print(f"Total items: {len(items)}")

for item in enumerate(items):
    print(f"- {item}")

