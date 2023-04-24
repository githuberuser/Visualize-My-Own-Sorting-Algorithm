import time
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def my_sorting_algorithm(arr):
    start_time = time.time()
    frames = []


# Replace the code below with your own sorting algorithm
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 




        plt.cla()
        plt.bar(np.arange(len(arr)), arr, color='purple')
        plt.title('My Sorting Algorithm Visualization')
        plt.xlabel('Index')
        plt.ylabel('Value')
        end_time = time.time()
        plt.text(0, max(arr), f'Time used: {end_time - start_time:.2f} seconds', fontsize=10)
        plt.pause(0.001) # Decrease pause time to speed up animation

        # Save the current frame as an image
        fig = plt.gcf()
        fig.canvas.draw()
        img = np.array(fig.canvas.renderer.buffer_rgba())
        frames.append(img)
    plt.show()
    # Save the frames as a video
    height, width, layers = frames[0].shape
    size = (width, height)
    out = cv2.VideoWriter('my_sorting_algorithm.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
    for i in range(len(frames)):
        out.write(cv2.cvtColor(frames[i], cv2.COLOR_RGBA2BGR))
    out.release()

arr = np.random.permutation(70) + 1

my_sorting_algorithm(arr)
print('Video saved: ',os.path.join(os.getcwd()))


