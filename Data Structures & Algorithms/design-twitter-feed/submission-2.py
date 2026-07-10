class Twitter:

    def __init__(self):
        self.users = {}
        self.timer = 0        

    def _check_or_create(self, userId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {
                "tweets": [],
                "followees": set([userId]),
            }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._check_or_create(userId)
        self.users[userId]["tweets"].append((tweetId, self.timer))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        followee_id = []
        tweet_pointers = []
        for followee in self.users[userId]["followees"]:
            followee_id.append(followee)
            tweet_pointers.append(len(self.users[followee]["tweets"]) - 1)
    
        while len(feed) < 10:
            mr_tweet_time = -int(2e9)
            mr_tweet_id = -1

            for i in range(len(followee_id)):
                if (
                    tweet_pointers[i] >= 0 and
                    mr_tweet_time < self.users[followee_id[i]]["tweets"][tweet_pointers[i]][1]
                ):
                    mr_tweet_time = self.users[followee_id[i]]["tweets"][tweet_pointers[i]][1]
                    mr_tweet_id = self.users[followee_id[i]]["tweets"][tweet_pointers[i]][0]
                    tweet_pointer_id = i

            if mr_tweet_id == -1:
                break

            feed.append(mr_tweet_id)
            tweet_pointers[tweet_pointer_id] -= 1
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._check_or_create(followerId)
        self.users[followerId]["followees"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._check_or_create(followerId)
        if followeeId in self.users[followerId]["followees"]:
            self.users[followerId]["followees"].remove(followeeId)