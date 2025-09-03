class Twitter:

    def __init__(self):
        self.posts = {}
        self.follows = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        postsq = []
        res = []
        if userId not in self.follows:
            self.follows[userId] = set()
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee in self.posts and len(self.posts[followee]):
                last_post = self.posts[followee][-1]
                last_post_index = len(self.posts[followee]) - 1 
                heapq.heappush(postsq, (-last_post[0], last_post[1], followee, last_post_index))

        while len(postsq) and len(res) < 10:
            _, postId, followee, post_index = heapq.heappop(postsq)
            res.append(postId)
            if post_index != 0:
                prev_post = self.posts[followee][post_index-1]
                heapq.heappush(postsq, (-prev_post[0], prev_post[1], followee, post_index-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)