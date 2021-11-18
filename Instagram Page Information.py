from instagramy import InstagramUser

user = InstagramUser('medaitchikh')
print('UserName = ',user.username)
print('Followers = ',user.number_of_followers)
print('Following = ',user.number_of_followings)
print('Mutual Followings = ',user.no_of_mutual_follower)
print('No. of Posts = ',user.number_of_posts)
print('is Private = ',user.is_private)

