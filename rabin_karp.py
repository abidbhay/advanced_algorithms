def lengthOfLongestSubstring(s):
        max_len=0
        visited=""
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                
                max_len=max(max_len, len(visited))
                visited=visited[hashmap[s[i]]+1:]
                
            
            hashmap[s[i]]=i
            visited+=s[i]
        max_len=max(max_len, len(visited))

        return max_len

print(lengthOfLongestSubstring("tmmzuxt"))