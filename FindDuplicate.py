class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = {}
        for path in paths:
            directory, *files = path.split(" ")
            for file in files:
                idx = file.index('(')
                content = file[idx + 1: -1]
                directory_path = directory + '/' + file[:idx]
                if content in duplicates:
                    duplicates[content].append(directory_path)
                else:
                    duplicates[content] = [directory_path]
        
        duplicates = duplicates.values()
        ans = []
        for duplicate in duplicates:
            if len(duplicate) > 1:
                ans.append(duplicate)
        return ans
                    
