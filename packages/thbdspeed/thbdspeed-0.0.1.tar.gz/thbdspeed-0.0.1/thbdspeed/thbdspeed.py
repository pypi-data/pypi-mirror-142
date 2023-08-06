import requests, os, sys, time
from time import sleep


logo = '''
\033[31m█▀▄▀█ █▀█ ▄▀█ ░░█ ░░█ █▀▀ █▀▄▀█
█░▀░█ █▄█ █▀█ █▄█ █▄█ ██▄ █░▀░█

\033[31m█░█ █▀█ █░█ 
\033[31m▀▀█ █▄█ ▀▀█ \033[1;33;40mSpeed Cheakar

\033[33m--------------------------------------------------
  \033[36mAuthor     \033[33m:\033[37m Md Moajjem Hossen
  \033[36mGitHub    \033[33m :\033[37m https://github.com/Moajjem404
 \033[36m Facebook  \033[33m :\033[37m https://fb.com/Md.Moajjem.Hossen404
  \033[36mPublic   \033[33m  : \033[37m12-02-2022
\033[33m--------------------------------------------------\033[32m 

Welcome To \033[1;33;40m404 Internet Speed Checker

'''


os.system('clear')

print(logo)

print("\033[1;34;40mPlease Wait...")



import speedtest

# Speed test
st = speedtest.Speedtest()

# Download Speed
ds = st.download()

print("\033[1;35;40mYour Download sepeed :",ds)


def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

#Readable
print(humansize(ds))


import speedtest

# Speed test
st = speedtest.Speedtest()

# Upload speed
us = st.upload()

print("\033[1;32;40mYour Upload Speed :",us)

#Readable
print(humansize(us))


st.get_servers([])
ping = st.results.ping
#display the result
print("\033[31mYour Ping is : ", ping)



time.sleep(3)

os.system('xdg-open https://www.facebook.com/Md.Moajjem.Hossen.4O4')
