class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        # Sort the folders lexicographically
        folder.sort()
        
        # Result list to store the non-sub-folders
        result = []
        
        for f in folder:
            # If result is empty or the current folder is not a sub-folder of the last added folder
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)  # Add the current folder to the result list
        
        return result
