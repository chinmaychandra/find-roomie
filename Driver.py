from roomate_matcher import get_roommate_matches
from Viewer import show_user_details
from Viewer import show_multiple_users

result = get_roommate_matches(1234)
result.append(1234)
show_multiple_users(result)
print(result)