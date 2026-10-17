class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result  =  {}
        
        #s= strs[i]
        #t = strs[i ++ 1]
        

        for word in strs:
            sorted_word =  ''.join(sorted(word))

            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word]=[word]

        return list(result.values())


        
        
        

    
