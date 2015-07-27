'''
Created on 19 mai 2015

@author: rux
'''
# Restrict access to todo lists/views to `is_staff()` users.
# False here falls back to `is_authenticated()` users.
TODO_STAFF_ONLY = True

# If you use the "public" ticket filing option, to whom should these tickets be assigned?
# Must be a valid username in your system. If unset, unassigned tickets go to the first superuser.
TODO_DEFAULT_ASSIGNEE = 'admin'

# If you use the "public" ticket filing option, to which list should these tickets be saved?
# Defaults to first list found, which is probably not what you want!
TODO_DEFAULT_LIST_ID = 23

# If you use the "public" ticket filing option, to which *named URL* should the user be
# redirected after submitting? (since they can't see the rest of the ticket system).
# Defaults to "/"
TODO_PUBLIC_SUBMIT_REDIRECT = 'dashboard'


STAFF_ONLY = TODO_STAFF_ONLY
DEFAULT_ASSIGNEE = TODO_DEFAULT_ASSIGNEE
DEFAULT_LIST_ID = TODO_DEFAULT_LIST_ID
PUBLIC_SUBMIT_REDIRECT = TODO_PUBLIC_SUBMIT_REDIRECT