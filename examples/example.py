import sys

sys.path.append('../code')
from target_reader import target_reader

sample_file = 'example_target.jpg'

tr = target_reader()
result = tr.run(sample_file)
if result:
    print('Failed:', result)
else:
    print('Success!')