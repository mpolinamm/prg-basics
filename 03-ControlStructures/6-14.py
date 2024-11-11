facebook = True
twitter = False
instagram = True

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You need more social media presence to be a good influencer.")