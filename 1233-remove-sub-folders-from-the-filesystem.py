# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        If the original folders is ["/ad","/ad/af","/aa"], will sort the folders to ["/aa","/ad","/ad/af"]
        """
        sorted_folders = sorted(folder)

        result = [sorted_folders[0]]

        for i in range(1, len(sorted_folders)):
            last_folder = result[-1] + "/"

            if not sorted_folders[i].startswith(last_folder):
                result.append(sorted_folders[i])

        return result

if __name__ == '__main__':
    s = Solution()
    folders = ["/ad","/ad/af","/aa"]
    print(s.removeSubfolders(folders))  # ["/a","/c/d","/c/f"]


    