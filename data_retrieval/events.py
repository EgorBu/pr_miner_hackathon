class Event(object):
    def __str__(self):
        return "{} {}".format(self.type, self.created_at)

class Commit(Event):
    def __init__(self, commit):
        self.type = "Commit"
        self.created_at = commit.author.created_at
        self.committer  = commit.committer.name

class CommonComment(Event):
    def __init__(self, comment, type):
        self.type = type
        self.created_at = comment.created_at
        self.path       = comment.path
        self.diff_hunk  = comment.diff_hunk
        self.author     = comment.user.name
        self.body       = comment.body

    def __str__(self):
        return "{} {} {} {}".format(self.type, self.created_at, self.path, self.body)

class Comment(CommonComment):
    def __init__(self, comment):
        super(self.__class__, self).__init__(comment, "Comment")

class ReviewComment(CommonComment):
    def __init__(self, comment):
        super(self.__class__, self).__init__(comment, "ReviewComment")
