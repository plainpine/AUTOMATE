import ezgmail
unreadThreads = ezgmail.unread()
ezgmail.summary(unreadThreads)
print(ezgmail.summary(unreadThreads))
