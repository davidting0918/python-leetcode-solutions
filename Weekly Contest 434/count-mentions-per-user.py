# https://leetcode.com/contest/weekly-contest-434/problems/count-mentions-per-user/?slug=count-partitions-with-even-sum-difference&region=global_v2

from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda event: (int(event[1]), 0 if event[0] == "OFFLINE" else 1))

        n = numberOfUsers
        offline_until = {
            i: 0 for i in range(n)
        }

        mentions = [0] * n

        all_mentions = 0
        for name, time, message in events:
            time = int(time)
            if name == 'MESSAGE':
                if message == 'ALL':
                    all_mentions += 1

                elif message == 'HERE':
                    for user in range(n):
                        if offline_until[user] <= time:
                            mentions[user] += 1

                else:
                    for user in message.split():
                        user = int(user[2:])
                        mentions[user] += 1

            elif name == 'OFFLINE':
                offline_until[int(message)] = time + 60

        return [i + all_mentions for i in mentions]


if __name__ == "__main__":
    s = Solution()
    numberOfUsers = 3
    events = [["MESSAGE","1","id0 id1"],["MESSAGE","5","id2"],["MESSAGE","6","ALL"],["OFFLINE","5","2"]]
    print(s.countMentions(numberOfUsers, events)) # [2, 1]