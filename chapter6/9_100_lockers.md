# 100 Lockers

## Question

There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?

## Answer

On pass i, locker j will be toggled if and only if i is a factor of j. Thus, locker j will be toggled the same number of times as the number of distinct factors it has. If will only remain open if it has an odd number of factors. But factors come in pairs; there will only be a singleton factor if a number is a perfect square. Thus, only the perfect squares (1, 4, 9, 16, ..., 100) will remain open.
