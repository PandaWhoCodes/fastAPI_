def get_posts(count: int = 10, page: int = 1):

    dummy = {
        "count": count,
        "page": page,
        "posts": [
            {
                "post_title": "Test",
                "post_picture": ".png",
                "post_excrept": "this is another test to check if things are working",
            }
        ],
    }
    return dummy

