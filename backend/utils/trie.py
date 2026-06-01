class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):

        node = self.root

        for char in word.lower():

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def _search(
        self,
        node,
        prefix,
        results,
        limit
    ):

        if len(results) >= limit:
            return

        if node.is_end:
            results.append(prefix)

        for char, child in node.children.items():

            self._search(
                child,
                prefix + char,
                results,
                limit
            )

    def search_prefix(
        self,
        prefix: str,
        limit: int = 5
    ):

        node = self.root

        prefix = prefix.lower()

        for char in prefix:

            if char not in node.children:
                return []

            node = node.children[char]

        results = []

        self._search(
            node,
            prefix,
            results,
            limit
        )

        return results