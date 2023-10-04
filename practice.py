from pathlib import Path
p = Path('d:\\')
p = p/'qa_automation'/'lahernyi_git'/'aqa_py'/'textik.txt'
with p.open('r') as file:
    f = file.read()
#print(f)
print(Path(__file__))
