"""- a very good scenario to work with stacks is browisng session
- for examples, when a user goes into pages in a website
- when they press back, you remove the session from the stack
- it goes with a phenomenon LIFO - Last In First Out
- a code example of how it works below """

browsing_session = [1,2]
# user goes adds to their session
browsing_session.append(3)
#  when a user presses back
browsing_session.pop()
# a better way to do it is
browsing_session = [1,2]
# user goes adds to their session
browsing_session.append(3)
# when a user clicks on back remove the last item
browsing_session.pop()
#check if the list is not empty
if not browsing_session:
        #taking the user to the previous website on the stack
        print('redirect',browsing_session[-1])