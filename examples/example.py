import sys
import matplotlib.pyplot as plt

sys.path.append('../code')
from target_reader import target_reader

sample_file = 'example_target.jpg'

tr = target_reader()
result = tr.run(sample_file)
output_image = tr.stage_images[-1]
print('Output size:', output_image.shape)
plt.imsave('example_output.jpg', output_image)

if result:
    print('Failed:', result)
else:
    print('Success!')