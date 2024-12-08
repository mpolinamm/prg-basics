import queue

# Create a stack for visited websites
visited_websites = queue.LifoQueue()

# Some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back, q to quit): ')

    if website == '0':  # Go back to the previous website
        if visited_websites.empty():
            print("No previously visited websites.")
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get()  # Retrieve the last visited website
    elif website == 'q':  # Quit the program
        print("Exiting the browser simulation.")
        break
    elif website != "":  # Add a new website to the stack
        visited_websites.put(website)

    print('You are currently viewing:', website)
    print()
