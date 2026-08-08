class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ## Created the hash dict 
        main_dict ={}

        # iteration over each word present in the list
        for word in strs:
            # here we are creating keys, such that by sorting the chars in each word we can
            # have the unique keys across the list
            key = tuple(sorted(word))

            # now check if new word is not present in the dict create new key for that word
            if key not in main_dict:
                main_dict[key] = []
            
            # add the word correspond key
            main_dict[key].append(word) 
            ##{('a', 'c', 't'): ['act'], ('o', 'p', 's', 't'):['pots', 'tops']} 

        return list(main_dict.values())

        