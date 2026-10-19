## 1. Limit 
I've used `limit` (default 10, `ge=0`). so when there is a limit=0 it will just return [] and for the negative values gets rejected by FastApi with 422.

## 2. why I've ised threading and the lock
since I've used a read-then-increment at NEXT_ID in create_note along with the iteration in list_notes. I've imagined a what if scenario where if there are two threads read the same id at the same time it would just simply overwrite each other to prevent a duplication of id or runtime errors. Since im not sure with the experiment I tested the app with concurrent posts and gave a pass. but im not sure if there is a test i didnt include since ive been reading some documentations on threading.

## 3. Limits
The memory resets when the app restarts and it resets to 1. As for the lock it can only work with workers --2 and im not that sure of the whole process since im not that familiar with using threading