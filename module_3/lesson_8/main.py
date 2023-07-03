strs = ["alic3","bob","3","4","00000"]
max_ = float("-inf")
for i in strs:
    if i.isdigit():
        max_ = max(int(i) , max_)
    else:
        max_ = max(len(i) , max_)
print(max_)

print(max(list(map(lambda x : int(x) if x.isdigit() else len(x) , strs))))

"""
sudo apt-get install git
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dilshodev3234/Test.git
git push -u origin main
"""