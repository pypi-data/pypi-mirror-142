import requests
import string
import random
import aiohttp


class Client:
    """
    Represents a synchronous Client for fetching reddit posts
    """

    def __init__(self, agent, key):
        self.agent = agent
        self.key = key

    class Subreddit:
        r"""
        Gets the raw data on a subreddit, which can be fetched via the various methods here Parameters: name: str -
        The name of the subreddit mode: str - 'top', 'hot', or 'new' kind of posts limit: int - The number of posts
        to fetch, defaults to 25 if not specified limit does not follow a zero index, but all the methods under
        Subreddit() follow zero index. This may be changed sooner or later
        """

        def __init__(self, mode, name, limit: int = 25):
            self.name = name
            self.mode = mode
            self.limit = limit
            self.agent = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=8))
            if limit:
                if mode == 'top':
                    self.json = requests.get(
                        'https://www.reddit.com/r/{}/top/.json?limit={}'.format(name, self.limit),
                        headers={'User-Agent': self.agent}).json()
                elif mode == 'hot':
                    self.json = requests.get(
                        'https://www.reddit.com/r/{}/hot/.json?limit={}'.format(name, self.limit),
                        headers={'User-Agent': self.agent}).json()
                elif mode == 'new':
                    self.json = requests.get(
                        'https://www.reddit.com/r/{}/new/.json{}'.format(name, self.limit),
                        headers={'User-Agent': self.agent}).json()

        def selftext(self, index: int):
            r"""Returns the selftext of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').selftext(0)"""
            return self.json['data']['children'][index]['data']['selftext']

        def title(self, index: int):
            r"""Returns the title of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').title(0)"""
            return self.json['data']['children'][index]['data']['title']

        def post_url(self, index: int):
            r"""Returns the url of the post at the specified index
                  Example: reddit.Client('agent', 'key').Subreddit('top', 'python').url(0)"""
            return 'https://reddit.com' + self.json['data']['children'][index]['data']['permalink']

        def author(self, index: int):
            r"""Returns the author of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').author(0)"""
            return self.json['data']['children'][index]['data']['author']

        def image(self, index: int):
            r"""Returns any image in the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').image(0)
                Possible exceptions: KeyError, IndexError"""

            try:
                return self.json['data']['children'][index]['data']['url_overridden_by_dest']
            except KeyError:
                raise KeyError('No image found')

        def num_comments(self, index: int):
            r"""Returns the number of comments of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').num_comments(0)"""
            return self.json['data']['children'][index]['data']['num_comments']

        def upvotes(self, index: int):
            r"""Returns the number of upvotes of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').upvotes(0)"""
            return self.json['data']['children'][index]['data']['ups']

        def downvotes(self, index: int):
            r"""Returns the number of downvotes of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').downvotes(0)"""
            return self.json['data']['children'][index]['data']['downs']

        def score(self, index: int):
            r"""Returns the score of the post at the specified index
                Example: reddit.Client('agent', 'key'Async).Subreddit('top', 'python').score(0)"""
            return self.json['data']['children'][index]['data']['score']

        def permalink(self, index: int):
            r"""Returns the permalink of the post at the specified index
                Example: reddit.Client('agent', 'key').Subreddit('top', 'python').permalink(0)"""
            return self.json['data']['children'][index]['data']['permalink']


class AsyncClient:
    """
    Represents an asynchronous Client for fetching reddit posts
    """

    def __init__(self, agent, key):
        self.agent = agent
        self.key = key

    class Subreddit:
        r"""
        Gets the raw data on a subreddit, which can be fetched via the various methods here Parameters: name: str -
        The name of the subreddit mode: str - 'top', 'hot', or 'new' kind of posts limit: int - The number of posts
        to fetch, defaults to 25 if not specified limit does not follow a zero index, but all the methods under
        Subreddit() follow zero index. This may be changed sooner or later
        """

        async def subreddit_main(self, mode, name, limit):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://www.reddit.com/r/{name}/{mode}.json?limit={limit}") as resp:
                    return await resp.json()

        def __init__(self, mode, name, limit: int = 25):
            self.name = name
            self.mode = mode
            self.limit = limit
            self.agent = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=8))

        async def __call__(self):
            self.json = await self.subreddit_main(self.mode, self.name, self.limit)

        async def selftext(self, index: int):
            r"""Returns the selftext of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').selftext(0)"""
            return self.json['data']['children'][index]['data']['selftext']

        async def title(self, index: int):
            r"""Returns the title of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').title(0)"""
            return self.json['data']['children'][index]['data']['title']

        async def post_url(self, index: int):
            r"""Returns the url of the post at the specified index
                  Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').url(0)"""
            return 'https://reddit.com' + self.json['data']['children'][index]['data']['permalink']

        async def author(self, index: int):
            r"""Returns the author of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').author(0)"""
            return self.json['data']['children'][index]['data']['author']

        async def image(self, index: int):
            r"""Returns any image in the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').image(0)
                Possible exceptions: KeyError, IndexError"""

            try:
                return self.json['data']['children'][index]['data']['url_overridden_by_dest']
            except KeyError:
                raise KeyError('No image found')

        async def num_comments(self, index: int):
            r"""Returns the number of comments of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').num_comments(0)"""
            return self.json['data']['children'][index]['data']['num_comments']

        async def upvotes(self, index: int):
            r"""Returns the number of upvotes of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').upvotes(0)"""
            return self.json['data']['children'][index]['data']['ups']

        async def downvotes(self, index: int):
            r"""Returns the number of downvotes of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').downvotes(0)"""
            return self.json['data']['children'][index]['data']['downs']

        async def score(self, index: int):
            r"""Returns the score of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').score(0)"""
            return self.json['data']['children'][index]['data']['score']

        async def permalink(self, index: int):
            r"""Returns the permalink of the post at the specified index
                Example: await reddit.AsyncClient('agent', 'key').Subreddit('top', 'python').permalink(0)"""
            return self.json['data']['children'][index]['data']['permalink']
