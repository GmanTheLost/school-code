blog_posts = {}

next_post_id = 1

Loop = True

def create_post():
    global next_post_id
    title = input("Enter Post Title ")
    content = input("Write here ")
    blog_posts[next_post_id] = {"title" : title, "content" : content, "comments" : []}
    print(f"Post created with ID {next_post_id}")
    next_post_id += 1
    
def view_all_posts():
    if not blog_posts:
        print("No posts available.")
        return
    for post_id, post in blog_posts.items():
        print(f"Post ID:{post_id} | Title: {post["title"]} \n Content: {post["content"]}")

def view_full_post():
    if not blog_posts:
        print("No posts available.")
        return
    post_id = int(input("Enter Post ID you wish to view: "))
    if post_id in blog_posts:
        print(f"Title: {blog_posts[post_id]["title"]}")
        print(f"Content: {blog_posts[post_id]["content"]}")
        comments_list = blog_posts[post_id]["comments"]
        if len(comments_list) == 0:
            print("No one has bothered to comment. :(")
        else:
            print("\n---Comments---")
            for comment in comments_list:
                print(f"- {comment}")
    else:
        print("Post not found.")
    
def add_comment():
    post_id = int(input("Enter post ID to comment on: "))
    if post_id in blog_posts:
        comment = input("Enter your comment: ")
        blog_posts[post_id]["comments"].append(comment)
        print("Comment added!")
    else:
        print("Post not found.")  

def edit_post():
    post_id = int(input("Enter post ID you wish to edit:"))
    if post_id in blog_posts:
        post = blog_posts[post_id]
        new_title = input(f"Enter new title(leave blank to keep it as '{post["title"]}'):") or post["title"]
        new_content = input("Enter new content (leave blank to keep current): ") or post["content"]
        blog_posts[post_id] = {"title": new_title, "content": new_content, "comments": post["comments"]}
        print("Post updated successfully!")
    else:
        print("Post not found.")

def search_posts():
    term = input("Enter a keyword to search for in titles: ").lower()
    found = False
    for pid, post in blog_posts.items():
        if term in post['title'].lower():
            print(f"Match found -> Post ID: {pid}, Title: {post['title']}")
            found = True
    if not found:
        print("No matches found.")
    
def delete_post():
    post_id = int(input("Enter post ID to delete: "))
    if post_id in blog_posts:
        del blog_posts[post_id]
        print("Post deleted successfully.")
    else:
        print("Post not found.")

def check_user_input(user_choice):
    global Loop
    match user_choice:
        case 1:
            create_post()

        case 2:
            view_all_posts()

        case 3:
            view_full_post()

        case 4:
            edit_post()

        case 5:
            add_comment()
        
        case 6:
            search_posts()

        case 7:
            delete_post()

        case 8:
           Loop = False
            

        case _:
            print("Please pick a valid option. ")            


while Loop:
    print("\n===== Welcome to BLOG =====")
    print("1. Create New Post")
    print("2. View All Posts")
    print("3. View Single Post")
    print("4. Edit a Post")  
    print("5. Add a Comment")
    print("6. Search Posts")
    print("7. Delete a Post")
    print("8. LEAVE!!!")

    user_choice = int(input("Choose an option (1-8): "))
    check_user_input(user_choice)