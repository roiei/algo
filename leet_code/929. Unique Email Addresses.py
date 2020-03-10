import time


class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        if not emails:
            return 0
        addrs = set()
        for email in emails:
            addr = email.split('@')
            local_name = addr[0].split('+')
            local_name = local_name[0].replace('.', '')
            addrs.add(local_name + '@' + addr[-1])
        return len(addrs)


    def numUniqueEmails(self, emails: [str]) -> int:
        if not emails:
            return 0
        
        accounts = set()
        for email in emails:
            account, domain = email.split('@')
            idx = account.find('+')
            if -1 != idx:
                account = account[:idx]
            account = account.replace('.', '')
            accounts.add(account + '@' + domain)

        return len(accounts)

stime = time.time()
#print(2 == Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(2 == Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))

print('elapse time: {} sec'.format(time.time() - stime))