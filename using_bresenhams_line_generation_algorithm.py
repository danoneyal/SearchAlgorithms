import bresenhams_line_generation_algorithm
import bresenhams_line_generation_algorithm as bla
# driver function
x1 = 45
y1 = 45
x2 = 1
y2 = 1

bla.BresenhamsLineGenerationAlgorithm.bresenham(x1, y1, x2, y2, 2)

len_pixel_position_array = len(pixel_position_array)

calc_result_array_short = np.zeros((2, len(pixel_position_array)))

# element = pixel_position_array[0]
calc_result_array_index = 0
for element in pixel_position_array:
    calc_result_array_short[1, calc_result_array_index] = element.vertical
    calc_result_array_short[0, calc_result_array_index] = element.horizontal
    calc_result_array_index += 1

# x = np.arange(0, 1, 0.05)
# y = np.power(x, 2)

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(0, 30, 1))
ax.set_yticks(np.arange(0, 30, 1))
# plt.scatter(x, y)
plt.scatter(calc_result_array_short[0], calc_result_array_short[1])
point1 = [x1, y1]
point2 = [x2, y2]
x_values = [point1[0], point2[0]]  # gather x-values
y_values = [point1[1], point2[1]]  # gather y-values
plt.plot(x_values, y_values)

# plt.grid()
plt.show()

# plot pixels

# define the size of the canvas
Row = 50
Cols = 50
# create an image
local_matrix_search = np.zeros((Row, Cols))

# draw the pixels on the canvas
for element in pixel_position_array:
    local_matrix_search[element.vertical][element.horizontal] = 1
    calc_result_array_index += 1

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
plt.show()

# ax1.imshow(calc_result_array, interpolation='nearest', cmap=cm.Greys_r)
# plt.show()
