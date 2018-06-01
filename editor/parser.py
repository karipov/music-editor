def split_title(title):
    """ Split the erroneus title into title and singer """
    title, singer = title.split(' - ')

    return title, singer
